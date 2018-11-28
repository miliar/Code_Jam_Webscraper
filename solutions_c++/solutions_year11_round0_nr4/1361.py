#include<iostream>
#include<cstdio>
#include<cstring>
using namespace  std;

int main()
{
    int i,ii,t,n,a,s;
    freopen("D1.in","r",stdin);
    freopen("D1.out","w",stdout);
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        s=0;
        scanf("%d",&n);
        for(ii=1;ii<=n;ii++)
        {
           scanf("%d",&a);
           if(a!=ii)
           s++;
        }
        printf("Case #%d: %d.000000\n",i,s);
    }
    return 0;
}
