#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

char a[101][101];
double tmpwp[101],wp[101], owp[101], oowp[101];
int sum[101], wins[101];
int n;

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int tt;
    scanf("%d", &tt);
    for (int i = 0; i < tt; i++)
    {
        printf("Case #%d:\n", i + 1);
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
        //{
            for (int j = 0; j < n; j++)
             //   scanf("%c", &a[i][j]);
                cin >>a[i][j];
          //  scanf("\n");
        //}
        memset(wins, 0, sizeof(wins));
        memset(sum, 0, sizeof(sum));
        for (int i = 0; i < n; i++)
        {
           // int sum = 0;
            for (int j = 0; j < n; j++)
                if (a[i][j] != '.')
                {
                    sum[i]++;
                    if (a[i][j] == '1') wins[i]++;
                }
            wp[i] = (double)wins[i] / sum[i];
        }

        for (int i = 0; i < n; i++)
        {

            int opt = 0;
            double sumwp = 0;
            for (int j = 0; j < n; j++)
                if (a[i][j] != '.')
                {
                    opt ++;
                    double wpnow;
                    if (a[i][j] == '1') wpnow = (double)wins[j] / (sum[j] - 1);
                    else wpnow = (double)(wins[j] - 1) / (sum[j] - 1);
                    sumwp += wpnow;
                }
            owp[i] = (double)sumwp / opt;
        }

        for (int i = 0; i < n; i++)
        {
            int opt = 0;
            double sumowp = 0;
            for (int j = 0; j < n; j++)
                if (a[i][j] != '.')
                {
                    opt ++;
                    sumowp += owp[j];
                }
            oowp[i] = (double)sumowp / opt;
        }

        for (int i = 0; i < n; i++)
            cout << (double) (0.25 * wp[i]) + (0.50 * owp[i]) + (0.25 * oowp[i]) <<endl;
    }


    return 0;
}
