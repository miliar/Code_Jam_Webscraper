#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

const int nmax = 1005;
int num[nmax];

int main(void) {
  freopen("C-large.in", "r", stdin);
  freopen("C-large.out.txt", "w", stdout);


  int nc;
  scanf("%d", &nc);

  for (int c = 1; c <= nc; ++c) {
    int n;
    scanf("%d", &n);

    int minVal = 1e9;
    int sum = 0;
    for (int i = 0; i < n; ++i) {
      scanf("%d\n", &num[i]);

      sum += num[i];
      minVal = min(minVal, num[i]);
    }

    int csum = 0;
    for (int i = 0; i < n; ++i) {
      int pw2 = 1;
      while (pw2 <= num[i]) {
        if (pw2 & num[i]) {
          csum ^= pw2;
        }
        pw2 *= 2;
      }
    }

    bool possible = (csum == 0);

    if (possible) {
      printf("Case #%d: %d\n", c, sum - minVal);
    } else {
      printf("Case #%d: NO\n", c);
    }
  }
}