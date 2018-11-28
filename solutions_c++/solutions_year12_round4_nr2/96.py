#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define repeat(n) for ( int repc = (n); repc > 0; --repc )
typedef long long int64;
#define foreach(i,c) for ( typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i )

int n;
int64 W, L;
int64 r[1005], x[1005], y[1005];
vector<int> placed;

bool sortmax(int a, int b) { return r[a] > r[b]; }
bool sortmin(int a, int b) { return r[a] < r[b]; }

bool okay(int tr, int64 tx, int64 ty) {
  foreach (it, placed) {
    int i = *it;
    int64
      x1 = max(tx-tr, x[i]-r[i]),
      x2 = min(tx+tr, x[i]+r[i]);
    int64
      y1 = max(ty-tr, y[i]-r[i]),
      y2 = min(ty+tr, y[i]+r[i]);
    if (x2 > x1 && y2 > y1) {
      return false;
    }
  }
  return true;
}

void try_one(int p, int64 tx, int64 ty) {
  if (tx < 0 || tx > W) {
    return;
  }
  if (ty < 0 || ty > L) {
    return;
  }
  if (x[p] == -1 ||
      ty < y[p] ||
      (ty == y[p] && tx < x[p])) {
    if (okay(r[p], tx, ty)) {
      x[p] = tx;
      y[p] = ty;
    }
  }
}

bool trysolve(int *order) {
  placed.clear();
  placed.push_back(order[0]);
  x[order[0]] = y[order[0]] = 0;
  for (int i=1; i<n; ++i) {
    int p = order[i];
    x[p] = y[p] = -1;
    foreach (it, placed) {
      try_one(p, x[*it] + r[*it] + r[p], max(0LL, y[*it] - r[*it] + r[p]));
      try_one(p, max(0LL, x[*it] - r[*it] + r[p]), y[*it] + r[*it] + r[p]);
    }
    if (x[p] == -1) {
      return false;
    }
    placed.push_back(p);
  }
  return true;
}

int main() {
  cin.sync_with_stdio(0);

  int T;
  cin >> T;
  for (int tt=1; tt<=T; ++tt) {
    cin >> n >> W >> L;
    for (int i=0; i<n; ++i) {
      cin >> r[i];
    }

    static int order[1005];
    bool done = false;
    int iter;
    for (iter=0; iter<50; ++iter) {
      if (iter == 0) {
        for (int i=0; i<n; ++i) {
          order[i] = i;
        }
      } else if (iter == 1) {
        sort(order, order+n, sortmax);
      } else if (iter == 2) {
        sort(order, order+n, sortmin);
      } else {
        random_shuffle(order, order+n);
      }

      if (trysolve(order)) {
        printf("Case #%d:", tt);
        for (int i=0; i<n; ++i) {
          printf(" %lld %lld", x[i], y[i]);
        }
        printf("\n");
        done = true;
        break;
      }
    }

    if (!done) {
      abort();
    }

    if (iter > 0) {
      fprintf(stderr, "success after %d retries\n", iter);
    }
  }  
  
  return 0;
}
