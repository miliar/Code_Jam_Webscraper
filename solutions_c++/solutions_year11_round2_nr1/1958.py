#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;

int n;
char m[105][105];
int map[105][105];
double f[105],owp[105],oowp[105];
double s[105],c[105];

int main()
{
    freopen("A-large(2).in","r",stdin);
    freopen("A-large(2).out","w",stdout);
    int t;
    int h=1;
    scanf("%d",&t);
    while(t--)
    {
        memset(s,0,sizeof(s));
        memset(c,0,sizeof(c));
        memset(map,0,sizeof(map));
        memset(owp,0,sizeof(owp));
        memset(oowp,0,sizeof(oowp));
        int i,j;
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%s",m[i]);
            for(j=0;j<n;j++)
            {
                if(m[i][j]!='.')
                {
                   map[i][j]=m[i][j]-'0';
                   c[i]+=map[i][j];
                   s[i]++;
                }
            }
            f[i]=(c[i]/s[i]*1.0)*0.25;
        }
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(m[i][j]!='.')
                {
                    owp[i]+=(c[j]-map[j][i])/(s[j]-1);
                }
            }
            owp[i]=owp[i]/s[i];
        }
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(m[i][j]!='.')
                {
                    oowp[i]+=(owp[j]);
                }
            }
            oowp[i]=(oowp[i]/s[i])*0.25;

        }
        printf("Case #%d:\n",h++);
        for(i=0;i<n;i++)
        {
            printf("%.12lf\n",f[i]+owp[i]*0.5+oowp[i]);
        }
    }
    return 0;
}
