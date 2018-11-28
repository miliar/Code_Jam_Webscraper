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

// BEGIN CUT HERE
#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

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
// END CUT HERE

inline PII operator + (const PII &a, const PII &b) { return PII(a.X+b.X, a.Y+b.Y); }

const int Max = 6010;

int Left[Max], Right[Max], Top[Max], Bottom[Max];

inline void turnLeft(PII &dir)
{
	if (dir.Y == +1) {
		dir = PII(-1, 0);
	} else
	if (dir.X == -1) {
		dir = PII(0, -1);
	} else
	if (dir.Y == -1) {
		dir = PII(+1, 0);
	} else
	if (dir.X == +1) {
		dir = PII(0, +1);
	}
}

inline void turnRight(PII &dir)
{
	if (dir.Y == +1) {
		dir = PII(+1, 0);
	} else
	if (dir.X == +1) {
		dir = PII(0, -1);
	} else
	if (dir.Y == -1) {
		dir = PII(-1, 0);
	} else
	if (dir.X == -1) {
		dir = PII(0, +1);
	}
}

int initialArea;

inline void edge(const PII &a, const PII &b)
{
	if (a.X == b.X) {
		int y = min(a.Y, b.Y);
		Left[y] = min(a.X, Left[y]);
		Right[y] = max(a.X, Right[y]);
	} else {
		int x = min(a.X, b.X);
		Top[x] = max(Top[x], a.Y);
		Bottom[x] = min(Bottom[x], a.Y);
		initialArea += (a.X - b.X)*a.Y;
	}
}

inline bool inPacket(int x, int y) {
	return ((Bottom[x] <= y) && (y < Top[x])) || ((Left[y] <= x) && (x < Right[y]));
}

int solve()
{
	REP(i, Max) {
		Left[i] = Bottom[i] = INF;
		Right[i] = Top[i] = -INF;
	}

	initialArea = 0;
	PII p(Max/2, Max/2), dir(0, +1);
	int T;
	cin >> T;
	REP(i, T) {
		string S;
		int K;
		cin >> S >> K;
		REP(j, K) REP(k, S.sz) {
			if (S[k] == 'L')
				turnLeft(dir);
			if (S[k] == 'R')
				turnRight(dir);
			if (S[k] == 'F') {
				PII pN = p+dir;
				edge(p, pN);
				p = pN;
			}
		}
	}

	initialArea = abs(initialArea);
	int L = INF, R = -INF, B = INF;
	T = -INF;
	REP(x, Max)
		if (Top[x] > Bottom[x]) {
			L = min(x, L);
			R = max(x, R);
		}
	REP(y, Max)
		if (Right[y] > Left[y]) {
			B = min(y, B);
			T = max(y, T);
		}

	int areaWithPacket = 0;
	FOR(x, L, R+1) {
		areaWithPacket += Top[x]-Bottom[x];
		FOR(y, B, Bottom[x])
			if (inPacket(x, y))
				areaWithPacket++;
		FOR(y, Top[x], T+1)
			if (inPacket(x, y))
				areaWithPacket++;
	}

	return areaWithPacket - initialArea;
}

int main()
{
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
	int nTest;
	scanf("%d", &nTest);
	for (int iTest = 1; iTest <= nTest; iTest++)
		cout << "Case #" << iTest << ": " << solve() << endl;
	return 0;
}
