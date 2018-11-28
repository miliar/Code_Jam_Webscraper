#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int n;
char g[120][120],win[120],tot[120];
double wp[120],owp[120],oowp[120];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    int t;
    scanf("%d",&t);
    for (int ft = 1;ft <= t;ft++)
    {
        scanf("%d",&n);
        for (int i = 0;i < n;i++)   scanf("%s",g[i]);
        memset(wp,0,sizeof(wp));
        memset(owp,0,sizeof(owp));
        memset(oowp,0,sizeof(oowp));
        for (int i = 0;i < n;i++)
        {
            win[i] = tot[i] = 0;
            for (int j = 0;j < n;j++)
                if (g[i][j] != '.')
                {
                    tot[i]++;
                    if (g[i][j] == '1') win[i]++;
                }
            wp[i] = (double)win[i]/(double)tot[i];
        }
        for (int i = 0;i < n;i++)
        {
            double sum = 0.0;
            for (int j = 0;j < n;j++)
                if (g[i][j] != '.')
                {
                    if (g[i][j] == '1')
                    {
                        if (tot[j]-1 != 0)
                            sum += (double)win[j]/(double)(tot[j]-1);
                    }
                    else
                    {
                        if (tot[j]-1 != 0)
                            sum += (double)(win[j]-1)/(double)(tot[j]-1);
                    }
                }
            owp[i] = sum/(double)tot[i];
        }
        for (int i = 0;i < n;i++)
        {
            double sum = 0;
            for (int j = 0;j < n;j++)
                if (g[i][j] != '.')
                    sum += owp[j];
            oowp[i] = sum/(double)tot[i];
        }
        //for (int i = 0;i < n;i++)
        //    cout << wp[i] << ' ' << owp[i] << ' ' << oowp[i] << endl;
        printf("Case #%d:\n",ft);
        for (int i = 0;i < n;i++)
            printf("%f\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
    }
}
