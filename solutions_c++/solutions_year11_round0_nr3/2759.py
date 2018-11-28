#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
//#define ONLINE_JUDGE
#define rep(i,n) for(int i=0; i<(n); i++)
#define forr(i,a,b) for(int i=(a);i<=(b);i++)

const int N = 1001;
const int M = (1<<20);
int candy[N];
int dp[2][M];

int main() {
    #ifndef ONLINE_JUDGE
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    #endif

    int tt, cas = 1;
    scanf("%d", &tt);
    for(cas=1; cas<=tt; cas++) {
        //To-Do
        int n,tot=0,tot_m=0, mmax=0;
        scanf("%d", &n);
        for(int i=0; i<n; i++) {
            scanf("%d",candy+i);
            tot+=candy[i];
            tot_m^=candy[i];
            mmax=max(mmax,candy[i]);
        }
        
        int bits=0;
        while(mmax) {
            mmax>>=1;
            bits++;   
        }
        
        int up=(1<<bits);
        
        int ans=-1;
        int pre=0, cur=1;
        for(int i=0;i<up;i++) {
            dp[cur][i]=-1;
        }
        dp[cur][0]=0;
        for(int i=0;i<n;i++) {
            cur = pre;
            pre = 1-cur;
            for(int mask=0; mask<up; mask++) {
                dp[cur][mask]=dp[pre][mask];
            }
            for(int mask=0; mask<up; mask++) {
                if(dp[pre][mask]>=0) {
                    dp[cur][mask^candy[i]]=max(dp[pre][mask^candy[i]],dp[pre][mask]+candy[i]);
                }
            }   
        }
        rep(mask,up) {
            if(mask == (tot_m^mask) && dp[cur][mask]>0 && dp[cur][mask]<tot) {
                ans=max(ans,max(dp[cur][mask],tot-dp[cur][mask]));
            }   
        }
        
        printf("Case #%d: ",cas);
        if(ans==-1) printf("NO\n");
        else printf("%d\n",ans);
    }
    //system("pause");
    return 0;
}
