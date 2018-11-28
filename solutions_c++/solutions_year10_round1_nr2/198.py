#include <string>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <stack>
#include <set>
#include <iostream>
#include <sstream>
#include <numeric>
#include <algorithm>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <cstdio>
#include <cstring>
using namespace std;

#define CLR(x) memset((x),0,sizeof(x))
#define SET(x,y) memset((x),(y),sizeof(x))
#define REP(i,x) for(int i=0;i<(x);i++)
#define FOR(i,x,y) for(int i=(x);i<(y);i++)
#define VI vector<int> 
#define PB(i,x) (i).push_back(x)
#define MP(x,y) make_pair((x),(y))

int D, I, M, N, A[300], C[300];
int dp[300][300];
int T;

int remove(int a, int b)
{
    if(b-a-1<=0) return 0;
    return D*(b-a-1);
}

int build(int a, int b)
{
    
    int d=abs(a-b);
    if(d==0)return 0;
    if(M==0) return 1<<20;
    return I*((d-1)/M);
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d", &T);
    REP(cas,T){
        scanf("%d %d %d %d", &D,&I,&M,&N);
        REP(i,N) scanf("%d", &A[i+1]);
        int ans = 0;
        REP(i,N+1)REP(j,257)dp[i][j]=1<<20;
        dp[0][256]=0;
        FOR(i,1,N+1) FOR(j,0,257){
            if(j==256){
                dp[i][j]=D*i;
                continue;
            }
            dp[i][j]=dp[i-1][256]+abs(A[i]-j);
            //if(j<=5)printf("%d,%d,%d,%d\n",i,j,dp[i-1][256],abs(A[i]-j));
            if(i>1){
                dp[i][j]=min(dp[i][j],dp[i-1][j]+D);
                REP(k,256){
                    dp[i][j]=min(dp[i][j],abs(A[i]-j)+dp[i-1][k]+build(k,j));
                }
            }
            //if(j<=5)printf("%d,%d(%d)\n",i,j,dp[i][j]);
        }
        ans=1<<20;
        REP(i,257) ans=min(ans,dp[N][i]);
        printf("Case #%d: %d\n", cas+1, ans);
    }
    return 0;
}
