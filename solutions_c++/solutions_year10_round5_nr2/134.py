#pragma comment (linker, "/STACK:64000000")
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <sstream>
#include <iostream>
#include <queue>
#include <set>
#include <map>

#define ABS(x) ((x)<0?-(x):(x))
#define SQR(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define SS stringstream
#define LL long long
#define LD long double
#define SZ(x) int(x.size())
#define ALL(x) x.begin(),x.end()
#define FOR(a,b) for(int a=0;a<b;a++)
#define DFOR(a,b) for(int a=b-1;a>=0;a--)
#define CLR(a,b) memset(a,b,sizeof(a))

using namespace std;

#define maxn 105
#define maxv 100005

#define inf 10000000000000ll

struct edge
{
	int v, w;
	edge(int v, int w) : v(v), w(w) { }
};

LL s;
int n, m;
int a[maxn];
vector<edge> e[maxv];
LL d[maxv];



void solvecase() {
	scanf("%lld%d", &s, &n);
	for (int i = 0; i < n; i++)
		scanf("%d", &a[i]);
	sort(a, a+n);
	
	m = a[n-1];
	// build a graph
	for (int i = 0; i < m; i++)
		e[i].clear();
	for (int i = 0; i < m; i++)
	{
		for (int j = 0; j+1 < n; j++)
		{
			int t = i + a[j];
			int w = 1;
			if (t >= m)
			{
				t -= m;
				w = 0;
			}
			e[i].PB(edge(t, w));
		}
	}

	// run dijkstra
	set<pair<LL, int> > S;
	for (int i = 1; i < m; i++)
	{
		d[i] = inf;
		S.insert(MP(inf, i));
		//f[i] = false;
	}
	d[0] = 0;
	S.insert(MP(0, 0));

	for (int i = 0; i < m; i++)
	{
		int cur = S.begin()->second;
		//f[cur] = true;
		S.erase(S.begin());
		if (d[cur] == inf)
			break;
		for (int i = 0; i < SZ(e[cur]); i++)
		{
			int t = d[cur] + e[cur][i].w;
			int v = e[cur][i].v;
			if (t < d[v])
			{
				S.erase(MP(d[v], v));
				d[v] = t;
				S.insert(MP(d[v], v));
			}
		}
	}

	if (d[s % m] == inf)
		printf("IMPOSSIBLE");
	else
	{
		printf("%lld", s / m + d[s % m]);
	}
}

void solve() {
	int n;
	scanf("%d\n", &n);
	FOR(i, n) {
		printf("Case #%d: ", i+1);
		solvecase();
		printf("\n");
	}
}

int main() {
	freopen("B-small-attempt0.in", "rt", stdin);
	//freopen("B-large.in", "rt", stdin);
	//freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	solve();
	return 0;
}