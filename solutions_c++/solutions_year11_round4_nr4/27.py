#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#include <algorithm>
#include <set>
#include <vector>
#define clr(a) memset(a, 0, sizeof(a))

typedef long long ll;
typedef std::pair<int, int> pii;
#define DEBUG 0

void dbg(const char * fmt, ...)
{
#if DEBUG
	va_list args;
	va_start(args, fmt);
	vfprintf(stdout, fmt, args);
	va_end(args);
#endif
}

int adjmat[512][512];
int deg[512];
int dist[512];
int edist[512];
int q[512];


void bfs(int first, int d[512], int n)
{
	memset(d, -1, 512 * sizeof(int));
	d[first] = 0;
	int r = 0;
	q[r++] = first;
	for(int i = 0; i < r; i++)
	{
		int v = q[i];
	//	dbg("-> %d %d\n", v, d[v]);
		for(int j = 0; j < n; j++)
			if (d[j] == -1 && adjmat[v][j])
			{
				d[j] = d[v] + 1;
				q[r++] = j;
			}
	}
}



int bits[1<<16];
pii v[512];
int dp[512][512];

class vec
{
public:
	unsigned int ar[25];
	vec()
	{
		clr(ar);
	}
	void add(int pos)
	{
		ar[pos/16] |= (1u << (pos % 16));
	}
	int len()
	{
		int ans = 0;
		for(int i = 0; i < 25; i++)
			ans += bits[ar[i]];
		return ans;
	}
	vec operator & (const vec & v) const
	{
		vec ans;
		for(int i = 0; i < 25; i++)
			ans.ar[i] = ar[i] & v.ar[i];
		return ans;
	}
} ad[512];



void solve(int test_case)
{
	printf("Case #%d: ", test_case);
	int n,m;
	scanf("%d%d", &n, &m);
	clr(adjmat);
	clr(deg);
	clr(dist); clr(edist);
	clr(dp);
	for(int i = 0; i < n; i++)
		clr(ad[i].ar);

	for(int i = 0; i < m; i++)
	{
		int a,b;
		scanf("%d,%d", &a, &b);
		adjmat[a][b] = adjmat[b][a] = 1;
		deg[a] ++; deg[b] ++;
		ad[a].add(b); ad[b].add(a);		
	}
	bfs(0, dist, n);
	bfs(1, edist, n);
	int len = dist[1], ans = 0;
	for(int i = 0; i < n; i++)
		v[i] = pii(dist[i], i);
	std::sort(v, v + n);
	int pos = 0;
	dp[0][0] = ad[0].len();
	for(int i = 0; i < n; i++)
		dbg("%d ", dist[i]);
	dbg("\n");
	while(v[pos].first < 1)
		pos++;
	while(v[pos].first == 1)
	{
		int u = v[pos].second;
		dp[0][u] = ad[u].len() + ad[0].len() - (ad[u] & ad[0]).len();
		dbg("dp[%d][%d] = %d\n", 0, u, dp[0][u]);
		if (dist[1] == 2 && adjmat[u][1])
			ans = std::max(ans, dp[0][u]);
		pos ++;
	}
	while(v[pos].first < dist[1])
	{
		int u = v[pos].second;
		for(int i = 0; i < n; i++)
		{
			if (!adjmat[i][u] || dist[i] != dist[u] - 1)
				continue;
			for(int j = 0; j < n; j++)
			{
				if (!adjmat[j][i] || dist[j] != dist[i] - 1)
					continue;
				dp[i][u] = std::max(dp[i][u], dp[j][i] + 
						ad[u].len() - (ad[u] & ad[i]).len() - (ad[u] & ad[j]).len() + (ad[u] & ad[i] & ad[j]).len());
			}
			if (adjmat[u][1])
				ans = std::max(ans, dp[i][u]);
			dbg("dp[%d][%d] = %d\n", i, u, dp[i][u]);
		}
		pos ++;
	}
	if (len == 1)
		ans = dp[0][0] + 1;
	printf("%d %d\n", len - 1, ans - len);
}

int main()
{
	bits[0] = 0;
	for(int i = 1; i < (1<<16); i++)
		bits[i] = i % 2 + bits[i/2];

	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
