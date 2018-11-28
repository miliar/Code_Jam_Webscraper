#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;
int t,n,a[1005];
bool visit[1005];
int main()
{
//    freopen("D-large.in","r",stdin);
//    freopen("D-large.out","w",stdout);
    int i;
    scanf("%d",&t);
    double ans;
    int cases = 1;
    int tem;
    int cnt;
    while(t--)
    {
        scanf("%d",&n);
        for(i=1;i<=n;i++)
            scanf("%d",&a[i]);
        ans = 0;
        memset(visit,false,sizeof(visit));
        for(i=1;i<=n;i++)
        {
            if(visit[i]) continue;
            tem = i;cnt = 0;
            while(!visit[tem])
            {
                visit[tem] = 1;
                tem = a[tem];
                cnt++;
            }
            if(cnt==1) cnt = 0;
            ans+=cnt;
        }
        printf("Case #%d: %.6f\n",cases++,ans);
    }
	return 0;
}
