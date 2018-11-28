#include <cstdio>
#include <iostream>
#include <algorithm>
#define MAXN 800
using namespace std;

int x[MAXN+1],y[MAXN+1];
long long sum;
int n;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,k,t;
    scanf("%d",&t);
    for(k=0;k<t;k++)
    {
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%d",&x[i]);
        }
        sort(x,x+n);
        for(i=0;i<n;i++)
        {
            scanf("%d",&y[i]);
        }
        sort(y,y+n);
        reverse(y,y+n);
        sum=0;
        for(i=0;i<n;i++)
        {
            sum=sum+1LL*x[i]*y[i];
        }
        printf("Case #%d: %I64d\n",k+1,sum);
    }
    return 0;
}
