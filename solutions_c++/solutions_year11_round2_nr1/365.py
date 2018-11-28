#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#define MAXN 100
using namespace std;

char g[MAXN+1][MAXN+1];
double wp[MAXN+1],owp[MAXN+1],oowp[MAXN+1];
int c0[MAXN+1],c1[MAXN+1];
int n;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,j,k,c,t;
    double s;
    scanf("%d",&t);
    for(c=0;c<t;c++)
    {
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%s",g[i]);
            c0[i]=count(g[i],g[i]+n,'0');
            c1[i]=count(g[i],g[i]+n,'1');
            wp[i]=1.0*c1[i]/(c1[i]+c0[i]);
            //printf("wp%d = %.6f\n",i,wp[i]);
        }
        for(i=0;i<n;i++)
        {
            s=0.0;
            k=0;
            for(j=0;j<n;j++)
            {
                if(g[i][j]!='.')
                {
                    if(g[i][j]=='1')
                    {
                        s=s+1.0*c1[j]/(c1[j]+c0[j]-1);
                        k++;
                    }
                    else
                    {
                        s=s+1.0*(c1[j]-1)/(c1[j]+c0[j]-1);
                        k++;
                    }
                }
            }
            owp[i]=s/k;
            //printf("owp%d = %.6f\n",i,owp[i]);
        }
        for(i=0;i<n;i++)
        {
            s=0.0;
            k=0;
            for(j=0;j<n;j++)
            {
                if(g[i][j]!='.')
                {
                    s=s+owp[j];
                    k++;
                }
            }
            oowp[i]=s/k;
            //printf("oowp%d = %.6f\n",i,oowp[i]);
        }
        printf("Case #%d:\n",c+1);
        for(i=0;i<n;i++)
        {
            printf("%.12f\n",0.25*wp[i]+0.50*owp[i]+0.25*oowp[i]);
        }
    }
    return 0;
}
