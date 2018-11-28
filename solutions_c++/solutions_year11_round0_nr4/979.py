#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<time.h>
#include<ctype.h>

#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<string>
#include<iostream>

using namespace std;

#define FOR(i,n) for(int i=0;i<(n);++i)
#define REP(i,a,b) for(int i=(a);i<=(b);++i)
#define CLR(A,x) memset(A,(x),sizeof(A))

typedef long long LL;
typedef pair<int,int> pii;

bool seen[1005];
int A[1005];

int dfs(int x)
{
    seen[x]=1;
    int ret=1;

    if(!seen[A[x]])
        ret += dfs(A[x]);
    return ret;
}

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);

    int n, T; scanf("%d",&T);

    REP(t,1,T)
    {
        scanf("%d",&n);
        REP(i,1,n)
        {
            scanf("%d",A+i);
            seen[i] = 0;
        }

        int ans = 0;

        REP(i,1,n)
        {
            if(!seen[i])
            {
                int cnt = dfs(i);
                if(cnt>1) ans += cnt;
            }
        }

        printf("Case #%d: %lf\n",t,(double)ans);
    }

    return 0;
}
