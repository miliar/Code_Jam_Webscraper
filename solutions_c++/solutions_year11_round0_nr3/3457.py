#include<cstdio>
#include<string>
#include<cstring>
#include<memory>
#include<algorithm>
using namespace std;
#define FOR(i,a,b) for(int i = (a); i < (b); ++i)
#define SET(x, v) memset(x, v, sizeof(x))
    int n, N;
int dat[128];
int main() {
    int e=0,T;
    scanf("%d",&T);
    while(T--) {
        scanf("%d",&n);
        FOR(i,0,n) scanf("%d",&dat[i]);
        N = 1<<n;
        int ans = -1;
        FOR(i,1,N-1) {
            int mine = 0;
            int s1, s2;
            s1 = s2= 0;
            FOR(j,0,n) 
                if(i & (1<<j)) {
                    // add to s1
                    mine += dat[j];
                    int s = 0;
                    FOR(k,0,22) 
                        s += (s1&(1<<k))^(dat[j]&(1<<k));
                    s1 = s;
                }
                else {
                    // add to s2
                    int s = 0;
                    FOR(k,0,22) 
                        s += (s2&(1<<k))^(dat[j]&(1<<k));
                    s2 = s;
                }
            if(s1 == s2) {
                ans=max(ans, mine);
            }
        }
        if(ans == -1) printf("Case #%d: NO\n",++e);
        else          printf("Case #%d: %d\n",++e, ans);
    }
    return 0;
}
