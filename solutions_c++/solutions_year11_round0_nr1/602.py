#include <stdio.h>
#include <stdlib.h>

char s[2];
int d[2][1000];
int id[2][1000];

int main () {
    int kase, i, n, v,h = 1;
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d", &kase);
    while (kase--) {
          scanf("%d", &n);
          int count1 = 0, count2 = 0;
          for (i = 0; i < n; ++i) {
              scanf("%s %d", &s, &v);
              if (s[0] == 'O') {
                 d[0][count1] = v;
                 id[0][count1++] = i;
              }
              else { 
                   d[1][count2] = v;
                   id[1][count2++] = i;
              }
          }
          int step1 = 1, step2 = 1, cur1 = 0, cur2 = 0;
          int ans = 0;
          while (count1 > cur1 && count2 > cur2) {
                ans++;
                if (step1 == d[0][cur1] && step2 == d[1][cur2]) {
                   if (id[0][cur1] > id[1][cur2]) {
                      cur2++;
                      if (step1 < d[0][cur1]) step1++;
                      if (step1 > d[0][cur1]) step1--;
                   }
                   else {
                        cur1++;
                        if (step2 < d[1][cur2]) step2++;
                        if (step2 > d[1][cur2]) step2--;
                   }
                   continue;
                }
                if (step1 == d[0][cur1] && id[0][cur1] < id[1][cur2]) {
                   cur1++;
                   if (step2 < d[1][cur2]) step2++;
                   if (step2 > d[1][cur2]) step2--;
                   continue;
                }
                if (step2 == d[1][cur2] && id[0][cur1] > id[1][cur2]) {
                   cur2++;
                   if (step1 < d[0][cur1]) step1++;
                   if (step1 > d[0][cur1]) step1--;
                   continue;
                }
                if (step1 < d[0][cur1]) step1++;
                if (step1 > d[0][cur1]) step1--;
                if (step2 < d[1][cur2]) step2++;
                if (step2 > d[1][cur2]) step2--;
          }
          while (count1 > cur1) {
                ans += abs(d[0][cur1]-step1)+1;
                step1 = d[0][cur1++];
          }
          while (count2 > cur2) {
                ans += abs(d[1][cur2]-step2)+1;
                step2 = d[1][cur2++];
          }
          printf("Case #%d: %d\n",h++, ans);
    }
    return 0;
}
