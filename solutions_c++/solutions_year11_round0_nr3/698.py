#include <iostream>
#include <cstdio>
#include <queue>
#include <cstring>
using namespace std;
int a[1002];
int main()
{
    freopen("data.in","r",stdin);
    freopen("out.txt","w",stdout);
    int n,sor,minc,sum,i,t,k;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        scanf("%d",&n);
        sor = 0;sum = 0;
        for(i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
            sum += a[i];
            sor ^= a[i];
            if(i == 0) minc = a[i];
            else minc = min(minc,a[i]);
        }
        if(sor != 0) printf("Case #%d: NO\n",k);
        else printf("Case #%d: %d\n",k,sum-minc);
    }
    return 0;
}
