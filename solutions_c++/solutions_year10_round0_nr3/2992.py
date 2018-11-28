#include<cstdio>

int main() {
   int T;
   scanf("%d", &T);
   for (int i = 1; i <= T; ++i) {
      int N, k, R;
      scanf("%d%d%d", &R, &k, &N);
      int G[1002];
      int ind = 0;
      
      for (int g = 0; g < N; g++) {
         scanf("%d", G+g);
      }

      int Total = 0;
      for (int ride = 0; ride < R; ++ride) {
         int ind_r = ind; 
         int s = 0;
         bool not_started = true;
         while (s + G[(ind_r)] <= k && (ind_r != ind || ind_r == ind && not_started)) {
            not_started = false;
            s += G[(ind_r)];
            ind_r++;
            ind_r %= N;
         }
         ind = ind_r;

         Total += s;
      } 
      printf("Case #%d: %d\n", i, Total);
   }

   return 0;
}
