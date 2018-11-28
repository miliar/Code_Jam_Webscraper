#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<iostream>
using namespace std;
int num[1005];
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    int t,cas=0;
    scanf("%d",&t);
    while(t--)
    {
        int n;
        scanf("%d",&n);
        for(int i=1;i<=n;i++)
            scanf("%d",num+i);
        int ans=0;
        int len=0;
        for(int i=1;i<=n;i++)
            if(num[i]!=i)
                ans++;
        printf("Case #%d: %d.000000\n",++cas,ans);
    }
    return 0;
}
