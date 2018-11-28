#include <cstdio>
#include <iostream>
using namespace std;

char grid[103][103];
double wp[103], owp[103], oowp[103], rpi[103];
int totg[103];

int main()
{
    freopen("A-large.in", "rt", stdin);
    freopen("out.txt", "wt", stdout);
    int T, N;
    cin>>T;
    for (int cas=1; cas<=T; ++cas)
    {
        cin>>N;
        for (int i=0; i<N; ++i)
        {
            cin>>grid[i];
            wp[i] = 0.0;
            int tg = 0;
            for (int j=0; j<N; ++j)
            {
                if (grid[i][j]=='0') ++tg;
                else if (grid[i][j]=='1') ++tg, wp[i] += 1.0;
            }
            totg[i] = tg;
            if (tg) wp[i] /= tg;
        }
        for (int i=0; i<N; ++i)
        {
            owp[i] = 0.0;
            int tg = 0;
            for (int j=0; j<N; ++j)
            {
                if (grid[i][j]=='1') ++tg, owp[i] += wp[j]*totg[j]/(totg[j]-1);
                else if (grid[i][j]=='0') ++tg, owp[i] += (wp[j]*totg[j]-1.0)/(totg[j]-1);
            }
            if (tg) owp[i] /= tg;
        }
        for (int i=0; i<N; ++i)
        {
            oowp[i] = 0.0;
            int tg = 0;
            for (int j=0; j<N; ++j)
            {
                if (grid[i][j]!='.') ++tg, oowp[i] += owp[j];
            }
            if (tg) oowp[i] /= tg;
        }
        printf("Case #%d:\n", cas);
        for (int i=0; i<N; ++i)
        {
            rpi[i] = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
            printf("%.7lf\n", rpi[i]);
        }
    }
    return 0;
}
