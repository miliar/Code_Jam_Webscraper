#include<cstdio>

int main() {
   int T;
   scanf("%d", &T);
   for (int i = 1; i <= T; ++i) { 
      int N, K;
      scanf("%d%d", &N, &K);
      int mod = (1 << N);
      K %= mod;
      if (K == mod-1) {
         printf("Case #%d: ON\n", i);
      } else {
         printf("Case #%d: OFF\n", i);
      }

   }
   return 0;
}
