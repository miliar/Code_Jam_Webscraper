#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int map[105][105];
char tmp;
int sum[105][2];
double a[105];
double b[105];
double c[105];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("data1.txt", "w", stdout);
    int t, n, u, i, j;
    scanf("%d", &t);
    for(u = 1; u <= t; u++)
    {
        scanf("%d", &n);
        memset(sum, 0, sizeof(sum));
        for(i = 1; i <= n; i++)
        {
            for(j = 1; j <= n; j++)
            {
                cin >> tmp;
                if(tmp == '.')
                    map[i][j] = 2;
                else
                    map[i][j] = tmp - '0';
                if(map[i][j] == 0)
                    sum[i][0]++;
                else if(map[i][j] == 1)
                    sum[i][1]++;
            }
            a[i] = sum[i][1] * 1.0 / (sum[i][1] + sum[i][0]);
//            if(i == 2)
//            cout << sum[i][0] << "   " << sum[i][1] << "  " << a[i] << endl;
        }
        double sum1;
        int cnt;
        for(i = 1; i <= n; i++)
        {
            sum1 = 0;
            cnt = 0;
            for(j = 1; j <= n; j++)
            {
                if(map[i][j] != 2)
                {
                    sum[j][1-map[i][j]]--;
                    cnt++;
                    sum1 += sum[j][1] * 1.0 / (sum[j][1] + sum[j][0]);
                    sum[j][1-map[i][j]]++;
                }
            }
            b[i] = sum1 / cnt;
        }
        for(i = 1; i <= n; i++)
        {
            sum1 = 0;
            cnt = 0;
            for(j = 1; j <= n; j++)
            {
                if(map[i][j] != 2)
                {
                    sum1 += b[j];
                    cnt ++;
                }
            }
            c[i] = sum1 / cnt;
        }
        printf("Case #%d:\n", u);
//        cout << a[1] << "     " << a[1] << "    " << c[1] << "   " << endl;
//        cout << a[3] << "     " << endl;
        for(i = 1; i <= n; i++)
        {
            printf("%lf\n", 0.25 * a[i] + 0.50 * b[i] + 0.25 * c[i]);
        }
    }
    return 0;
}
