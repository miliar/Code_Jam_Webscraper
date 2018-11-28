#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <ctime>
#include <map>
#include <utility>


using namespace std;

#define double long double

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define forv(i, v) forn(i, v.size())
#define ensure(condition) if (!(condition)) fprintf(stderr, "failed: %s\n", #condition), exit(239)
#define x first
#define y second
#define pb push_back

int INF = 1000000000;

const int MAXN = 300;


struct edge {
	int u, v, cap, cost, f;
};

edge e[MAXN * MAXN];
int m = 0;

vector<int> g[MAXN];

inline void add(int u, int v, int pp, int cc) {
	edge e1 = {u, v, pp, cc, 0};
	g[u].pb(m);
	e[m++] = e1;

	edge e2 = {v, u, 0, -cc, 0};
	g[v].pb(m);
	e[m++] = e2;
}

int n;

int p[MAXN];
int d[MAXN];
int us[MAXN];
int q[MAXN * MAXN * 5], qh, qt;
int s, t;

int res = 0;


bool flow() {
	memset(us, 0, sizeof us);
	for(int i = 0; i < n + n + 2; i++)
		d[i] = INF;
	qh = qt = 0;
	q[0] = s;
	d[s] = 0;
	us[s] = 1;
	int steps = 0;
	while(qh <= qt) {
		//if (us[t] && ++steps >= 10000 || steps >= 50000)
		//	break;
		int v = q[qh++];
		us[v] = 0;
		for(int i = 0; i < (int)g[v].size(); i++){
			edge ed = e[g[v][i]];
			if (ed.f < ed.cap) {
				int u = ed.v, dst = d[v] + ed.cost;
				if (d[u] > dst) {
					d[u] = dst;
					p[u] = g[v][i];
					if (us[u] == 0) {
						us[u] = 1;
						q[++qt] = u;
						swap(q[qt], q[qh]);
					}
				}
			}
		}
	}
	if (d[t] > 0){
		return false;
	}
	res++;

	int minf = INF;
	for(int v = t; v != s; v = e[p[v]].u) {
		minf = min(minf, e[p[v]].cap - e[p[v]].f);
	}
	for(int v = t; v != s; v = e[p[v]].u) {
		e[p[v]].f += minf;
		e[p[v] ^ 1].f -= minf;
	}
	return true;
}

int k;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tu;
	cin >> tu;
	forn(tt, tu) {
		cin >> n >> k;
		vector<int> a[101];
		forn(i, n) {
			a[i].clear();
			forn(j, k) {
				int x;
				cin >> x;
				a[i].pb(x);
			}
		}
		sort(a, a + n);

		m = 0;
		forn(i, n + n + 2)
			g[i].clear();
		
		forn(i, n) {
			for(int j = i + 1; j < n; j++) {
				bool inter = 0;
				forn(l, k - 1) {
					if (a[i][l] > a[j][l] && a[i][l + 1] < a[j][l + 1] || 
						a[i][l] < a[j][l] && a[i][l + 1] > a[j][l + 1] || 
				    	a[i][l] == a[j][l] && a[i][l + 1] == a[j][l + 1] ||
						(l < k - 2 && (a[i][l] > a[j][l] && a[i][l + 2] < a[j][l + 2] || 
						a[i][l] < a[j][l] && a[i][l + 2] > a[j][l + 2]) && 
				    	a[i][l + 1] == a[j][l + 1])
					) {
							inter = 1;
							break;
					}
				}
				forn(l, k) {
					if (a[i][l] == a[j][l])
						inter = 1;
				}
				if (!inter) {
					add(i * 2 + 1, j * 2, 1, -1);
				}
			}
		}
		s = n + n, t = s + 1;
		

		forn(i, n) {
			add(s, i * 2, 1, 0);
			add(i * 2 + 1, t, 1, 0);
			add(i* 2, i * 2 + 1, 1, 0);
		}
		res = 0;
		while(flow());
		printf("Case #%d: %d\n", tt + 1, res);
	}


	
	return 0;
}