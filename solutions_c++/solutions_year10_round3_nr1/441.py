#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;
int t,n;
struct SS
{
    int u,v;
}ss[1005];
bool cmp(SS sa,SS sb)
{
    return sa.u < sb.u;
}
int main()
{
        freopen("A-large.in","r",stdin);
        freopen("a.out","w",stdout);
        int ans;
        int case_t;
        int i,j;
        while(scanf("%d",&t)!=EOF)
        {
            case_t = 1;
            while(t--)
            {
                ans = 0;
                scanf("%d",&n);
                for(i=0;i<n;i++)
                {
                    scanf("%d%d",&ss[i].u,&ss[i].v);
                }
                sort(ss,ss+n,cmp);
                for(i=1;i<n;i++)
                {
                    for(j=0;j<i;j++)
                    {
                        if(ss[i].v < ss[j].v)
                            ans++;
                    }
                }
                printf("Case #%d: ",case_t++);
                printf("%d\n",ans);
            }
        }
        return 0;
}
