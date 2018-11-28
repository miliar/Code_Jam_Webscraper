#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <queue>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define all(c) (c).begin(), (c).end()
#define pb push_back
#define mp make_pair

typedef long long int tint;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<string> vs;
typedef pair<int,int> ii;
typedef vector<ii> vii;

const int maxn = 1000 + 100;
tint g[maxn];
bool vis[maxn];
int next[maxn];
tint pay[maxn];
tint r, k;
int n;

void calc(int u){
	int pos = u; tint tmp = 0;
	if(g[u]>k){ pay[u] = 0; next[u] = u; return ; }
	while(tmp + g[pos] <= k){
		tmp += g[pos];
		pos++; if(pos == n) pos = 0;
		if(pos == u) break;
	}
	next[u] = pos; pay[u] = tmp;
}

tint res;
int pasos[maxn];
tint sp[maxn];

int dfs(int u, int np){
	if(np == r) return 0;

	pasos[u] = np; vis[u] = true;
	int v = next[u];

//	cout << u << " sig " << v << " " << sp[u] << endl;
	if(vis[v]){
		int lc = (np - pasos[v]+1);
		tint pc = (sp[u] + pay[u] - sp[v]);
//		cout << "EA " << lc << " " << pc << " " << ((r-pasos[v])/lc) * pc << endl;
		res += (max(0LL, (r-pasos[v]-lc))/lc) * pc;

		r = (r-pasos[v])%lc;
//		cout << r << endl;
		int pos = v, ea = 0;
		while(ea<r){ res += pay[pos]; pos = next[pos]; ea++; }
	}else{
		sp[v] = sp[u] + pay[u];
		dfs(v, np+1);
	}
	res += pay[u];
}

void init(){
	memset(vis, false, sizeof(vis));
	forn(i, n){
		sp[i] = 0;
		pasos[i] = 0;
	}
	res = 0;
}

int main(){
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int NC; cin >> NC;
	forn(nc, NC){
		cin >> r >> k >> n;
		init();

		forn(i, n) cin >> g[i];

		forn(i, n) calc(i);
//		forn(i, n) cout << i << " " << pay[i] << " " << next[i] << endl;

		dfs(0, 0);

		cout << "Case #" << nc+1 << ": " << res << endl;

	}

	return 0;
}
