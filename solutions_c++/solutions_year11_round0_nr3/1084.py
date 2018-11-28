#include <cstdio>

#define maxn 1010

int T;
int n;
int a[maxn];


int main() {
  scanf("%d", &T);
  for (int q = 1; q <= T; q++) {
    scanf("%d", &n);

    int sum = 0;
    int rsum = 0;
    int mn = 100000000;
    for (int i = 0; i < n; i++) {
      scanf("%d", &a[i]);
      sum ^= a[i];
      rsum += a[i];
      if (a[i] < mn) mn = a[i];
    }

    if (sum != 0) {
      printf("Case #%d: NO\n", q);
    } else {
      printf("Case #%d: %d\n", q, rsum - mn);
    }

    
  }
}