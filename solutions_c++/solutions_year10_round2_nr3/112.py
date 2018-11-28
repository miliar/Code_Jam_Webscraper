#include <stdio.h>
#include <assert.h>
#include <utility>
#include <map>
using namespace std;
#define FOR(q,n) for(int q=0; q<n; q++)

#define MOD 100003
long long int fact(int n) {
    assert(n>=0);
    if (n==0) return 1;
    return ((long long)n*fact(n-1))%MOD;

}

typedef long long ll;
typedef pair<ll, ll> PLL;
typedef pair<int, int> PII;
map<PII, int> mapa;
map<PII, int> cmapa;

PLL extended_gcd_(ll a, ll b) {
    // extended gcd
    if (a % b == 0) return make_pair(0, 1);

    PLL tmp = extended_gcd_(b, a % b);
    return make_pair(tmp.second, tmp.first - tmp.second * (a / b));    
}

ll inverse(int a) {
    PLL tmp = extended_gcd_(a, MOD);
    ll g = tmp.first * a + tmp.second * MOD;
    if (g == 1) {
        return (tmp.first + MOD) % MOD;
    } else {
        return 0;
    }
}

int choose(int n,int k) {
    if (cmapa.find(make_pair(n,k))!=cmapa.end()) {
        return cmapa[make_pair(n,k)];
    }
    if (n<0) return 0;
    if (k<0) return 0;
    if (k>n) return 0;
    long long int t=fact(n);
    t = (t*inverse(fact(k)))%MOD;
    t = (t*inverse(fact(n-k)))%MOD;
//    printf("choose %d %d -- %d\n",n,k,(int)t);
    cmapa[make_pair(n,k)]=t;
    return t;
}

int P(int t, int n) {
    if (mapa.find(make_pair(t,n))!=mapa.end()) {
        return mapa[make_pair(t,n)];
    }
    int s=0;
    if (t==1) return 0;
    if (n==1) return 1;
    for (int l=1; l<n; l++) {
        s = (s+(long long) choose(t-n-1, n-l-1) * P(n,l))%MOD;
    }
    mapa[make_pair(t,n)]=s;
    return s;
}

void solve(int _case) {
    int n;
    scanf("%d",&n);
    int cnt=0;
    for(int q=1; q<n; q++)
        cnt = (cnt+P(n,q))%MOD;

    printf("Case #%d: %d\n",_case,cnt);
}

int main() {
    int t;
    scanf("%d", &t);
    FOR(q,t) solve(q+1);
}
