#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <complex>

using namespace std;

//
typedef long long LL;
typedef pair<int,int> PII;
#define MP make_pair
#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define SIZE(x) (int)x.size()
#define ALL(c) c.begin(),c.end()
//
#define rep(i,b) for(int i=(0);i<(b);++i)
#define fo(i,a,b) for(int i=(a);i<=(b);++i)
#define ford(i,a,b) for(int i=(a);i>=(b);--i)
#define fore(a,b) for(__typeof((b).begin()) a = (b).begin();a!=(b).end();++a)
#define vv vector
#define pb push_back
#define ll long long
#define ld long double
#define ss(a) (int)(a).size()
#define all(x) (x).begin(),(x).end()
#define clr(x,a) memset(x,a,sizeof(x))
#define vi vv<int>
#define vs vv<string>
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}

int cond = (ll)1;
#define db(x) { if (cond > 0) { cond--; rep (xxx, 1) cerr << __LINE__ << " " << #x << " " << x << endl; cerr.flush(); } }


const int sz = (int)1e6 + 11;
bool pr[sz];

bool prime(int i) {
    for (int j = 2; j * j <= i; j++) if (i % j == 0) { return false; }
    return true;
}

void _main() {
    ll n;
    scanf("%lld", &n);
    ll diff = n >= 2 ? 1 : 0;
    fo (i, 2, min((ll)sz - 1,  n)) if (prime(i)) {
        ll cur = i;
        while (cur <= n) {
            diff++;
            cur *= i;
        }
        diff--;
    }
    printf (" %lld\n", diff);
}

int main(int argc, char ** argv) {
    fo (i, 2, sz - 1) pr[i] = prime(i);
    string p = "../gcj/source/" + string("") + argv[0][strlen(argv[0])-1];
    freopen("1.in","r",stdin);
    rep (i, argc) if (strcmp(argv[i], "s0") == 0) { freopen((p + "-small-0.in").c_str(),"r",stdin);freopen((p + "-small-0.out").c_str(),"w",stdout); }
    rep (i, argc) if (strcmp(argv[i], "s1") == 0) { freopen((p + "-small-1.in").c_str(),"r",stdin);freopen((p + "-small-1.out").c_str(),"w",stdout); }
    rep (i, argc) if (strcmp(argv[i], "s2") == 0) { freopen((p + "-small-2.in").c_str(),"r",stdin);freopen((p + "-small-2.out").c_str(),"w",stdout); }
    rep (i, argc) if (strcmp(argv[i], "l0") == 0) { freopen((p + "-large-0.in").c_str(),"r",stdin);freopen((p + "-large-0.out").c_str(),"w",stdout); }
    rep (i, argc) if (strcmp(argv[i], "q") == 0) cond = 1 << 30;
    db(argc);
    int t;
    scanf("%d", &t);
    fo (i, 1, t) {
        db(i);
        printf("Case #%d:", i);
        _main();
        fflush(stdout);
        cerr.flush();
    }
    return 0;
}

