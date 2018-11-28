#include<iostream>
using namespace std;
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C.out","w",stdout);
    int j,i,t,x,m,ans,sum,n;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d",&n);
        sum=0;
        for(j=0;j<n;j++)
        {
            scanf("%d",&x);
            sum+=x;
            if(j==0)
            {
                m=x;
                ans=x;
            }
            else
            {
                m=min(x,m);
                ans^=x;
            }
        }
        printf("Case #%d: ",i);
        if(ans!=0) printf("NO\n");
        else printf("%d\n",sum-m);
    }
    return 0;
}
