#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

const int MAXN = 10000 + 10;
const int INF = 1<<30;
const double eps = 1e-8;

int d[MAXN],l[MAXN],D;
int n;
int dp[MAXN];

int main()
{
    freopen("Ain.in","r",stdin);
    freopen("Aout.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        scanf("%d",&n);
        for(int i=0;i<n;i++)
            scanf("%d%d",&d[i],&l[i]);
        scanf("%d",&D);
        if(d[0]>l[0])
        {
            printf("Case #%d: NO\n",cas);
            continue;
        }
        if(d[0]*2>=D)
        {
            printf("Case #%d: YES\n",cas);
            continue;
        }
        memset(dp,0,sizeof(dp));
        dp[0]=d[0];
        for(int i=0;i<n;i++)
            for(int j=i+1;j<n&&dp[i]+d[i]>=d[j];j++)
                dp[j]=max(dp[j],min(l[j],d[j]-d[i]));
        if(dp[n-1]+d[n-1]>=D) printf("Case #%d: YES\n",cas);
        else printf("Case #%d: NO\n",cas);
    }
	return 0;
}

/*
1
2
10 10
11 10
21
*/
