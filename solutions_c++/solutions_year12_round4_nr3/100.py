#include <cstdio>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;

typedef long long int64;
#define debug(x) cerr << #x << " = " << (x) << endl;

void verify(int n, const vector<int> &next) {
  for (int i=1; i<n; ++i) {
    if (next[i] <= i) {
      throw 1;
    }

    for (int j=i+1; j<n; ++j) {
      if (next[i] > j && next[j] > next[i]) {
        throw 1;
      }
    }
  }
}

int64 ceildiv(int64 a, int64 b) {
  return (a+b-1) / b;
}

int main() {
  cin.sync_with_stdio(0);

  int T;
  cin >> T;
  for (int tt=1; tt<=T; ++tt) {
    printf("Case #%d:", tt);
    try {
      int n;
      cin >> n;
      vector<int> next(n+1);
      for (int i=1; i<n; ++i) {
        cin >> next[i];
      }
      next[n] = n+1;

      verify(n, next);

      vector<int> h(n+1, -1);
      int MAX = 1000000000;

      queue<pair<int, int> > q;
      int pos = 1, last = 0;
      while (pos <= n) {
        h[pos] = MAX;
        q.push(make_pair(last+1, pos));
        last = pos;
        pos = next[pos];
      }

      while (!q.empty()) {
        int from = q.front().first, pos = q.front().second;
        q.pop();

        bool first = true;
        int64 knum=0, kdenom=0;
        for (int i=from; i<pos; ++i) {
          if (next[i] != pos) {
            continue;
          }

          q.push(make_pair(from, i));
          if (h[pos] == MAX) {
            h[i] = MAX-1;
          } else {
            int64 x1 = i, x2 = pos, x3 = next[pos];
            int64 y2 = h[x2], y3 = h[x3];

            if (first) {
              knum = y3-y2;
              kdenom = x3-x2;
            }

            int64 y1 = y2 - ceildiv(knum * (x2-x1), kdenom);

            if (!first && knum * (x2-x1) % kdenom == 0) {
              --y1;
            }
            if (y1 < 0) {
              throw 1;
            }
            h[x1] = y1;

            knum = y3-y1;
            kdenom = x3-x1;
            first = false;
          }
        }
      }

      for (int i=1; i<=n; ++i) {
        printf(" %d", h[i]);
      }
      printf("\n");
    } catch (int x) {
      puts(" Impossible");
    }
  }
  
  return 0;
}
