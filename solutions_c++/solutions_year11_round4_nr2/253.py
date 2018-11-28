#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

int T, R, C, D;
int g[500][500];


bool check(int k)
{
     double x2, y2, cx, cy, x, y;
     
     for (int x1 = 0; x1 <= R - k; x1++)
         for (int y1 = 0; y1 <= C - k; y1++)
         {
             x2 = x1 + k - 1;
             y2 = y1 + k - 1; 
             cx = 1.0 * (x1 + x2) / 2;
             cy = 1.0 * (y1 + y2) / 2;
             x = y = 0;
             for (int i = x1; i <= x2; i++)
                 for (int j = y1; j <= y2; j++)
                 {
                     if (i == x1 && (j == y1 || j == y2)) continue;
                     if (i == x2 && (j == y1 || j == y2)) continue;
                     x += (i - cx) * g[i][j];
                     y += (j - cy) * g[i][j];
                 }
             if (x == 0 && y == 0) return true;
         }
     return false;
}                 

int main()
{
    char ch;
    int ed, ans;
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        printf("Case #%d: ", cas);
        scanf("%d%d%d", &R, &C, &D);
        for (int i = 0; i < R; i++)
        {
            scanf("%c", &ch);
            for (int j = 0; j < C; j++)
            {
                scanf("%c", &ch);
                g[i][j] = (int)(ch - '0');
            }
        }
        ed = min(R, C);
        ans = -1;
        for (int i = 3; i <= ed; i++)
            if (check(i)) ans = i;
        if (ans == -1) printf("IMPOSSIBLE\n");
        else printf("%d\n", ans);
    }
    return 0;
}
