#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#define MAXN 1000000
#define LIMIT 255
using namespace std;

int p[MAXN+1];
double d;
int c,n;

int check(double mid)
{
    int i;
    double pos;
    pos=p[0]-mid;
    for(i=1;i<n;i++)
    {
        if(p[i]+mid<pos+d)
        {
            return 0;
        }
        pos=max(p[i]-mid,pos+d);
    }
    return 1;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int i,j,k,z,t,q,v;
    double low,high,mid;
    scanf("%d",&t);
    for(z=0;z<t;z++)
    {
        scanf("%d %lf",&c,&d);
        n=0;
        for(i=0;i<c;i++)
        {
            scanf("%d %d",&q,&v);
            for(j=0;j<v;j++)
            {
                p[n++]=q;
            }
        }
        low=0.0;
        high=1e12;
        for(k=0;(k<LIMIT)&&(low<high-1e-8);k++)
        {
            mid=(low+high)*0.5;
            if(check(mid)==1)
            {
                high=mid;
            }
            else
            {
                low=mid;
            }
        }
        printf("Case #%d: %.6f\n",z+1,high);
    }
    return 0;
}
