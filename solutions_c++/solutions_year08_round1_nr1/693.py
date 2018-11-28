#include<stdio.h>
#include<algorithm>

using namespace std;

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    
    int cases,ii,n,i;
    long long int an,x[1002],y[1002];
    
    scanf("%d",&cases);
    
    for(ii=1;ii<=cases;ii++)
    {
        scanf("%d",&n);
        for(i=1;i<=n;i++)scanf("%I64d",&x[i]);
        for(i=1;i<=n;i++)scanf("%I64d",&y[i]);
        sort(x+1,x+1+n);
        sort(y+1,y+1+n);
        an=0;
        for(i=1;i<=n;i++)an+=x[i]*y[n-i+1];
        printf("Case #%d: %I64d\n",ii,an);
    }
    
    
    return 0;
}
