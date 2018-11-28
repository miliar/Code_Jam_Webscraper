#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std; 

#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }

const int INF = 1<<29;
typedef long long ll;

inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return n & two(b); }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
inline int ones(int n) { int res = 0; while(n && ++res) n-=n&(-n); return res; }

template<class T> void chmax(T & a, const T & b) { a = max(a, b); }
template<class T> void chmin(T & a, const T & b) { a = min(a, b); }
///////////////////////////////////////////////////////////////////////////////////////////////////////////////

const int dx[] = {0,1,1,0,-1,-1},
	      dy[] = {1,1,0,-1,-1,0};

const int MAX = 6001;
int S, M, area;
pair<int, int> in[10001];

inline bool check(int x, int y)
{
	return x >= 0 && x < 2*S-1 && y >= 0 && y < 2*S-1 && abs(x-y) < S;
}

int on_edge[MAX][MAX], on_corner[MAX][MAX], used[MAX][MAX], parent[MAX*MAX], sz[MAX*MAX];
int get(int n) { return parent[n] = (n == parent[n] ? n : get(parent[n])); }
inline int get_index(int x, int y) { return x*2*S+y; }

int get_bridge()
{
	REP(i,S*S*4)
	{
		parent[i] = i;
		sz[i] = 0;
	}
	REP(x, 2*S) REP(y, 2*S) used[x][y] = 0;
	REP(i, M)
	{
		int x = in[i].first, y = in[i].second, index = get_index(x, y), p1 = index;
		sz[index] = on_corner[x][y];
		used[x][y] = 1;
		REP(d, 6)
		{
			int xx = x+dx[d], yy = y+dy[d], index2 = get_index(xx, yy);
			if (!check(xx, yy) || !used[xx][yy]) continue;
			int p2 = get(index2);
			if (p1 == p2) continue;
			parent[p2] = p1;
			sz[p1] |= sz[p2];
		}
		if (ones(sz[p1]) >= 2) return i+1;
	}
	return INF;
}

int get_fork()
{
	REP(i,S*S*4)
	{
		parent[i] = i;
		sz[i] = 0;
	}
	REP(x, 2*S) REP(y, 2*S) used[x][y] = 0;
	REP(i, M)
	{
		int x = in[i].first, y = in[i].second, index = get_index(x, y), p1 = index;
		sz[index] = on_edge[x][y];
		used[x][y] = 1;
		REP(d, 6)
		{
			int xx = x+dx[d], yy = y+dy[d], index2 = get_index(xx, yy);
			if (!check(xx, yy) || !used[xx][yy]) continue;
			int p2 = get(index2);
			if (p1 == p2) continue;
			parent[p2] = p1;
			sz[p1] |= sz[p2];
		}
		if (ones(sz[p1]) >= 3) return i+1;
	}
	return INF;
}

int get_ring()
{
	int sindex = 4*S*S-1;

	REP(i,S*S*4) parent[i] = i;
	REP(x, 2*S) REP(y, 2*S) used[x][y] = 0;
	REP(i, M)
	{
		int x = in[i].first, y = in[i].second;
		used[x][y] = 1;
	}

	int comps = area-M+1;
	int result = INF;
	REP(x, 2*S-1) REP(y, 2*S-1)
	{
		if (!check(x, y) || used[x][y]) continue;

		int index = get_index(x, y), p1 = get(index);
		REP(d, 6)
		{
			int xx = x+dx[d], yy = y+dy[d], index2 = get_index(xx, yy), p2;
			if (check(xx, yy) && used[xx][yy]) continue;
			if (check(xx, yy)) p2 = get(index2);
			else p2 = get(sindex);

			if (p1 == p2) continue;
			--comps;
			parent[p2] = p1;
		}
	}
	if (comps > 1) result = M;
	FORD(i, M-1, 0)
	{
		int x = in[i].first, y = in[i].second, index = get_index(x, y), p1 = get(index);
		used[x][y] = 0;
		++comps;

		REP(d, 6)
		{
			int xx = x+dx[d], yy = y+dy[d], index2 = get_index(xx, yy), p2;
			if (check(xx, yy) && used[xx][yy]) continue;
			if (check(xx, yy)) p2 = get(index2);
			else p2 = get(sindex);

			if (p1 == p2) continue;
			--comps;
			parent[p2] = p1;
		}
		if (comps > 1) result = i;
	}
	return result;
}

void Solve(int tc)
{
	scanf("%d%d", &S, &M);
	REP(i, M)
	{
		scanf("%d%d", &in[i].first, &in[i].second);
		--in[i].first;
		--in[i].second;
	}
	area = 0;
	REP(x, 2*S) REP(y, 2*S)
	{
		on_edge[x][y] = on_corner[x][y] = 0;
		if (check(x, y)) ++area;
	}


	// init edges / corners
	int x = 0, y = 0;
	REP(d, 6)
	{
		on_corner[x][y] = two(d);
		x += dx[d];
		y += dy[d];
		REP(i, S-2)
		{
			on_edge[x][y] = two(d);
			x += dx[d];
			y += dy[d];
		}
	}

	printf("Case #%d: ", tc);
	int b = get_bridge(), f = get_fork(), r = get_ring();
	int best = min(b, min(f, r));
	if (best == INF) printf("none\n");
	else if (best == b && best == f && best == r)
		printf("bridge-fork-ring in move %d\n", best);
	else if (best == b && best == f)
		printf("bridge-fork in move %d\n", best);
	else if (best == b && best == r)
		printf("bridge-ring in move %d\n", best);
	else if (best == f && best == r)
		printf("fork-ring in move %d\n", best);
	else if (best == b)
		printf("bridge in move %d\n", best);
	else if (best == f)
		printf("fork in move %d\n", best);
	else if (best == r)
		printf("ring in move %d\n", best);
}

int main()
{
	int T;
	scanf("%d\n", &T);
	FOR(tc,1,T) Solve(tc);

	return 0;
}
