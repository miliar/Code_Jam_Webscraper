#include	<cstdio>
#include	<cstring>
#include 	<algorithm>
#include    <iostream>
using namespace std;
const int N = 101;
char maps[N][N];
double w[N], cnt[N], ans[N];
double wp[N], owp[N], oowp[N];
double win(double a, double b)
{
    if(b == 0) return 0;
    return a / b;
}
int main ()
{
    int n, t;
    freopen("A-large.in", "r", stdin);
    freopen("ronaflx.out", "w", stdout);
    scanf("%d", &t);
    for(int k = 1;k <= t;k++)
    {
        scanf("%d", &n);
        for(int i = 0;i < n;i++)
            scanf("%s", maps[i]);
        memset(w, 0, sizeof(w));
        memset(cnt, 0, sizeof(cnt));
        memset(ans, 0, sizeof(ans));
        memset(wp, 0, sizeof(wp));
        memset(owp, 0, sizeof(owp));
        memset(oowp, 0, sizeof(oowp));
        for(int i = 0;i < n;i++)
        {
            for(int j = 0;j < n;j++)
            {
                if(maps[i][j] != '.') cnt[i]++;
                if(maps[i][j] == '1') w[i]++;
            }
            wp[i] = win(w[i], cnt[i]);
        }
        for(int i = 0;i < n;i++)
        {
            int c = 0;
            for(int j = 0;j < n;j++)
            {
                if(i == j) continue;
                if(maps[j][i] == '.') continue;
                if(maps[j][i] == '1') owp[i] += win(w[j] - 1, cnt[j] - 1);
                if(maps[j][i] == '0') owp[i] += win(w[j], cnt[j] - 1);
                c++;
            }
            owp[i] /= c;
        }
        for(int i = 0;i < n;i++)
        {
            int cnt = 0;
            for(int j = 0;j < n;j++)
                if(maps[i][j] != '.') oowp[i] += owp[j], cnt++;
            oowp[i] /= cnt;
        }
        printf("Case #%d:\n", k);
        for(int i = 0;i < n;i++)
        {
            printf("%0.8lf\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
        }
    }
    return 0;
}
