#include <cstdio>
#include <map>
#include <set>
#include <cstring>
using namespace std;

#define REP(i,a,b) for(int i=a; i<b; ++i)
#define rep(i,n) REP(i,0,n)
#define FORIT(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)

int in[1000],n,t;
int dp[2][1<<20];

int func() {
    int bap[20] = {};
    for(int i=0; i<n; ++i) {
        int k = in[i],cnt = 0;
        while(k > 0) {
            if(k%2) bap[cnt]++;
            k /= 2;
            cnt++;
        }
    }

    for(int i=19; i>=0; --i) {
        if(bap[i]%2) return -1;
    }

    int ans = 0;
    // check ans
    REP(i,1,1<<20) {
        if(dp[n%2][i] == -1) continue;
        ans = max(dp[n%2][i], ans);
    }
    return ans;
}

int main() {
    scanf("%d", &t);
    for(int tc=1; tc<=t; ++tc) {
        memset(dp, -1, sizeof(dp));
        dp[0][0] = 0;
        scanf("%d", &n);
        for(int i=0; i<n; ++i) scanf("%d", &in[i]);

        for(int i=0; i<n; ++i) {
            for(int j=0; j<=1000000; ++j)
                if(dp[i%2][j] >= 0) {
                    // printf("%d %d, ", i, j);
                    // printf("%d : %d,    ", (i+1)%2, j^in[i]);
                    dp[(i+1)%2][j] = max(dp[(i+1)%2][j], dp[i%2][j]);
                    dp[(i+1)%2][j^in[i]] = max(dp[(i+1)%2][j^in[i]],
                                               dp[i%2][j] + in[i]);
                }
            // puts("");
        }

        printf("Case #%d: ", tc);

        int a = func();
        if(a == -1) {
            printf("NO\n");
        }else{
            printf("%d\n", a);
        }
    }
}
