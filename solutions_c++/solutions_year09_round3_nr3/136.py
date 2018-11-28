#include <iostream>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
using namespace std;
int n, p, q;
int s[128];
int dp[128][128];
int go(int l, int r) {
                if (l+1==r) return 0;
                if (dp[l][r]!=-1) return dp[l][r];
                dp[l][r]=1000000000;
                for (int i=l+1; i<r; ++i) dp[l][r]<?=s[r]-s[l]-2+go(l,i)+go(i,r);
                return dp[l][r];
}
int main()
{
                freopen("C-large (2).in","r",stdin);
                freopen("C.out","w",stdout);
                scanf("%d", &n);
                for (int tc=1; tc<=n; ++tc) {
                                scanf("%d%d", &p, &q);
                                for (int i=1; i<=q; ++i) scanf("%d", s+i);
                                s[0]=0; s[q+1]=p+1;
                                memset(dp,-1,sizeof(dp));
                                printf("Case #%d: %d\n", tc, go(0, q+1));
                }
}
