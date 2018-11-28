#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int T,st,ed,n;
int nn[110];
int ans;
void solve()
{
    ans = -1;
    int i,j,flag;
    for(i = st; i<= ed; i++)
    {
        flag = 0;
        for(j = 0;j < n; j++)
        {
            if(i%nn[j]==0||nn[j]%i==0)
                continue;
            else
            {
                flag = 1;
                break;
            }
        }
        if(flag == 0)
        {
            ans = i;
            return;
        }
    }
    return;
}
int main()
{
    int cs,i;
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    while(scanf("%d",&T)!=EOF)
    {
        cs =1;
        while(T--)
        {
            scanf("%d",&n);
            scanf("%d%d",&st,&ed);
            for(i = 0; i < n; i++)
            {
                scanf("%d",&nn[i]);
            }
            solve();
            printf("Case #%d: ",cs++);
            if(ans == -1)
                printf("NO\n");
            else
                printf("%d\n",ans);
        }
    }
    return 0;
}
