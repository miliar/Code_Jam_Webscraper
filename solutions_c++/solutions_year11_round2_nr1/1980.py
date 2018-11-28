#include<iostream>
#include<cstdio>

using namespace std;
int main()
{
    int t;
    char N[100][100];
    double wp[100], owp[100], oowp[100];
    int cnt[100], tmatch[100];
    scanf("%d", &t);
    for(int k = 1;k<=t;k++)
    {
        int n, i, j;

        scanf("%d", &n);
        for(i=0;i<n;i++)
            scanf("%s", N[i]);

        for(i=0;i<n;i++)
        {
            cnt[i] = 0;
            tmatch[i] = 0;
            for(j=0;j<n;j++)
            {
                if(N[i][j] == '1')
                    cnt[i]++;

                if(N[i][j] == '0' || N[i][j] == '1')
                    tmatch[i] ++;
            }
            wp[i] = (double)cnt[i] / tmatch[i];
        }

        double sum, x, c;
        for(i=0;i<n;i++)
        {
            sum = 0;
            c = 0;
            for(j=0;j<n;j++)
            {
                if(i == j || N[i][j] == '.')
                    continue;
                c++;
                if(N[j][i] == '1')
                    x = cnt[j]-1;
                else
                    x = cnt[j];

                sum += (double)x / (tmatch[j] - 1);
            }
            owp[i] = (double)sum/c;
        }
        for(i=0;i<n;i++)
        {
            sum = 0;
            c = 0;
            for(j=0;j<n;j++)
            {
                if(i == j || N[i][j] == '.')
                    continue;
                c++;
                sum += owp[j];
            }
            oowp[i] = (double)sum/c;
        }

        printf("Case #%d:\n", k);

        for(i = 0;i<n;i++)
            printf("%f\n",(0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]));
    }
    return 0;
}
