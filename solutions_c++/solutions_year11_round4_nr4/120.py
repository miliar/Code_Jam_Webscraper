#include <iostream>
#include <cassert>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#define nextLine() { for (int c = getchar(); c != '\n' && c != EOF; c = getchar()); }
#define sqr(a) ((a)*(a))
#define has(mask,i) (((mask) & (1<<(i))) == 0 ? false : true)
using namespace std;

#define pii pair<int,int>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
typedef long long LL;
typedef long double ldb;

const int inf = (1 << 30) - 1;
const ldb eps = 1e-9;
const ldb pi = fabs(atan2(0.0, -1.0));

const int maxv = 405;
const int maxe = 4005;
int edges = 0;
int fst[maxv];
int nxt[maxe];
int end[maxe];

inline void addEdge(int u, int v)
{
	nxt[edges] = fst[u];
	end[edges] = v;
	fst[u] = edges++;
}

int n, m;
void Load()
{
	edges = 0;
	memset(fst, -1, sizeof(fst));
	scanf("%d%d", &n, &m);
	int u, v;
	for (int i = 0; i < m; i++)
	{
		scanf("%d,%d", &u, &v);
		addEdge(u, v);
		addEdge(v, u);
	}
}

int d[maxv];
int q[maxe];
bool used[maxv];
bool col[maxv];
int bres;

void rec(int v)
{
	if (v == 1)
	{
		memset(col, false, sizeof(col));
		int cres = 0;
		for (int i = 0; i < n; i++)
		{
			if (!used[i]) continue;
			for (int j = fst[i]; j != -1; j = nxt[j])
				if (!used[end[j]] && !col[end[j]]) 
				{
					cres++;
					col[end[j]] = true;
				}	
		}
	   	bres = max(cres, bres);
		return;
	}
	used[v] = true;
	for (int j = fst[v]; j != -1; j = nxt[j])
		if (d[end[j]] == d[v] + 1)
			rec(end[j]);
	used[v] = false;
}

void Solve()
{
	memset(d, -1, sizeof(d));
	int qh = 0;
	int qt = 1;
	d[0] = 0;
	q[0] = 0;
	while (qh < qt)
	{
		int v = q[qh++];
		for (int j = fst[v]; j != -1; j = nxt[j])
			if (d[end[j]] == -1)
			{
				d[end[j]] = d[v] + 1;
				q[qt++] = end[j];
			}
	}
	memset(used, false, sizeof(used));
	bres = 0;
	rec(0);
	printf("%d %d", d[1] - 1, bres);
}

int main()
{
//	freopen("d.in", "r", stdin);
	int nt;
	scanf("%d", &nt);
	for (int tt = 1; tt <= nt; tt++)
	{ 
		Load();
		printf("Case #%d: ", tt);
		Solve();
		printf("\n");
	}	
	return 0;
}
