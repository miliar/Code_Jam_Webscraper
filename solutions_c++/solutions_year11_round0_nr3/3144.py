#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
    int i,j,k,t,n,sum,mini,x;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d",&n);
        sum=0;
        mini=1000000;
        x=0;
        for(j=0;j<n;j++)
        {
            scanf("%d",&k);
            sum+=k;
            mini=min(mini,k);
            x^=k;
        }
        printf("Case #%d: ",i);
        if(x)
            printf("NO\n");
        else
            printf("%d\n",sum-mini);
    }
    return  0;
}
