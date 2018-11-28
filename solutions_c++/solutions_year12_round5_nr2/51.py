#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstdarg>
#include <cassert>
#include <climits>
#include <cstring>
#include <complex>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <cmath>
#include <ctime>
#include <set>
#include <map>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pi;
typedef vector<int> vi;


#define all(c) (c).begin(),(c).end()
#define sz(c) (int)(c).size()

#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define x first
#define y second
#define y1 y1_gdssdfjsdgf
#define y0 y0_fsdjfsdogfs
#define ws ws_fdfsdfsdgfs
#define image(a) {sort(all(a)),a.resize(unique(all(a))-a.begin());}
#define eprintf(...) {fprintf(stderr,__VA_ARGS__),fflush(stderr);}

#define forn(i,n) for( int i = 0 ; i < (n) ; i++ )
#define forit(it,c) for( __typeof((c).begin()) it = (c).begin() ; it != (c).end() ; it++ )
#define problem_name "a"
int n, m;
const int mx = 6003;
int a[mx * mx];
int up[mx * mx];
int cl[mx * mx];
int x[100000];
int y[100000];
int dx[6] = {0,1,1,0,-1,-1};
int dy[6] = {1,1,0,-1,-1,0};
int num(int x, int y) {
	return x + (y) * (2 * n + 1);
}
int go(int x) {
	if (up[x] == x) return x;
	return up[x] = go(up[x]);
}
void uni(int x, int y) {
	x = go(x);
	y = go(y);
	if (x != y) {
		up[y] = x;
		cl[x] |= cl[y];
	}
}
bool bridge(int k) {
	for (int i = 0; i < (2 * n + 1) * (2 * n + 1); i++) {
		up[i] = i;
		a[i] = 0;
		cl[i] = 0;
	}
	cl[num(1, 1)] = 1;
	cl[num(1, n)] = 2;
	cl[num(n, 1)] = 4;
	cl[num(n, 2 * n - 1)] = 8;
	cl[num(2 * n - 1, n)] = 16;
	cl[num(2 * n - 1, 2 * n - 1)] = 32;	
	for (int i = 0; i < k; i++) {
		a[num(x[i], y[i])] = 1;
		for (int j = 0; j < 6; j++) {
			if (a[num(x[i] + dx[j], y[i] + dy[j])] == 1) {				
//				cerr<<go(num(x[i], y[i]))<<" "<<go(num(x[i] + dx[j], y[i] + dy[j]))<<endl;
				uni(num(x[i], y[i]), num(x[i] + dx[j], y[i] + dy[j]));
//				cerr<<go(num(x[i], y[i]))<<" "<<go(num(x[i] + dx[j], y[i] + dy[j]))<<endl;				
				if (__builtin_popcount(cl[go(num(x[i], y[i]))]) >= 2) {
					return true;
				}
			}
		}
	}
	return false;
}
bool fork(int k) {
	for (int i = 0; i < (2 * n + 1) * (2 * n + 1); i++) {
		up[i] = i;
		a[i] = 0;
		cl[i] = 0;
	}
	for (int i = 2; i < n; i++) {
		cl[num(1, i)] = 1;
		cl[num(i, 1)] = 2;
		cl[num(n - 1 + i, i)] = 4;
		cl[num(i, n - 1 + i)] = 8;
		cl[num(2 * n - 1, n - 1 + i)] = 16;
		cl[num(n - 1 + i, 2 * n - 1)] = 32;				
	}	
	for (int i = 0; i < k; i++) {
		a[num(x[i], y[i])] = 1;
		for (int j = 0; j < 6; j++) {
			if (a[num(x[i] + dx[j], y[i] + dy[j])] == 1) {				
//				cerr<<go(num(x[i], y[i]))<<" "<<go(num(x[i] + dx[j], y[i] + dy[j]))<<endl;
				uni(num(x[i], y[i]), num(x[i] + dx[j], y[i] + dy[j]));
//				cerr<<go(num(x[i], y[i]))<<" "<<go(num(x[i] + dx[j], y[i] + dy[j]))<<endl;				
				if (__builtin_popcount(cl[go(num(x[i], y[i]))]) >= 3) {
				//	cerr<<i<<endl;
				//	cerr<<cl[go(num(x[i], y[i]))]<<endl;
					return true;
				}
			}
		}
	}
	return false;
}
void dfs(int x, int y) {
	if (x < 0 || x > 2 * n || y < 0 || y > 2 * n) return;
	if (a[num(x, y)] != 0) return;
	a[num(x, y)] = 1;
	for (int i = 0; i < 6; i++) {
		dfs(x + dx[i], y + dy[i]);
	}
}
bool cycle(int k) {
	for (int i = 0; i < (2 * n + 1) * (2 * n + 1); i++) {
		a[i] = 0;
	}
	for (int i = 0; i < k; i++) {		
		a[num(x[i], y[i])] = 1;
	}
	dfs(0, 0);
	for (int i = 0; i <= 2 * n; i++)
		for (int j = 0; j <= 2 * n; j++) {
			if (a[num(i, j)] == 0) {
				return true;
			}
		}
	return false;
}

int main(){	
	freopen(problem_name".in","rt",stdin);
	freopen(problem_name".out","wt",stdout);
	int T;
    scanf("%d", &T);
    for (int ti = 1; ti <= T; ti++) {
    	printf("Case #%d: ", ti);
		scanf("%d %d", &n, &m);		
		for (int i = 0; i < m; i++) {
			scanf("%d %d", &x[i], &y[i]);
		}
		int ll, rr, mm;
	//	cerr<<bridge(2)<<endl;
	//	return 0;
		ll = m;
		rr = m;
		for (int i = 0; i <= m; i++) {
			if (bridge(i) || fork(i) || cycle(i)) {
				ll = i - 1;
				break;
			}
		}		
		if (ll == m) {
			printf("none\n");
			continue;
		}
		ll++;
		vector<string> vv;
		if (bridge(ll)) {
			vv.pb("bridge");
		}
		if (fork(ll)) {
			vv.pb("fork");
		}
		if (cycle(ll)) {
			vv.pb("ring");
		}
		for (int i = 0; i < sz(vv); i++) {
			if (i != 0) cout<<"-";
			cout<<vv[i];
		}
		printf(" in move %d\n", ll);
    }
	return 0;
}
