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
#define X first
#define Y second
#define pb push_back
#define sz size()

typedef long long i64;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

const int MaxRC = 16;
const int MaxN = 5;
const int dir_c = 4;
const int dc[4] = {+1, -1, 0, 0};
const int dr[4] = {0, 0, +1, -1};

struct State
{
	int N, pos[MaxN];
	State() : N(0) {}
	void add(int x) { pos[N++] = x; }
	void sort() { std::sort(pos, pos+N); }
};

inline bool operator==(const State& a, const State& b)
{
	REP(i, a.N)
		if (a.pos[i] != b.pos[i])
			return false;
	return true;
}

inline bool operator<(const State& a, const State& b)
{
	REP(i, a.N)
		if (a.pos[i] != b.pos[i])
			return a.pos[i] < b.pos[i];
	return false;
}

int R, C;
char lab[MaxRC][MaxRC];
queue< pair<State, int> > Q;
set<State> processed;

void push(const State& s, int len)
{
	if (processed.count(s))
		return;
	processed.insert(s);
	Q.push( make_pair(s, len) );
}

inline int pack(int r, int c) { return r*C + c; }
inline void unpack(int s, int &r, int &c) { c = s%C, r = s/C; }

bool is_stable(const State& s)
{
	bool connected[MaxN][MaxN];
	int rr[MaxN], cc[MaxN];
	REP(i, s.N)
		unpack(s.pos[i], rr[i], cc[i]);

	REP(i, s.N) REP(j, s.N)
		connected[i][j] = (abs(rr[i]-rr[j]) + abs(cc[i]-cc[j]) <= 1);
	REP(k, s.N) REP(i, s.N) REP(j, s.N)
		connected[i][j] |= connected[i][k] && connected[k][j];

	REP(i, s.N) REP(j, s.N)
		if (!connected[i][j])
			return false;
	return true;
}

bool is_free(const State& s, int r, int c)
{
	if (r < 0 || r >= R || c < 0 || c >= C)
		return false;
	if (lab[r][c] == '#')
		return false;

	int ind = pack(r, c);
	REP(i, s.N)
		if (s.pos[i] == ind)
			return false;

	return true;
}

int solve()
{
	scanf("%d %d\n", &R, &C);
	REP(i, R)
		gets(lab[i]);

	State start, finish;
	REP(r, R) REP(c, C) {
		int ind = pack(r, c);
		if (lab[r][c] == 'o' || lab[r][c] == 'w')
			start.add(ind);
		if (lab[r][c] == 'x' || lab[r][c] == 'w')
			finish.add(ind);
	}
	start.sort();
	finish.sort();

	processed.clear();
	while (!Q.empty()) Q.pop();

	push(start, 0);
	while (!Q.empty()) {
		State s = Q.front().first;
		int len = Q.front().second;
		Q.pop();

		if (s == finish)
			return len;

		bool orig_stable = is_stable(s);
		REP(i, s.N) {
			int r, c;
			unpack(s.pos[i], r, c);
			REP(j, dir_c)
				if (is_free(s, r-dr[j], c-dc[j]) &&
					is_free(s, r+dr[j], c+dc[j])) {
						State sNext = s;
						sNext.pos[i] = pack(r+dr[j], c+dc[j]);
						sNext.sort();
						if (!orig_stable) {
							if (is_stable(sNext))
								push(sNext, len+1);
						} else
							push(sNext, len+1);
				}
		}
	}

	return -1;
}

int main()
{
	// freopen("input.txt", "r", stdin);

	int n_test;
	scanf("%d\n", &n_test);
	REP(i_test, n_test) {
		printf("Case #%d: %d\n", i_test+1, solve());
		fflush(stdout);
	}

	return 0;
}
