#include <vector>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <map>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <string>
#include <set>
#include <cstring>
using namespace std;
#define For(i,n) for(int i=0;i<n;i++)
#define sz(i) int(i.size())
#define mst(i,n) memset(i,n,sizeof(i))
#define eps 1e-9
#define INF 1e20
#define MOD 1000000007
#define LL long long
#define pi acos(-1)
LL gcd(LL a,LL b){if(a==0)return b;return gcd(b%a,a);}
int main()
{
    int T;
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&T);
    For(ca,T)
    {
        int n,d[10005],l[10005];
        scanf("%d",&n);
        For(i,n)scanf("%d %d",&d[i],&l[i]);
        int D;
        scanf("%d",&D);
        int dp[10005];
        mst(dp,-1);
        dp[0]=d[0];
        bool ans = 0;
        For(i,n){
            if(dp[i]==-1)
                continue;
            int len = dp[i]+d[i];
            for(int j=i+1;j<n&&d[j]<=len;j++){
                int tp = min(l[j],d[j]-d[i]);
                if(dp[j]==-1||tp>dp[j])
                    dp[j]=tp;
            }
            if(dp[i]+d[i]>=D)
                ans = 1;
        }
        printf("Case #%d: ",ca+1);
        if(ans)
            printf("YES\n");
        else
            printf("NO\n");
    }
}
