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
using namespace std;

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

int cond = (ll)1;
#define db(x) { if (cond > 0) { cond--; rep (xxx, 1) cerr << __LINE__ << " " << #x << " " << x << endl; cerr.flush(); } }

#define pii complex<int>

int ary[1<<12];
int cena[1<<12];

void solve() {
    int p;
    scanf("%d", &p);
    clr(ary, 0x7f);

    rep (i,1<<p) scanf("%d", &ary[(1<<p)+i]);
    rep (i,(1<<p)-1) scanf("%d", &cena[i]);
    rep (i,1<<p) {
        int cur = (1<<p) + i;
        int x = ary[cur];
        db(i<<" "<<x);
        while (cur >= 1) {
            db(cur<<" "<<x);
            ary[cur] = min(ary[cur], x);
            cur /= 2;
            --x;
        }
    }
    int ret = 0;
    rep (i, 1<<p) {
        if (ary[i] < 0) {
            ret++;
            cerr << i << " " << ary[i] << endl;
        }
    }
    printf("%d\n", ret * cena[0]);
}

int main(int argc, char ** argv) {
    //freopen("1.in","r",stdin); 
    //freopen("2.in","r",stdin); 
    //freopen("3.in","r",stdin); 

    freopen("../B-small-attempt0.in","r",stdin);freopen("B-small-attempt0.out","w",stdout);
    //freopen("../B-small-attempt1.in","r",stdin);freopen("B-small-attempt1.out","w",stdout);
    //freopen("../B-small-attempt2.in","r",stdin);freopen("B-small-attempt2.out","w",stdout);

    //freopen("../B-large.in","r",stdin); freopen("B-large.out","w",stdout);

    cond = argc >= 2 && argv[1][0] == 'q' ? 1 << 30 : 0;
    int t;
    scanf("%d", &t);
    fo (i, 1, t) {
        cerr << "i" << " " << i << endl;
        printf("Case #%d: ", i);
        solve();
        fflush(stdout);
        cerr.flush();
    }
	return 0;
}

