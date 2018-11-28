#include <stdio.h>

int stat;
int cal(int j, int k) {
   if (k >= 2*j)
      return stat+1;
   if (k <= j+1) 
      return stat;
   else {
      stat++;
      return (cal(k%j, j));
   }
}

int main(void) {
   int kases;
   int a1, a2, b1, b2;
   int win;
   scanf("%d", &kases);
   for (int i = 1; i <= kases; i++) {
      win = 0;
      scanf("%d %d %d %d", &a1, &a2, &b1, &b2);
      int j = a1, k = b1;
//      printf("a1 = %d, a2 = %d, b1 = %d, b2 = %d\n", j, a2, k, b2);
      int min, max;
      for (j = a1; j <= a2; j++) {
         for (k = b1; k <= b2; k++) {
            min = j;
            max = k;
            if (k < j) {
               min = k;
               max = j;
            }
//            printf("j = %d, k = %d\n", j,k);
            stat = 0;
            stat = cal(min, max);
            if (stat%2 != 0)
               win++;
         }
      }
      printf("Case #%d: %d\n", i, win);
   }
   return 0;
}
