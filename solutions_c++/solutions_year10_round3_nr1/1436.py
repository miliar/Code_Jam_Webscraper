#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;
#define For(i, x) for (int i=0; i<(int)(x); i++)

typedef vector<int> vi;

int calc(vi& as, vi& bs) {
  int n = as.size();
  int ans = 0;
  For(i, n) For(j, n) {
    if (i < j) {
      if (as[i] < as[j] && bs[i] > bs[j]) ans++;
      if (as[i] > as[j] && bs[i] < bs[j]) ans++;
    }
  }
  return ans;
}

int main() {
  int ncases;
  scanf("%d", &ncases);
  For(cc, ncases) {
    int n;
    scanf("%d", &n);
    vi as(n), bs(n);
    For(i, n) scanf("%d %d", &as[i], &bs[i]);

    printf("Case #%d: %d\n", cc+1, calc(as, bs));
  }
}
