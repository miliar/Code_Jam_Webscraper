#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)

#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())

#define INF 1000000000
#define R first
#define C second
#define pb push_back
#define sz size()

typedef long long i64;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

const int Max = 64;

int NR, NC, NF;
string tbl[Max];

string subtr(int r, int i, int j)
{
	string level(tbl[r]);
	for (int x = i; x <= j; x++)
		level[x] = '.';
	return level;
}

struct Key
{
	int row, col, fall;
	string level;

	Key(int r, int c, string lvl, int f = 1) : row(r), col(c), fall(f), level(lvl) {}
};

inline bool operator < (const Key &a, const Key &b) { return false; }
/*
{
	if (a.row != b.row) return a.row < b.row;
	if (a.col != b.col) return a.col < b.col;
	if (a.fall != b.fall) return a.fall < b.fall;
	return a.level < b.level;
}
*/

typedef pair<PII, string> KKey;

void solve()
{
	scanf("%d %d %d\n", &NR, &NC, &NF);
	REP(i, NR) {
		static char stg[1024];
		gets(stg);
		tbl[i] = stg;
	}

	priority_queue< pair<int, Key> > Q;
	set<KKey> checked;

	Q.push( make_pair(0, Key(0, 0, tbl[0])) );
	
	int ans = INF;
	while (!Q.empty()) {
		Key key = Q.top().second;
		int dist = -Q.top().first;
		Q.pop();

		if (key.fall > NF) continue;
		if (key.row == NR-1) {
			ans = min(ans, dist);
			continue;
		}

		if (tbl[key.row+1][key.col] == '.') {
			Q.push( make_pair(-dist, Key(key.row+1, key.col, tbl[key.row+1], key.fall+1)) );
			continue;
		}

		KKey kkey(make_pair(key.row, key.col), key.level);
		if (checked.count(kkey))
			continue;
		checked.insert(kkey);

		int left = key.col, right = key.col;
		int rr = key.row+1;
		while (left > 0 && key.level[left-1] == '.' && tbl[rr][left-1] == '#')
			left--;
		while (right < NC-1 && key.level[right+1] == '.' && tbl[rr][right+1] == '#')
			right++;

		// Just fall left
		if (left > 0 && key.level[left-1] == '.' && tbl[key.row+1][left-1] == '.')
			Q.push( make_pair(-dist, Key(key.row+1, left-1, tbl[key.row+1])) );

		// Just fall right
		if (right < NC-1 && key.level[right+1] == '.' && tbl[key.row+1][right+1] == '.')
			Q.push( make_pair(-dist, Key(key.row+1, right+1, tbl[key.row+1])) );

		// Dig [i, j], fall j
		FOR(i, left, right)
			FOR(j, i, right)
				Q.push( make_pair(-dist-(j-i+1), Key(key.row+1, j, subtr(key.row+1, i, j))));

		// Dig [i, j], fall i
		FOR(i, left+1, right+1)
			FOR(j, i, right+1)
				Q.push( make_pair(-dist-(j-i+1), Key(key.row+1, i, subtr(key.row+1, i, j))));
	}

	if (ans >= INF)
		printf("No\n"); else
		printf("Yes %d\n", ans);
}

int main()
{
//	freopen("input.txt", "r", stdin);

	int n_test;
	scanf("%d\n", &n_test);
	REP(i_test, n_test) {
		printf("Case #%d: ", i_test+1);
		solve();
	}

	return 0;
}
