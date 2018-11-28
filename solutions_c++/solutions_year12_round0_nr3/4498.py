#include <iostream>
#include <cstdio>
#include <cstring>
#include <map>
#include <cmath>
using namespace std;
int bit[]= {1,10,100,1000,10000,100000,1000000,10000000};
int A,B,ans;
void dfs(int x)
{
    int pre=-1;
    for(int i=1; i<=int(log10(x)); i++)
    {
        int j=x%bit[i],k=x/bit[i];
        int now=j*bit[int(log10(k))+1]+k;
        if(now>A&&now<=B&&now>x&&now!=pre)
        {
            ans++;
            pre=now;
        }
    }
}
int main()
{
    freopen("txt.in","r",stdin);
    freopen("txt.out","w",stdout);
    int t,num=1;
    cin >>t;
    while(t--)
    {
        ans=0;
        scanf("%d%d",&A,&B);
        for(int i=A; i<B; i++)
        {
            dfs(i);
        }
        printf("Case #%d: ",num++);
        printf("%d\n",ans);
    }
    return 0;
}
