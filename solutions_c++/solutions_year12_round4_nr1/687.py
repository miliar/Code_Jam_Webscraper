#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<stdlib.h>
#include<time.h>
#include<assert.h>

#include<vector>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<iostream>
#include<algorithm>
#include<string>

using namespace std;

#define FOR(i,n) for(int i=0;i<(n);++i)
#define REP(i,a,b) for(int i=(a);i<=(b);++i)
#define CLR(a,x) memset(a,(x),sizeof(a))

typedef long long LL;
typedef pair<int,int> pii;

LL D[105], L[105];
int she, N;
LL dp[105];


int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A_small.out","w",stdout);

    int T; scanf("%d",&T);

    REP(t,1,T){
        scanf("%d",&N);

        FOR(i,N) cin>>D[i]>>L[i];
        scanf("%d",&she);

        dp[0] = D[0]+min(D[0],L[0]);

        for(int i=1;i<N;++i){
            dp[i] = 0;
            for(int j=0;j<i;++j){
                if(dp[j]>=D[i]){
                    dp[i] = max(dp[i], D[i]+min(D[i]-D[j],L[i]));
                }
            }
        }

        bool can=false;

        FOR(i,N)if(dp[i]>=she) can=true;

        printf("Case #%d: ",t);

        if(can)puts("YES");
        else puts("NO");
    }

    return 0;
}
