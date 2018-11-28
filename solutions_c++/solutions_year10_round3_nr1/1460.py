#include <stdio.h>
#define MAX 55

int intersect(int a[], int b[], int N) {
   int cnt = 0;
   int j, k;
   for (j = 0; j < N-1; j++) {
      for (k = j+1;  k < N; k++) {
         if ((b[j] > b[k])) {
            cnt++;
         } 
      }
   }
   return cnt;
}

int main()
{
   int kases;
   int j, k, l;
   scanf("%d", &kases);
   int N; //wires
   for (int i = 1; i <= kases; i++) {
      int a[MAX] = {0}, b[MAX] = {0};
      scanf("%d", &N);
      for (j = 0; j < N; j++) {
         scanf("%d %d", &a[j], &b[j]);
      }
      
      int swap;
      // sort
      for (j = 0; j < N-1; j++) {
         for (k = (N-2)-j; k >= 0; k--) {
            if (a[k] > a[k+1]) {
               swap = a[k];
               a[k] = a[k+1];
               a[k+1] = swap;

               swap = b[k];
               b[k] = b[k+1];
               b[k+1] = swap;
            }
         }
      }
 #if 0
      for (j = 0; j < N; j++) {
         printf("%d %d\n", a[j], b[j]);
      }
#endif
      int cnt = intersect(a,b, N);
      printf("Case #%d: %d\n", i, cnt);
   }
   return 0;
}
