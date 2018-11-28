#include<iostream>
#include<string>
#include<cmath>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
using namespace std;

char s[128][128];
int wins[128], totals[128];
double wp[128], owp[128], oowp[128];

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    
    int T, tt, n, win, total, i, j, cnt;
    double sum;
    
    scanf("%d", &T);
    for(tt = 1; tt <= T; tt++)
    {
        printf("Case #%d:\n", tt);
        scanf("%d", &n);
        for(i = 0; i < n; i++) scanf("%s", &s[i]);
        for(i = 0; i < n; i++)
        {
            totals[i] = 0;
            wins[i] = 0;
            for(j = 0; j < n; j++)
                if(s[i][j] != '.')
                {
                    totals[i]++;
                    if(s[i][j] == '1') wins[i]++;
                }
            wp[i] = (double)wins[i] / totals[i];
        }
        for(i = 0; i < n; i++)
        {
            sum = 0;
            cnt = 0;
            for(j = 0; j < n; j++)
                if(s[i][j] != '.')
                {
                    cnt++;
                    if(s[i][j] == '1') sum += (double)wins[j] / (totals[j] - 1);
                    else sum += (double)(wins[j] - 1) / (totals[j] - 1);
                }
            owp[i] = sum / cnt;
        }
        for(i = 0; i < n; i++)
        {
            sum = 0;
            cnt = 0;
            for(j = 0; j < n; j++)
                if(s[i][j] != '.')
                {
                    cnt++;
                    sum += owp[j];
                }
            oowp[i] = sum / cnt;
        }
        for(i = 0; i < n; i++) printf("%.8lf\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
    }
    
    return 0;
}
