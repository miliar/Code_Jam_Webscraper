#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int map[105][105];
    char tmp;
    int sum[105][2];
    double a[105];
    double b[105];
    double c[105];
    int t, n, u, i, j;
    double sum1;
    int tot;
    scanf("%d", &t);
    for(u = 1; u <= t; u++)
    {
        scanf("%d", &n);
        memset(sum,0,sizeof(sum));
        for(i = 1; i <= n; i++)
        {
            for(j = 1; j <= n; j++)
            {
                cin >> tmp;
                if(tmp == '.') map[i][j] = 2;
                else map[i][j] = tmp - '0';
                if(map[i][j] == 0) sum[i][0]++;
                else if(map[i][j] == 1) sum[i][1]++;
            }
            a[i] = sum[i][1] * 1.0 / (sum[i][1] + sum[i][0]);
        }
        for(i = 1; i <= n; i++)
        {
            sum1 = 0;
            tot = 0;
            for(j = 1; j <= n; j++)
            {
                if(map[i][j] != 2)
                {
                    tot++;
                    sum[j][1-map[i][j]]--;
                    sum1 += sum[j][1] * 1.0 / (sum[j][1] + sum[j][0]);
                    sum[j][1-map[i][j]]++;
                }
            }
            b[i] = sum1 / tot;
        }
        for(i = 1;i <= n; i++)
        {
            sum1 = 0;
            tot = 0;
            for(j = 1; j <= n; j++)
            {
                if(map[i][j] != 2)
                {
                    sum1 += b[j];
                    tot ++;
                }
            }
            c[i] = sum1 / tot;
        }
        printf("Case #%d:\n",u);
        for(i = 1; i <= n; i++)
            printf("%lf\n",0.25 * a[i] + 0.50 * b[i] + 0.25 * c[i]);
    }
    return 0;
}
