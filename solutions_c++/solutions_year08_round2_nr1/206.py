#include <stdio.h>
#include <map>
using namespace std;

long long all1[100000][3][3];
long long all2[100000][3][3];

struct point
{
       int x, y;
       point(){}
       point(int _x, int _y):x(_x), y(_y){}
       bool operator<(point p) const
       {
            if (x != p.x) return x < p.x;
            return y < p.y;
       }
       bool operator==(point p)
       {
            return x == p.x && y == p.y;
       }
} P[100000];

int main()
{
    int Q;
    scanf("%d", &Q);
    
    for (int q = 0; q < Q; q++)
    {
        printf("Case #%d: ", q + 1);
        int n, x0, y0, A, B, C, D, M;
        scanf("%d%d%d%d%d%d%d%d", &n, &A, &B, &C, &D, &x0, &y0, &M);
        
        P[0] = point(x0, y0);
        for (int i = 1; i < n; i++)
         x0 = ((long long)A*x0 + B)%M,
         y0 = ((long long)C*y0 + D)%M,
         P[i] = point(x0, y0);
        for (int i = 0; i < n; i++) P[i].x %= 3, P[i].y %= 3;
        
        memset(all1, 0, sizeof(all1));
        memset(all2, 0, sizeof(all2));
        
        all1[0][ P[0].x ][ P[0].y ] = 1;
        
        //for (int i = 0; i < n; i++) printf("%d %d\n", P[i].x, P[i].y);
        
        for (int i = 1; i < n; i++)
         for (int k1 = 0; k1 < 3; k1++)
          for (int k2 = 0; k2 < 3; k2++)
          {
              all1[i][k1][k2] = all1[i-1][k1][k2];
              if (k1 == P[i].x && k2 == P[i].y) all1[i][k1][k2]++;
          }
        
        for (int i = 1; i < n; i++)
        {
            for (int k1 = 0; k1 < 3; k1++)
             for (int k2 = 0; k2 < 3; k2++)
             {
                 all2[i][k1][k2] = all2[i-1][k1][k2];
                 all2[i][k1][k2] += all1[i-1][ (k1 - P[i].x + 3)%3 ][ (k2 - P[i].y + 3)%3 ];
             }
        }
        
        /*for (int i = 0; i < n; i++)
        {
            printf("%d:\n", i);
            for (int k1 = 0; k1 < 3; k1++)
             for (int k2 = 0; k2 < 3; k2++)
              printf("%d %d: %d\n", k1, k2, all2[i][k1][k2]);
        }*/
        long long ans = 0;
        for (int i = 1; i < n; i++)
         for (int k1 = 0; k1 < 3; k1++)
          for (int k2 = 0; k2 < 3; k2++)
          {
              if ( ((k1 + P[i].x)%3) == 0 && ((k2 + P[i].y)%3) == 0 ) ans += all2[i-1][k1][k2];
          }
        printf("%I64d\n", ans);
        
    }
    return 0;
}
