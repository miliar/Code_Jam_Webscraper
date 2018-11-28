#include <cstdio>
#include <cstring>
#include <fstream>
using namespace std;

const int N = 105;
double wp[N], owp[N], oowp[N];
int sum[N], one[N];
char s[N][N];
int t, n;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);

    scanf("%d", &t);
    for (int k = 1; k <= t; k++)
    {
        scanf("%d", &n);
        memset(sum, 0, sizeof(sum));
        memset(one, 0, sizeof(one));
        for (int i = 0; i < n; i++)
            wp[i] = owp[i] = oowp[i] = 0;

        for (int i = 0; i < n; i++)
        {
            getchar();
            for (int j = 0; j < n; j++)
            {
                scanf("%c", &s[i][j]);
                if (s[i][j] != '.') sum[i]++;
                if (s[i][j] == '1') one[i]++;
            }
        }
        for (int i = 0; i < n; i++)
            wp[i] = one[i] * 1.0 / sum[i];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
            {
                if (s[i][j] == '1')
                    owp[j] += (one[i]-1)*1.0 / ((sum[i]-1)*1.0) / (sum[j]*1.0);
                if (s[i][j] == '0')
                    owp[j] += one[i]*1.0 / ((sum[i]-1)*1.0) / (sum[j]*1.0);
            }
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (s[i][j] != '.')
                    oowp[i] += owp[j] / (sum[i]*1.0);
        printf("Case #%d:\n", k);
        for (int i = 0; i < n; i++)
            printf("%f\n", 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]);
    }
}
