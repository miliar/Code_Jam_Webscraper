#include <cassert>
#include <stdio.h>
#include <vector>
using namespace std;
#define FOR(q,n) for(int q=0; q<n; q++)

#define MAX 4000
int vyska[MAX];
int next[MAX];
int ok;
int n;
vector<int> prev[MAX];

int check_chain() {
  FOR(current, n-1) { 
    int dalsi = next[current];
    for (int i = current; i < dalsi; i++) {
      if (next[i] > dalsi) {
        return 0;
      };
    }
    prev[dalsi].push_back(current);
  }
  return 1;
}

void assign_vysky(int pos, int slope) {
  FOR(q, prev[pos].size()) {
    int p = prev[pos][q];
    vyska[p] = vyska[pos] - slope * (pos - p);
    assign_vysky(p, slope+1);
    slope++;
  }
}

void check() {
  FOR(current, n-1) {
    int dalsi = next[current];
    for (int i=current+1; i<dalsi; i++) {
      assert((vyska[dalsi] - vyska[current]) / 1.0 / (dalsi-current) <
             (vyska[dalsi] - vyska[i]) / 1.0 / (dalsi-i));
    }
    for (int i=dalsi+1; i<n; i++) {
      assert((vyska[dalsi] - vyska[current]) / 1.0 / (dalsi-current) >
             (vyska[dalsi] - vyska[i]) / 1.0 / (dalsi-i));

    }

  }
}

void solve(int _case) {
  scanf("%d", &n);
  FOR(q, n-1) {
    int x;
    scanf("%d", &x);
    next[q] = x - 1;
    vyska[q] = -1;
    prev[q].clear();
  }
  prev[n-1].clear();
  ok = check_chain();

  /*
  FOR(q, n) {
    printf("prev %d:", q);
    FOR(w, prev[q].size()) printf(" %d", prev[q][w]);
    printf("\n");
  }
  */

  if (ok) {
    vyska[n-1] = 99999999;
    assign_vysky(n-1, 0);
    check();
  }

  printf("Case #%d:", _case);
  if (ok) {
    FOR(q,n) {
      printf(" %d", vyska[q]);
    }
  } else {
    printf(" Impossible");
  }
  printf("\n");
}

int main() {
  int t;
  scanf("%d", &t);
  FOR(q, t) {
    solve(q+1);
  }
}
