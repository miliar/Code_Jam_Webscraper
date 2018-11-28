#include<cstdio>
#include<cstring>
using namespace std;

int test;
int start[100],speed[100];
bool flag[100];
int n,k,p,t;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("result.out","w",stdout);
    scanf("%d",&test);
    int cas=0;
    while(test--)
    {
        scanf("%d%d%d%d",&n,&k,&p,&t);
        for(int i=0;i<n;i++)
            scanf("%d",&start[i]);
        for(int i=0;i<n;i++)
            scanf("%d",&speed[i]);
        memset(flag,false,sizeof(flag));
        for(int i=0;i<n;i++)
        {
            if(start[i]+speed[i]*t>=p) flag[i]=true;
            else flag[i]=false;
        }
        int u,num=0;
        for(int i=n-1;i>=0;i--)
        {
            if(flag[i])
            {
                num++;
                if(num==k)
                {
                    u=i;
                    break;
                }
            }
        }
        if(num<k)
        {
            printf("Case #%d: IMPOSSIBLE\n",++cas);
            continue;
        }
        int ans=0;
        for(int i=u;i<n;i++)
        {
            if(!flag[i]) continue;
            for(int j=i+1;j<n;j++)
            {
                if(!flag[j]) ans++;
            }
        }
        printf("Case #%d: %d\n",++cas,ans);
    }
    return 0;
}
                
