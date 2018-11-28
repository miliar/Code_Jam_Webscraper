

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
void solve() {
    int n;
    scanf("%d", &n);
    int diff[2] = { 0, 0 };
    int p[2] = { 1, 1 };
    int result = 0;
    db(n);
    rep (i, n) {
        char who; int np;
        scanf(" %c %d", &who, &np);
        db(who<<" "<<np);
        who = who == 'B';

        int curdiff = max(0, abs(np - p[who]) - diff[who]);

        diff[who] = 0;
        diff[1-who] += curdiff + 1;
        p[who] = np;
        result += curdiff + 1;
        db(curdiff);
    }
    printf("%d\n", result);
}

int main(int argc, char ** argv) {
	cond = argc >= 2 && argv[1][0] == 'q' ? 1 << 30 : 0;
    int t;
    scanf("%d", &t);
    rep (i, t) {
        printf("Case #%d: ", i + 1);
        solve();
    }
   	return 0;
}


