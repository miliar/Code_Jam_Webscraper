#include <stdio.h>
#include <stdlib.h>

int num_dancers;
int scores[120];
int values[120];
int s, p;

int count() {
   int i, j;
   int q;
   int m;
   int num_surprise = 0;
   int num_no_surprise = 0;
   for (i = 0; i < num_dancers; ++i) {
       if (scores[i] == 0) {
          if (0 >= p)
              ++num_no_surprise;
          continue;
       }
       else if (scores[i] == 1) {
            if (1 >= p)
                ++num_no_surprise;
            continue;
       }
       q = scores[i] / 3;
       m = scores[i] % 3;
       if (m == 0) {
           if (q >= p) {
               ++num_no_surprise;
               continue;
            }
           else if (q + 1 <= 10 && q + 1 >= p) {
                ++num_surprise;
                continue;
           }
       }
       else if (m == 1) {
            if (q + 1 <= 10 && q + 1 >= p) {
                ++num_no_surprise;
                continue;
            }
       }
       else if (m == 2) {
            if (q + 1 <= 10 && q + 1 >= p) {
                ++num_no_surprise;
                continue;
            }
            else if (q + 2 <= 10 && q + 2 >= p) {
                ++num_surprise;
                continue;
            }
       }
   }
   
   if (num_surprise > s)
       num_surprise = s;
   return num_no_surprise + num_surprise;
}

int main() {
    int n;
    int i, j;
    scanf("%d", &n);

    for (int n_case = 1; n_case <= n; ++n_case) {
        scanf("%d%d%d", &num_dancers, &s, &p);
        for (i = 0; i < num_dancers; ++i)
            scanf("%d", &scores[i]);
        int ans = count();

        printf("Case #%d: %d\n", n_case, ans);
    }
    return 0;
}
