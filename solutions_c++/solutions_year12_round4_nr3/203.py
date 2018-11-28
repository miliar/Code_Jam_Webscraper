#include <stdio.h>
#include <stdlib.h>
#include <math.h>

const int MAXN = 2010;

int p[MAXN], n;
long long h[MAXN];

void init()
{
     scanf("%d", &n);
     for (int i = 1; i < n; ++i)
         scanf("%d", &p[i]);          
}

void height(int s, int t, int sight, long long dx, long long dy)
{
     int first;
     for (first = s; first <= t; ++first)
         if (p[first] == sight) break;
     int last = s;
     for (int i = s; i <= t; ++i)
         if (p[i] == sight){
            long long  ddx = sight - i;
            long long  ddy = (long long)ceil((double)ddx * (double)dy / (double)dx - (1e-7)) + 1;
            dx = ddx;
            dy = ddy;
            h[i] = h[sight] - ddy;
            if (last < i) height(last, i-1, i, sight - i, ddy);
            last = i+1;
         }
     
}
     
void work()
{
     for (int i = 1; i < n; ++i)
         for (int j = i + 1; j < n; ++j)
             if (p[i] > j && p[i] < p[j]) {
                      printf("Impossible\n");
                      return;
             }
     h[n] = 0;
     height(1, n-1, n, 1, 0);
     long long min = h[1];
     for (int i = 1; i <=n ; ++i)
         if (min > h[i]) min = h[i];
     for (int i = 1; i <= n; ++i)
         h[i] -= min;  
     for (int i = 1; i <= n; ++i)
         printf("%lld ", h[i]);
     printf("\n");
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
