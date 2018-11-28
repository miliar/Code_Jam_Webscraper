/*
TASK: RPI
LANG: C++
*/
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;
int N,M,T;
double WP[127],OWP[127],OOWP[127];
char tb[127][127];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,j,k,tt=0;
    scanf("%d",&T);
    while(T--)
    {
        tt++;
        scanf("%d",&N);
        for(i=0;i<N;i++)
            scanf("%s",tb[i]);
        int x,y,z;
        for(i=0;i<N;i++)
        {
            x=0;    y=0;
            for(j=0;j<N;j++)
            {
                if(tb[i][j]=='.')
                    continue;
                y++;
                if(tb[i][j]=='1')
                    x++;
            }
            WP[i]=(double)x/y;
        }
        // OWP
        for(k=0;k<N;k++)
        {
            z=0;
            for(i=0;i<N;i++)
            {
                if(i==k || tb[k][i]=='.')    continue;
                x=0;    y=0;    z++;
                for(j=0;j<N;j++)
                {
                    if(tb[i][j]=='.' || j==k)
                        continue;
                    y++;
                    if(tb[i][j]=='1')
                        x++;
                }
                OWP[k]+=((double)x/y);
            }
            OWP[k]/=z;
        }
/*
        for(i=0;i<N;i++)
            printf("%lf\n",OWP[i]);
//*/
        // OOWP
        for(i=0;i<N;i++)
        {
            y=0;
            for(j=0;j<N;j++)
            {
                if(tb[i][j]=='.')
                    continue;
                y++;
                OOWP[i]+=OWP[j];
            }
            OOWP[i]/=y;
        }
/*
        for(i=0;i<N;i++)
            printf("%lf\n",OOWP[i]);
//*/
        printf("Case #%d:\n",tt);
        for(i=0;i<N;i++)
            printf("%lf\n",0.25*WP[i]+0.50*OWP[i]+0.25*OOWP[i]);
        for(i=0;i<N;i++)
        {
            WP[i]=0;
            OWP[i]=0;
            OOWP[i]=0;
        }
    }
}
