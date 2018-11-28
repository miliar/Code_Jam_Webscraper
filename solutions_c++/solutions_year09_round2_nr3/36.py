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
#include<ctime>

using namespace std;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)

#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())

#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define sz size()

typedef long long i64;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

const int MAX = 20;
const int MIN_SUM = -435;
const int MAX_SUM = +765;
const int RNG = MAX_SUM-MIN_SUM+1;

int W, Queries;
char square[MAX][MAX];
string best[MAX][MAX][RNG];
int itest[MAX][MAX][RNG];

inline bool is_inside(int x, int y)
{
	return (x >= 0) && (x < W) && (y >= 0) && (y < W);
}

struct Key
{
	short x, y, sum;
};

int cur, prev;
queue<Key> Q[2];

void relax(string &a, const string &b)
{
	if (a.empty()) {
		a = b; return;
	}

	if (a.size() > b.size()) {
		a = b; return;
	}

	if (a.size() == b.size() && a > b) {
		a = b; return;
	}
}

void push_Q(int x, int y, int sum, const string &s, int test)
{
	if (sum < MIN_SUM || sum > MAX_SUM)
		return;

	if (itest[x][y][sum-MIN_SUM] < test) {
		itest[x][y][sum-MIN_SUM] = test;
		 best[x][y][sum-MIN_SUM] = s;

		Key key;
		key.x = x;
		key.y = y;
		key.sum = sum;
		Q[cur].push(key);
		return;
	}

	relax(best[x][y][sum-MIN_SUM], s);
}

int dx[4] = {+1, -1, 0, 0};
int dy[4] = {0, 0, +1, -1};

void solve(int test)
{
	scanf("%d %d\n", &W, &Queries);
	REP(i, W)
		gets(square[i]);

	cur = 0;
	while (!Q[cur].empty())
		Q[cur].pop();

	REP(x, W) REP(y, W)
		if (isdigit(square[y][x]))
			push_Q(x, y, square[y][x]-'0', string("")+square[y][x], test);

	int total = 0;
	prev = cur;
	while (true) {
		if (Q[prev].empty()) {
			prev = cur;
			if (Q[prev].empty())
				break;
		}
		cur = prev ^ 1;

		Key key = Q[prev].front();
		Q[prev].pop();

//		if (total % 1000 == 0)
//			printf("%d %d %d -- %d\n", key.x, key.y, key.sum, total);
//		 ++total;

		REP(d1, 4) if (is_inside(key.x+dx[d1], key.y+dy[d1])) {
			int x1 = key.x+dx[d1], y1 = key.y+dy[d1];
			int sgn = (square[y1][x1] == '-' ? -1 : +1);

			REP(d2, 4) if (is_inside(x1+dx[d2], y1+dy[d2])) {
				int x2 = x1+dx[d2], y2 = y1+dy[d2];
				int new_sum = key.sum + sgn*(square[y2][x2] - '0');

				push_Q(x2, y2, new_sum, 
				       (best[key.x][key.y][key.sum-MIN_SUM] + square[y1][x1]) + square[y2][x2],
				       test);
			}
		}
	}

	string ans[MAX_SUM+1];
	REP(x, W) REP(y, W) REP(sum, MAX_SUM+1)
		if (itest[x][y][sum - MIN_SUM] == test)
			relax(ans[sum], best[x][y][sum - MIN_SUM]);

	REP(i, Queries) {
		int qq;
		scanf("%d", &qq);
		puts(ans[qq].c_str());
	}
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	memset(itest, 0, sizeof(itest));

	int n_test;
	scanf("%d\n", &n_test);
	REP(i_test, n_test) {
		printf("Case #%d:\n", i_test+1);
		solve(i_test+1);
		fprintf(stderr, "test #%d clock=%d\n", i_test+1, (int)clock());
	}

	return 0;
}
