#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>

#include <cstdarg>

using namespace std;

#define DBG2 0

#define clr(a) memset(a, 0, sizeof(a))
#define fill(a, b) memset(a, b, sizeof(a))

void dbg(char * fmt, ...)
{
#ifdef DBG1
#if	DBG2
	FILE * file = stdout;

	va_list args;
	va_start(args, fmt);
	vfprintf(file, fmt, args);
	va_end(args);

	fflush(file);
#endif
#endif
}

typedef long long ll;
typedef unsigned long long ull;
typedef std::pair<int, int> pii;

const int INF = 1 << 25;

struct Distance {
	int dist, count;

	Distance () {}
	Distance(int _d, int _c) : dist(_d), count(_c) {}

	bool operator < (const Distance & d) const
	{
		if (dist != d.dist)
			return dist < d.dist;
		return count > d.count;
	}
};

const int N = 1000;

Distance d[N][N];
bool used[N][N];
vector <int> ed[N];

int getNewV(int v1, int v2, int v3)
{
	vector <int> p = ed[v1];
	for (int i = 0; i < int(ed[v2].size()); ++i)
		p.push_back(ed[v2][i]);
	p.push_back(v1);
	p.push_back(v2);
	sort(p.begin(), p.end());

	int res = 0;
	for (int i = 0; i < int(ed[v3].size()); ++i)
		if (!binary_search(p.begin(), p.end(), ed[v3][i]))
			++res;
	return res;	
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen(".in", "r", stdin);
	freopen(".out", "w", stdout);
#endif

	int tt;
	scanf("%d", &tt);
	for (int ii = 1; ii <= tt; ++ii)
	{
		int n, m;
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i)
			ed[i].clear();
		for (int i = 0; i < m; ++i)
		{
			int u, v;
			scanf("%d,%d", &u, &v);
			ed[u].push_back(v);
			ed[v].push_back(u);
		}
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j)
			{
				d[i][j] = Distance(INF, 0);
				used[i][j] = false;
			}
		d[0][0] = Distance(0, int(ed[0].size()));
		Distance res(INF, 0);
		for (int i = 0; i < n * n; ++i)
		{
			int bestJ = -1, bestK = -1;
			for (int j = 0; j < n; ++j)
				for (int k = 0; k < n; ++k)
				{
					if (!used[j][k] && (bestJ == -1 || d[j][k] < d[bestJ][bestK]))
						bestJ = j, bestK = k;
				}
			if (bestJ == -1 || d[bestJ][bestK].dist == INF)
				break;
			used[bestJ][bestK] = true;
			for (int j = 0; j < int(ed[bestK].size()); ++j)
			{
				int v = ed[bestK][j];
				Distance cur(d[bestJ][bestK].dist + 1, d[bestJ][bestK].count - 1 + getNewV(bestJ, bestK, v));
				if (cur < d[bestK][v])
				{
					d[bestK][v] = cur;
					dbg("%d %d| %d\n", bestK, v, cur.dist);
					cur = d[bestJ][bestK];
					if (v == 1 && cur < res)
						res = cur;
				}
			}
		}

		printf("Case #%d: %d %d\n", ii, res.dist, res.count);
	}


	return 0;
}
