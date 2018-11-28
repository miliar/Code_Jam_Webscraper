#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;
int n,S,P;
int f(int x,int s)
{
    if(s>1)return -998998998;
    int i,j,k,m=0;
    for(i=0;i<=10;i++)
    for(j=i;j<=min(10,i+2);j++)
    {
        k=x-i-j;
        if(k<j||k-i>2)continue;
        if(s&&(k-i!=2))continue;
        if(!s&&(k==2+i))continue;
        m=max(m,k);
    }
    return m>=P;
}
int a[111];
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int i,j,k,m,n,l,t,cs=1,ans;
    scanf("%d",&t);
    while(t--)
    {
        ans=0;
        scanf("%d %d %d",&n,&S,&P);
        for(i=1;i<=n;i++)
        scanf("%d",&a[i]);
        if(n==1)ans=max(ans,f(a[1],S));
        if(n==2)
        {
            for(i=0;i<=S;i++)
            ans=max(ans,f(a[1],i)+f(a[2],S-i));
        }
        if(n==3)
        {
            for(i=0;i<=S;i++)
            for(j=0;j<=S-i;j++)
            ans=max(ans,f(a[1],i)+f(a[2],j)+f(a[3],S-i-j));
        }
        printf("Case #%d: %d\n",cs++,ans);
    }

}
