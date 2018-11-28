#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<iostream>
using namespace std;
int sum[40];
int num[1005];
void add(int k)
{
    int pos=0;
    while(k)
    {
        if(k&1)
            sum[pos]++;
        k>>=1;
        pos++;
    }
}
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int t,cas=0;
    scanf("%d",&t);
    while(t--)
    {
        memset(sum,0,sizeof(sum));
        int n;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
            scanf("%d",num+i);
            add(num[i]);
        }
        bool bad=0;
        for(int i=0;i<32;i++)
            if(sum[i]%2)
            {
                bad=1;
                break;
            }
        printf("Case #%d: ",++cas);
        if(bad)
        {
            printf("NO\n");
            continue;
        }
        sort(num,num+n);
        int ans=0;
        for(int i=1;i<n;i++)
            ans+=num[i];
        printf("%d\n",ans);
    }
    return 0;
}
