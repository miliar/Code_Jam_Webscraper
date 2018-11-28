#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

const int MAXN = 10100;

int d[MAXN], l[MAXN], n, D;
int f[MAXN];

void init()
{
     scanf("%d", &n);
     for (int i = 0; i < n; ++i)
         scanf("%d%d", &d[i], &l[i]);              
     scanf("%d", &D);
}

int min(int a, int b)
{
    return a<b?a:b;    
}

void work()
{
     memset(f, 0xFF, sizeof(f));
     f[0] = d[0];
     for (int i = 0; i < n; ++i)
         for (int j = i+1; j < n; ++j)
             if (d[j] - d[i] <= f[i]){
                if (f[j] == -1 || f[j] < min(d[j] - d[i], l[j]))
                   f[j] = min(l[j], d[j] - d[i]);                      
             } else break;
     bool flag = false;
     for (int i = 0; i < n; ++i)
         if (D - d[i] <= f[i]){
               flag = true;
               break;
         }
     if (flag)
          printf("YES\n");
     else
          printf("NO\n");
}
          
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int cases;
    scanf("%d", &cases);
    for (int i = 1; i <= cases; ++i){
        printf("Case #%d: ", i);
        init();
        work();    
    }
    return 0;
}
