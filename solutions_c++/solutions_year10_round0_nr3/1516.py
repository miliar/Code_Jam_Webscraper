#include <stdio.h>
#include <stdlib.h>

int g[1000];
long long sum[1000];
int next[1000];
long long starting[1000];
int startind[1000];

int main() {
  int t, r, k, n, i, j, m, c;
  long long total, s;
  scanf("%d", &t);
  for (i = 0; i < t; i++) {
    scanf("%d%d%d", &r, &k, &n);
    s = 0;
    for (j = 0; j < n; j++) {
      scanf("%d", &g[j]);
      s += g[j];
      starting[j] = -1;
    }
    if (s <= k) { // everyone will fit
      total = s * r;
    }
    else { // someone won't fit
      s = 0;
      j = 0;
      for (m = 0; m < n; m++) {
        if (s + g[m] <= k) {
          s += g[m];
        }
        else
          break;
      }
      
      sum[0] = s;
      next[0] = m;
      s -= g[0];
      for (j = 1; j < n; j++) {
        while (s + g[m] <= k) {
          s += g[m++];
          if (m == n)
            m = 0;
        }
        sum[j] = s;
        next[j] = m;
        s-= g[j];
      }
      
      j = 0;
      total = 0;
      c = 0;
      do {
        starting[j] = total;
        startind[j] = c;
        total += sum[j];        
        j = next[j];
        c++;
      } while (starting[j] == -1 && c < r);
      if (c < r) {
        long long cycleAmt = total - starting[j];
        int cycleLen = c - startind[j];
        while (c + cycleLen < r) {
          total += cycleAmt;
          c += cycleLen;
        }
        while (c < r) {
          total += sum[j];        
          j = next[j];
          c++;
        }
      }
    }
    printf("Case #%d: %lld\n", i + 1, total);
  }
  return 0;
}