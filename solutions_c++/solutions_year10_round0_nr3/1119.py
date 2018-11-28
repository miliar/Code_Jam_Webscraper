#include <stdio.h>
#define MAX 1002

int main()
{
   int i, j, k;
   int kases, max_ride, max_val, groups;
   long long group_sum, summ;
   long long tot_sum;
   int head;

   scanf("%d", &kases);

   for (i = 1; i <= kases; i++) {
 
      int g[MAX];
      group_sum = 0;
      tot_sum = 0;

      scanf("%d %d %d", &max_ride, &max_val, &groups);
      for (j = 0; j < groups; j++) {
         scanf("%d", &g[j]);
         group_sum += (long long)g[j];
      }
      if (group_sum <= max_val) {
         tot_sum = max_ride*group_sum;
      }
      else {
         head = 0;
         for (k = 1; k <= max_ride; k++) {
            summ = 0;
            j = head;
            while (true) {
               summ += (long long)g[j];
               if (summ > max_val) {
                  summ -= g[j];
                  head = j;
                  break;
               }
               if (j == (groups-1))
                  j = 0; 
               else j++;
            }
            tot_sum += (long long)summ;
         }
      }
      printf("Case #%d: %lld\n", i, tot_sum);
   }
   return 0;
}
