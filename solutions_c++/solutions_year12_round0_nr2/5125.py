#include <stdio.h>
#include <stdlib.h>

const int MAXN = 10;

int n, s, p, t[MAXN];

void init()
{
     scanf("%d%d%d", &n, &s, &p);
     for (int i = 0; i < n; ++i)
         scanf("%d", &t[i]);
}

int can(int t, int p, bool s)
{
    int st = t/3;
    if (t%3 == 0){
       if (s) {
              if (t == 0) st = -1000; else 
              st++;     
       }
    }
    else
    if (t%3 == 1){
       if (s) {
              if (t == 1) st = -1000; else st++;
       }
       else
       st++;        
    }
    else
    {
        if (s) st+=2; else st++;
    }
    if (st >= p) return 1; else return 0;
}

void work()
{
     int best = 0;
     for (int i = 0; i < (1<<n); ++i){
         int ss = 0;
         for (int j = 0; j < n; ++j)
             if ((i & ( 1<< j))!=0) ss++;
         if (ss!=s) continue;
         int now = 0;
         for (int j = 0; j < n; ++j)
             if ((i & (1<<j))!=0)
                now += can(t[j], p, true);
             else
                now += can(t[j], p, false);
         if (best < now) best = now;               
                
                
     }     
     printf("%d\n", best);
}
          
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int ca;
    scanf("%d", &ca);
    for (int i =1; i <= ca; ++i){
        printf("Case #%d: ", i);
        init();
        work();
    }
        
    return 0;
}
