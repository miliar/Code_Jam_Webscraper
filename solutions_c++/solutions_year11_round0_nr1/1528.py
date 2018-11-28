#include <stdio.h>
#include <stdlib.h>

const int MAXN = 200;

int n;
int po[MAXN];
char ch[MAXN];

void work()
{
     int o, b, on, bn, time;
     
     scanf("%d", &n);
     for (int i = 0; i < n; ++i){
         while (scanf("%c", &ch[i]), ch[i]!='O' && ch[i]!='B');
         scanf("%d", &po[i]);        
     }
     o = 1; b = 1;
     time = 0;
     for (int i = 0; i < n; ++i){
         on = -1;
         bn = -1;
         for (int j = i; j < n; ++j){
             if (on == -1 && ch[j]=='O') on = j;    
             if (bn == -1 && ch[j]=='B') bn = j;
         }
         if (on==i){
            time += abs(po[i] - o) + 1;
            if (bn != -1)
               if (abs(po[bn] - b) <= abs(po[i] - o) + 1)
                  b = po[bn];
               else
                  b += (abs(po[i] - o) + 1) * ((po[bn] - b)/abs(po[bn] - b));
            o = po[i];                                       
         }
         else
         {
            time += abs(po[i] - b) + 1;
            if (on != -1)
               if (abs(po[on] - o) <= abs(po[i] - b) + 1)
                  o = po[on];
               else
                  o += (abs(po[i] - b) + 1) * ((po[on] - o)/abs(po[on] - o));
            b = po[i];                                      
         }
     }
     printf("%d\n", time);
     
}
     
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int cases, t = 0;
    scanf("%d", &cases);
    while (cases--){
          ++t;
          printf("Case #%d: ", t);
          work();      
    }
    return 0;
}
 