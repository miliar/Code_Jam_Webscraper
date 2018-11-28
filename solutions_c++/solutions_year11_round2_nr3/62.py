#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <cassert>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define all(a) a.begin(), a.end()
#define fs first
#define sc second
#define mp make_pair
#define pb push_back

typedef pair<int,int> pii;
typedef long long int64;

const int inf = 2 * 1e9 + 2;
const double eps = 1e-6;

const int nmax = 100;

int n,m;
int u[100], v[100];
int cnt;
vector<int> g[nmax];
int pos[100];
bool used[100];
vector<int> a,b;
int col[nmax];
int res;
int mask[nmax], ans[nmax];

void check(){
	int nd = 0;
	forn(i, n)
		nd = max(nd, col[i]);
	nd ++;
	if (nd <= res)
		return;
	forn(i, cnt){
		mask[i] = 0;
		forn(j, g[i].size())
			mask[i] |= (1 << col[g[i][j]]);
		if (mask[i] != ((1 << nd) - 1))
			return;
	}
	if (res < nd){
		res = nd;
		forn(i, n)
			ans[i] = col[i];
	}
}

void go(int c, int x){
	col[x] = c;
	bool done = 0;
	for (int i = 0; i < n; i++)
		if (col[i] == -1){
			go(c + 1, i);
			done = 1;
			break;
		}
	for (int i = x + 1; i < n; i++)
		if (col[i] == -1)
			go(c,i);
	if (!done)
		check();
	col[x] = -1;

}

void solve(){
	cin >> n >> m;
	forn(i, m)
		cin >> u[i];
	forn(i, m)
		cin >> v[i];
	forn(i, n){
		u[i] --;
		v[i] --;
	}
	a.clear();
	forn(i, n){
		a.pb(i);
		g[i].clear();
	}
	res = -1;
	cnt = 0;
	memset(used, 0, sizeof used);
	while (cnt < m){
//		cerr << "a\n";
//		forn(i, a.size())
//			cerr << a[i] << " ";
//		cerr << endl;
		
		for (int i = 0; i < a.size(); i++)
			pos[a[i]] = i;
		int p = -1;
		for (int i = 0; i < m; i++)
			if (!used[i] && (p == -1 || abs(pos[u[i]] - pos[v[i]]) < abs(pos[u[p]] - pos[v[p]])))
				p = i;
		if (p == -1) break;
		for (int i = pos[u[p]]; i <= pos[v[p]]; i++)
			g[cnt].pb(a[i]);
		for (int i = 0; i <= pos[u[p]]; i++)
			b.pb(a[i]);
		for (int i = pos[v[p]]; i < a.size(); i++)
			b.pb(a[i]);
		a = b;
		b.clear();
		used[p] = 1;
		cnt ++;
	}
	g[cnt] = a;
	cnt ++;
//	forn(i, cnt){
//		forn(j, g[i].size())
//			cerr << g[i][j] << " " ;
//		cerr << endl;
//	}
	forn(i, n)
		col[i] = -1;
	go(0, 0);
	cout << res << endl;
	forn(i, n)
		cout << ans[i]+1 << " ";
	cout << endl;
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tst;
	scanf("%d", &tst);
	for (int i = 0; i < tst; i++){
		printf("Case #%d: ", i + 1);
		solve();
	}

	return 0;
}