#include<iostream>
using namespace std;
int i,t,tmp,j,n,ans;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d",&n);
        ans=n;
        for(j=1;j<=n;j++)
        {
            scanf("%d",&tmp);
            if(tmp==j)ans--;
        }
        printf("Case #%d: %d.000000\n",i,ans);
    }
}
