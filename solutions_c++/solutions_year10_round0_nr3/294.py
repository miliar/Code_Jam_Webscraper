#include <cstdio>
#include <iostream>
#include <cstring>
#define MAXN 2000
using namespace std;

int g[MAXN+1],p[MAXN+1];
long long z[MAXN+1];
long long r,k;
int n;

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int c,i,j,q,t;
    long long s,y;
    scanf("%d",&t);
    for(c=0;c<t;c++)
    {
        scanf("%d %d %d",&r,&k,&n);
        s=0;
        for(i=0;i<n;i++)
        {
            scanf("%d",&g[i]);
            s=s+g[i];
        }
        printf("Case #%d: ",c+1);
        if(s<=k)
        {
            printf("%I64d\n",r*s);
            continue;
        }
        memcpy(g+n,g,n*sizeof(int));
        memset(p,-1,sizeof(p));
        p[0]=0;
        z[0]=0;
        y=0;
        for(j=1;j<=r;j++)
        {
            for(s=0;s+g[i]<=k;i++)
            {
                s=s+g[i];
            }
            z[j]=z[j-1]+s;
            y=y+s;
            i=i%n;
            if(p[i]!=-1)
            {
                q=(r-j)/(j-p[i]);
                y=y+(z[j]-z[p[i]])*q;
                j=j+(j-p[i])*q+1;
                break;
            }
            else
            {
                p[i]=j;
            }
        }
        while(j<=r)
        {
            for(s=0;s+g[i]<=k;i++)
            {
                s=s+g[i];
            }
            y=y+s;
            i=i%n;
            j++;
        }
        printf("%I64d\n",y);
    }
    return 0;
}
