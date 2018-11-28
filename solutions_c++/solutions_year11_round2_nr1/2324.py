#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

double WP[200] , OWP[200] , OOWP[200] ;

char s[101][110];

int  mp[2][200] , cnt[200] , N;

bool g[101][101];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,j,k,ncase;scanf("%d",&ncase);
    for(int cas=1;cas<=ncase;++cas)
    {
        scanf("%d",&N);
        memset(mp,0,sizeof(mp));
        memset(cnt,0,sizeof(cnt));
        memset(g,0,sizeof(g));
        for(i=0;i<N;++i)
        {
            scanf("%s",s[i]);
            for(j=0;j<N;++j)
            {
                if(s[i][j]!='.')
                {
                    g[i][j] = 1;
                    mp[s[i][j]-'0'][i]++;
                    cnt[i]++;
                }
            }
        }
        for(i=0;i<N;++i)
        {
            if(cnt[i]!=0)WP[i] = (double)mp[1][i] / (double)cnt[i];
            else WP[i] = 0.0;
        }
        double t , total ,Total,T;
        for(i=0;i<N;++i)
        {
            t = total = 0.0;
            Total = T = 0.0;
            for(j=0;j<N;++j)if(i!=j && g[i][j])
            {
                total = WP[j] * cnt[j];
                t = cnt[j];
                if(s[j][i] == '1')
                {
                    total -= 1;
                    t-=1;
                }
                else if(s[j][i]=='0')
                {
                    t-=1;
                }
                Total += total / t;
                ++T;
            }
            if(fabs(t)<=1e-8)OWP[i]=0.0;
            else OWP[i] = Total / T;
        }



        for(i=0;i<N;++i)
        {
            t = total = 0 ;
            for(j=0;j<N;++j)if(i!=j && g[i][j])
            {

                    t = t + 1.0;
                    total += OWP[j];

            }
            if(fabs(t)<=1e-7)OOWP[i]=0.0;
            else OOWP[i] = total / t;
        }

        printf("Case #%d:\n",cas);



        for(i=0;i<N;++i)
        {
            printf("%.10lf\n",0.25*WP[i] + 0.50*OWP[i] + 0.25*OOWP[i]);
        }
    }
    return 0;
}

