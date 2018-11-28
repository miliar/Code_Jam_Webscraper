#include <cstdio>
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

int n, k;

int a[111][111];

bool isl(int i, int j) {
	int cnt = 0;
	rep (g, k) if (a[i][g] < a[j][g]) cnt++;
	return cnt == k;
}

bool isl2(int i, int j) {
	int cnt = 0;
	rep (g, k) if (a[i][g] <= a[j][g]) cnt++;
	return cnt == k;
}

int used[1<<16];
int comp[1<<16];

void solve() {
	scanf("%d%d", &n, &k);
	db(n<<" "<<k);
	rep (i, n) {
		rep (j, k) {
			scanf("%d", &a[i][j]);
		}
	}
	clr(used, 0x3f);
	clr(comp, 0);
	used[0] = 0;
	rep (i, 1 << n) {
		vi tmp;
		rep (g, n) if ((1<<g)&i) {
			tmp.pb(g);
			if (i == (1<<n)-1) db(i<<" "<<g);
		}
		int &ok = comp[i] = 1;
		if (i == (1<<n)-1) fore (it, tmp) db(tmp.size()<<" "<<i<<" "<<n<<" "<<*it);
		rep (a, ss(tmp)) rep (b, a) ok = ok && (isl(tmp[a], tmp[b]) || isl(tmp[b], tmp[a]));
	}
	db(comp[(1<<n)-1]);
	rep (i, 1 << n) {
		for (int j = i; j > 0; j = (j-1)&i) {
			if (comp[j])
				used[i] = min(used[i], 1 + used[i^j]);
		}
	}

	printf("%d", used[(1<<n)-1]);
}

int main(int argc, char ** argv) {
    ios::sync_with_stdio(false);
    cond = argc >= 2 && argv[1][0] == 'q' ? 1 << 30 : 0;
    int t;
    scanf("%d", &t);
    fo (i, 1, t) {
	    cerr<<i<<endl;
	    printf("Case #%d: ", i);
	    solve();
	    printf("\n");
    }
    return 0;
}

