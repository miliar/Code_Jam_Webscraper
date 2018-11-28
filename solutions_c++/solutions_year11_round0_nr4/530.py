#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int cases=1,n,a[1010],ans;
bool flag[1010];

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        memset(flag,false,sizeof(flag));
        ans=0;
        for(int i=1;i<=n;++i)
        scanf("%d",&a[i]);
        for(int i=1;i<=n;++i)
        {
            if(flag[i])continue;
            int u=a[i],len=1;
            flag[i]=true;
            while(!flag[u])
            {
                flag[u]=true;
                u=a[u];
                len++;
            }
            if(len>1)
            ans+=len;
        }
        printf("Case #%d: %d.000000\n",cases++,ans);
    }
    return 0;
}
