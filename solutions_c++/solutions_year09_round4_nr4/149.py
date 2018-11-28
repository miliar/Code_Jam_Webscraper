#include <stdio.h>
#include <cstring>
#include <cmath>
#define max(a,b) ((a>b)?a:b)
#define min(a,b) ((a<b)?a:b)

int x[100], yy[100], r[100];
int a[100], c[3];
int x1, yy1, x2, yy2, r1, r2, n;
double ans;

double dist(int x1, int yy1, int x2, int yy2)
{
    return sqrt((x1 - x2) * (x1 - x2) + (yy1 - yy2) * (yy1 - yy2));
}

void solve()
{
    if(n == 1) ans = r[0];
    else if(n == 2) ans = max(r[0], r[1]);
    else
    {
        double ans1, ans2;
        for(a[0]=1; a[0]<=2; ++a[0])
        for(a[1]=1; a[1]<=2; ++a[1])
        for(a[2]=1; a[2]<=2; ++a[2])
        {
            if(a[0] == 1 && a[1] == 1 && a[2] == 1) continue;
            if(a[0] == 2 && a[1] == 2 && a[2] == 2) continue;

            memset(c, 0, sizeof c);
            c[a[0]]++; c[a[1]]++; c[a[2]]++;

            if(c[1] == 2)
            {
                x1 = yy1 = x2 = yy2 = r1 = r2 = -1;
                for(int i=0; i<n; ++i)
                {
                    if(a[i] == 1)
                    {
                        if(x1 == -1){ x1 = x[i], yy1 = yy[i], r1 = r[i];}
                        else{ x2 = x[i], yy2 = yy[i], r2 = r[i];}
                    }
                    else ans2 = r[i];
                }
                ans1 = (r1 + r2 + dist(x1, yy1, x2, yy2)) / 2.0;

                ans = min(ans,max(ans1, ans2));
            }
            else
            {
                x1 = yy1 = x2 = yy2 = r1 = r2 = -1;
                for(int i=0; i<n; ++i)
                {
                    if(a[i] == 2)
                    {
                        if(x1 == -1){ x1 = x[i], yy1 = yy[i], r1 = r[i];}
                        else{ x2 = x[i], yy2 = yy[i], r2 = r[i];}
                    }
                    else ans2 = r[i];
                }
                ans1 = (r1 + r2 + dist(x1, yy1, x2, yy2)) / 2.0;

                ans = min(ans, max(ans1, ans2));
            }
        }
    }
}

int main()
{
    int t, tc = 0;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d", &n);
        for(int i=0; i<n; ++i) scanf("%d%d%d", &x[i], &yy[i], &r[i]);
        ans = 1e20;
        solve();
        printf("Case #%d: %.10lf\n", ++tc, ans);
    }
    return 0;
}

