#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <map>
#include <set>
#define LL long long
#define ldb long double
#define sqr(a) ((a) * (a))
#define nextLine() {int c = 0; while((c = getchar()) != 10 && c != EOF);}
#define debug(a) cerr << #a << " = " << a << " ";
#define debugl(a) cerr << #a << " = " << a << "\n";
const ldb eps = 1e-9;
const ldb pi = fabsl(atan2(0.0, -1.0));
const LL LINF = 1ll << 60;
const ldb LDINF = 1e42;
const int INF = 0x7f7f7f7f;
using namespace std;
#define problem "a"

int X, S, R, T, n;
int b[1000010], e[1000010], w[1000010];
int per[1000010];

void Load()
{
	cin >> X >> S >> R >> T >> n;
	for (int i = 0; i < n; i++)
	{
		scanf("%d%d%d", &b[i], &e[i], &w[i]);
		per[i] = i;
	}
}
inline bool cmp(int a, int b)
{
	return e[a] - ::b[a] > e[b] - ::b[b];
}

void Solve(int Test)
{
	cout << "Case #" << Test << ": ";
	ldb sum = 0;
	ldb XN = X;
	for (int i = 0; i < n; i++)
	{
		sum += ((ldb)e[i] - b[i]) / ((ldb)w[i] + R);
		XN -= e[i] - b[i];
	}
	sum += (ldb)XN / (ldb)R;
	if (sum < T + eps)
	{
		cout << sum << "\n";
		return;
	}
	w[n] = 0;
	b[n] = 0;
	e[n] = XN;
	per[n] = n;
	n++;
	sort(per, per + n, cmp);
	ldb result = 0;
	ldb run = 0;
	ldb ans = 0;
	for (int i = 0; i < n; i++)
	{
		int j = per[i];
		ldb L = min((ldb)e[j] - b[j], ((ldb)T - result) * ((ldb)w[j] + R));
	//	cerr << e[j] - b[j] << " " << L << " " << result << "\n";
		run += L;
		result += L / ((ldb)w[j] + R);
		ans += (e[j] - b[j] - L) / ((ldb)S + w[j]);
	}
	//cerr << "\n\n";
	cout << result + ans << "\n";
}

int first[2010], next[10000], end[100000], edges;
ldb cost[100000], cap[100000];

void addEdge(int i, int j, ldb cpc, ldb cst)
{
	next[edges] = first[i];
	first[i] = edges;
	end[edges] = j;
	cost[edges] = cst;
	cap[edges] = cpc;
	edges++;
	next[edges] = first[j];
	first[j] = edges;
	end[edges] = i;
	cost[edges] = -cst;
	cap[edges] = 0;
	edges++;
}

ldb d[2010], fi[2010];
int L[2011];
int p[2011];
int s, t;
ldb maxflow, mincost;

class comp
{
	public: 
		bool operator () (int a, int b)
		{
			return d[a] < d[b] - eps || fabsl(d[a] - d[b]) < eps && a < b;
		}
};

set <int, comp> was;

void Augment()
{
	int i = t;
	ldb cmin = 1e42;
	while (i != s)
	{
		cmin = min(cmin, cap[p[i]]);
		i = end[p[i] ^ 1];
	}
	maxflow += cmin;
	i = t;
	while (i != s)
	{
		mincost += cmin * cost[p[i]];
		cap[p[i]] -= cmin;
		cap[p[i] ^ 1] += cmin;
		i = end[p[i] ^ 1];
	}
}


bool FordBellman()
{
	int i, u;
	for (i = s; i <= t; i++)
	{
		d[i] = 1e42;
	}
	d[s] = 0;
	for (i = s; i < t; i++)
	{
		for (u = 0; u < edges; u++)
		{
			if (cap[u] == 0) continue;
			if (fabsl(d[end[u ^ 1]] - 1e42)< eps) continue;
			if (d[end[u]] < d[end[u ^ 1]] + cost[u] + eps) continue;
			d[end[u]] = d[end[u ^ 1]] + cost[u];
			p[end[u]] = u;
		}
	}
	if (fabsl(d[t] - 1e42) < eps) return 0;
	Augment();
	for (i = s; i <= t; fi[i] = d[i], i++);
	return 1;
}

bool Dijkstra()
{
	int i, u, ver;
	for (i = s; i <= t; d[i] = 1e42, i++);
	d[s] = 0;
	was.insert(s);
	while (!was.empty())
	{
		ver = *was.begin();
		was.erase(ver);
		for (u = first[ver]; u != -1; u = next[u])
		{
			if (d[end[u]] < d[ver] + cost[u] + fi[ver] - fi[end[u]] + eps || cap[u] == 0) continue;
			if (was.find(end[u]) != was.end())
				was.erase(end[u]);
			d[end[u]] = d[ver] + cost[u] + fi[ver] - fi[end[u]];
			p[end[u]] = u;
			was.insert(end[u]);
		}
	}
	if (fabsl(d[t] - 1e42) < eps) return 0;
	for (i = s; i <= t; i++) fi[i] += d[i];
	Augment();
	return 1;
}


void Solve2(int Test)
{
	cout << "Case #" << Test << ": ";
	int i;
	L[n] = X;
	for (i = 0; i < n; i++)
	{
		L[i] = e[i] - b[i];
		L[n] -= L[i];
	}
	w[n] = 0;
	n++;
	memset(first, -1, sizeof first);
	edges = 0;
	//checking
	ldb sum = 0;
	for (int i = 0; i < n; i++)
	{
		sum += (ldb)L[i] / ((ldb)R + w[i]);
	}
	if (sum < T + eps)
	{
		cout << sum << "\n";
		return;
	}
	s = 0;
	t = n + 2;
	addEdge(s, n + 1, T, 0);
	for (i = 0; i < n; i++)
	{
		addEdge(n + 1, i + 1, L[i] / ((ldb)w[i] + R), -((ldb)w[i] + R) / ((ldb)w[i] + S));
		addEdge(i + 1, t, 1e42, 0);
	}
	if (FordBellman())
	{
		while (Dijkstra());
	}
	cerr << maxflow << " " << mincost << "\n";
	ldb res = T;
	for (int i = first[n + 1]; i != -1; i = next[i])
	{
		if (end[i] >= 1 && end[i] <= n)
		{
//			cerr << end[i] << " " << cap[i ^ 1] << " " << (ldb)L[end[i]] << " " <<  cap[i ^ 1] * (w[end[i]] + R) << "\n";
			res += ((ldb)L[end[i] - 1] - cap[i ^ 1] * (w[end[i] - 1] + R)) / ((ldb) S + w[end[i] - 1]);
		}
	}
	cout << res << "\n";
}

int main()
{
	freopen(problem ".in", "rt", stdin);
	freopen(problem ".out", "wt", stdout);
	int t;
	cout << setprecision(15) << fixed;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		Load();
		Solve2(i + 1);
	}
	return 0;
}

