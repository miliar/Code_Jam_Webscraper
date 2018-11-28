
#include <cstdio>
#include <cstdlib>

#define rep(i,n) for(int i=0; i<(n); i++)

using namespace std;

int T,N,s,p;
int t[200];

int solve() {
    int ans=0;
    rep(i, N) {
        int d = t[i] / 3;
        int r = t[i] % 3;
        if (d >= p) {
            ans++;
            continue;
        }
        if (d == (p-1) && (r > 0)) {
            ans++;
            continue;
        }
        if (d==(p-1) && r==0 && s>0 && d>0) {
            ans++; s--;
        }
        if (d==(p-2) && r>0 && s>0 && d>0) {
            ans++; s--;
        }        
    }
    return ans;
}

int main() {
    scanf("%d",&T);
    rep(tc,T) {
        scanf("%d %d %d",&N,&s,&p);
        rep(i,N) scanf("%d",&t[i]);
        int ans = solve();
        printf("Case #%d: %d\n",tc+1,ans);
    }
}
