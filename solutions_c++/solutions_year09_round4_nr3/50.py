#include <iomanip>
#include <algorithm>
#include <numeric>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <complex>
#include <cassert>
#include <bitset>
using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define decl(v, c) typeof(c) v = c
#define forall(i, c) for(decl(i, c.begin()); i!=c.end(); ++i)
#define dforall(i, c) for(decl(i, c.rbegin()); i!=c.rend(); ++i)
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define D(a) cout << #a << "=" << a << endl;
#define pb push_back
#define mp make_pair

typedef long long int tint;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<tint> vt;
typedef vector<vt> vvt;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

#define MAXN 204

vi next[MAXN];
int M,pre[MAXN];
bool vis[MAXN];

void initGraph(int M, int N) {
	::M = M;
	forn(i,M) next[i].clear();
	forn(i,N) pre[i] = -1;
}

void addEdge(int u, int v) {
	next[u].pb(v);
}

bool augment(int u) {
	if (u == -1) return true;
	if (vis[u]) return false;
	vis[u] = true;
	forall(it,next[u]) {
		int v = *it;
		if (augment(pre[v])) {
			pre[v] = u;
			return true;
		}
	}
	return false;
}

int matching() {
	int res = 0;
	forn(u,M) {
		forn(v,M) vis[v] = false;
		res += augment(u);
	}
	return res;
}


int n,k, chart[MAXN][MAXN];

bool below(int x, int y) {
	forn(i,k) if (chart[x][i] >= chart[y][i]) return false;
	return true;
}

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int ncas; cin >> ncas;
	forsn(cas,1,ncas+1) {
		cin >> n >> k;
		forn(i,n) forn(j,k) cin >> chart[i][j];
		
		initGraph(n,n);
		forn(i,n) forn(j,n) if (below(i,j)) addEdge(i,j);
		cout << "Case #" << cas << ": " << n-matching() << endl;
	}
}
