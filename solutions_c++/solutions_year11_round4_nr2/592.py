#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
int a[510][510];
int s[510][510];
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for(int ti = 1; ti <= tc; ti++)
    {
        int r, c, d;
        scanf("%d%d%d", &r, &c, &d);
        for(int i = 1; i <= r; i++)
        {
            char buf[510];
            scanf("%s", buf);
            for(int j = 1; j <= c; j++)
                a[i][j] = buf[j-1]-'0';
        }
        for(int i = 1; i <= r; i++)
        for(int j = 1; j <= c; j++)
            s[i][j] = a[i][j] + s[i-1][j] + s[i][j-1] - s[i-1][j-1];


        int m = max(c,r);
        int val = 0;
        for(int i = 1; i <= r; i++)
        for(int j = 1; j <= c; j++)
        {
            double s0x = 0, s0y = 0, s1x = 0, s1y = 0;
            for(int k = 3; k <= m; k++)
            {
                int k2 = k/2;
                if(k%2==0)
                {
                    if(i-k2+1 < 1 || i+k2 > r || j-k2+1 < 1 || j+k2 > c)break;
                    s0x += a[i-k2+2][j-k2+2]*(i-k2+2-(i+0.5));
                    s0y += a[i-k2+2][j-k2+2]*(j-k2+2-(j+0.5));
                    s0x += a[i-k2+2][j+k2-1]*(i-k2+2-(i+0.5));
                    s0y += a[i-k2+2][j+k2-1]*(j+k2-1-(j+0.5));
                    s0x += a[i+k2-1][j-k2+2]*(i+k2-1-(i+0.5));
                    s0y += a[i+k2-1][j-k2+2]*(j-k2+2-(j+0.5));
                    s0x += a[i+k2-1][j+k2-1]*(i+k2-1-(i+0.5));
                    s0y += a[i+k2-1][j+k2-1]*(j+k2-1-(j+0.5));
                    for(int y = j-k2+2; y <= j+k2-1; y++)
                    {
                        s0x += a[i-k2+1][y]*(i-k2+1-(i+0.5));
                        s0y += a[i-k2+1][y]*(y-(j+0.5));
                        s0x += a[i+k2][y]*(i+k2-(i+0.5));
                        s0y += a[i+k2][y]*(y-(j+0.5));
                    }
                    for(int x = i-k2+2; x <= i+k2-1; x++)
                    {
                        s0x += a[x][j-k2+1]*(x-(i+0.5));
                        s0y += a[x][j-k2+1]*(j-k2+1-(j+0.5));
                        s0x += a[x][j+k2]*(x-(i+0.5));
                        s0y += a[x][j+k2]*(j+k2-(j+0.5));
                    }

                    if(fabs(s0x) < 0.05 && fabs(s0y) < 0.05 && val < k)
                    {
                        val = k;
                    }
                }
                else
                {
                    if(i-k2 < 1 || i+k2 > r || j-k2 < 1 || j+k2 > c)break;
                    s1x += a[i-k2+1][j-k2+1]*(i-k2+1-(i));
                    s1y += a[i-k2+1][j-k2+1]*(j-k2+1-(j));
                    s1x += a[i-k2+1][j+k2-1]*(i-k2+1-(i));
                    s1y += a[i-k2+1][j+k2-1]*(j+k2-1-(j));
                    s1x += a[i+k2-1][j-k2+1]*(i+k2-1-(i));
                    s1y += a[i+k2-1][j-k2+1]*(j-k2+1-(j));
                    s1x += a[i+k2-1][j+k2-1]*(i+k2-1-(i));
                    s1y += a[i+k2-1][j+k2-1]*(j+k2-1-(j));
                    for(int y = j-k2+1; y <= j+k2-1; y++)
                    {
                        s1x += a[i-k2][y]*(i-k2-(i));
                        s1y += a[i-k2][y]*(y-(j));
                        s1x += a[i+k2][y]*(i+k2-(i));
                        s1y += a[i+k2][y]*(y-(j));
                    }
                    for(int x = i-k2+1; x <= i+k2-1; x++)
                    {
                        s1x += a[x][j-k2]*(x-(i));
                        s1y += a[x][j-k2]*(j-k2-(j));
                        s1x += a[x][j+k2]*(x-(i));
                        s1y += a[x][j+k2]*(j+k2-(j));
                    }

                    if(fabs(s1x) < 0.05 && fabs(s1y) < 0.05 && val < k)
                    {
                        val = k;
                    }
                }
            }
        }
        printf("Case #%d: ", ti);
        if(val == 0)printf("IMPOSSIBLE\n");
        else printf("%d\n", val);
    }
}
