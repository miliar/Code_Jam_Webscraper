#include<cstdio>
#include<string>
#include<cstring>
#include<memory>
#include<algorithm>
using namespace std;
#define FOR(i,a,b) for(int i = (a); i < (b); ++i)
#define SET(x, v) memset(x, v, sizeof(x))

typedef long long ll;
int c, d;
int p[256], v[256];
int n;
ll  dat[1048576];

int main() {
    int e = 0, T;
    scanf("%d",&T);
    while(T--) {
        scanf("%d%d",&c,&d);
        n = 0;
        ll D = 0;
        FOR(i,0,c) {
            ll pp,vv;
            scanf("%d%d",&p[i],&v[i]);
            pp = p[i], vv = v[i];
            FOR(j,0,vv) {
                dat[n] = D - pp;
                D += d;
                n++;
            }
        }
        //FOR(i,0,n) printf("%lld ",dat[i]);printf("\n");
        double ans = 0.0;
        ll ans2 = 0;
        ll min_f = dat[0];
        FOR(i,1,n) {
            ans2 = max(ans2, dat[i] - min_f);
            min_f=min(min_f, dat[i]);
        }
        ans = ans2/2.;
        printf("Case #%d: %.10lf\n", ++e, ans);
    }
    return 0;
}
