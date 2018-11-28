#include <iostream>
#include<cstdio>

using namespace std;
const int maxn=1100;
char ch[1000][1000];
double wp[maxn],owp[maxn],oowp[maxn],ip[maxn];
int xx[maxn],yy[maxn];
int main()
{
    int i,j,k,n,m,x,y,t,l,z;
    double dx,dy;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for(l=1;l<=t;l++)
    {
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%s",ch[i]);
        }
        for(i=0;i<n;i++)
        {
            xx[i]=yy[i]=0;
            for(j=0;j<n;j++)
            {
                if(ch[i][j]=='0')xx[i]++;
                else if(ch[i][j]=='1')yy[i]++;
            }
            wp[i]=double(yy[i]*1.0)/(xx[i]+yy[i]);
        }
        for(i=0;i<n;i++)
        {
            dx=dy=0.0;
            z=0;
            for(j=0;j<n;j++)
            {
                if(ch[i][j]=='0'||ch[i][j]=='1')
                {
                    z++;
                    y=yy[j];
                    x=xx[j];
                    if(ch[j][i]=='1')y--;
                    else x--;
                    dx+=double(y*1.0/(x+y));
                }
            }
            owp[i]=dx/(z*1.0);
        }
        for(i=0;i<n;i++)
        {
            dx=dy=0.0;
            x=0;
            for(j=0;j<n;j++)
            {
                if(ch[i][j]=='0'||ch[i][j]=='1')
                {
                    x++;
                    dx+=owp[j];
                }
            }
            oowp[i]=dx/(x*1.0);
        }
        printf("Case #%d:\n",l);
        for(i=0;i<n;i++)
        {
            ip[i]= 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
            printf("%.10lf\n",ip[i]);
        }
    }
    return 0;
}
