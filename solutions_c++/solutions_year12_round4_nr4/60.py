#include <list>
#include <string.h>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <ext/hash_map>
#include <stdint.h>
#include <ctime>
#include <queue>
#include <sstream>
#include <sys/time.h>
#include <fstream>
#include <vector>
#include<set>

using namespace std;

typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef long long LL;
typedef unsigned char BYTE;

#define FOR(i, n) for (int i = 0; i < (n); ++i)
#define FORU(i, s, e) for (int i = (s); i <= (e); ++i)
#define FORD(i, s, e) for (int i = (s); i >= (e); --i)
#define ALL(x) x.begin(),x.end()
#define FOREACH(i, v) for(__typeof((v).begin()) i = (v).begin(); i != (v).end(); ++i)
#define SIZE(x) ((int)x.size())
#define MP make_pair
#define PB push_back
#define BIT(x, b) (((x) >> (b)) & 1)
#define SWAP(a, b, t) do {t = a; a = b; b = t;} while (0);
#define INF 1000000000
#define EPS 1e-9
#define TIME_LEFT_UNTIL(end) ((curTime=getTime()-startTime) < (end))
#define TIME_LEFT() TIME_LEFT_UNTIL(MAX_TIME)
#define INIT_TIME() startTime = getTime()

static inline double getTime () {
   timeval tv;
   gettimeofday(&tv, 0);
   return tv.tv_sec + tv.tv_usec * 1e-6;
}

#define MAXN 10
#define TO_BIT(r, c) (1LL << ((r-1) * 8 + (c-1)))

int R, C;
bool pass[MAXN][MAXN];
char in[MAXN][MAXN];
set<LL> vis;
LL goal;
LL canReach;
int reachCount;

bool dfs (LL state) {
	if (state == goal)
		return 1;
	if (state & ~canReach)
		return 0;
	if (vis.count(state))
		return 0;
	vis.insert(state);

	LL stateL = 0, stateR = 0, stateD = 0;
	FORU(r, 1, 8) {
		FORU(c, 1, 8) {
			if (state & TO_BIT(r, c)) {
				if (pass[r][c-1])
					stateL |= TO_BIT(r, c-1);
				else
					stateL |= TO_BIT(r, c);
				if (pass[r][c+1])
					stateR |= TO_BIT(r, c+1);
				else
					stateR |= TO_BIT(r, c);
				if (pass[r+1][c])
					stateD |= TO_BIT(r+1, c);
				else
					stateD |= TO_BIT(r, c);
			}
		}
	}
	if (dfs(stateL))
		return 1;
	if (dfs(stateR))
		return 1;
	if (dfs(stateD))
		return 1;
	return 0;
}

void reachable (int r, int c) {
	if (canReach & TO_BIT(r, c))
		return;
	++reachCount;
	canReach |= TO_BIT(r, c);

	if (pass[r][c-1])
		reachable(r, c-1);
	if (pass[r][c+1])
		reachable(r, c+1);
	if (pass[r-1][c])
		reachable(r-1, c);
}

int main () {
//	cerr << RAND_MAX << endl;
	int T;
	scanf("%d", &T);
	FOR(itr, T) {
		scanf("%d%d", &R, &C);
		FOR(r, R) {
			scanf("\n");
			FOR(c, C) {
				scanf("%c", &(in[r][c]));
				pass[r][c] = in[r][c] != '#';
				cerr << in[r][c];
			}
			cerr << endl;
		}

		printf("Case #%d:\n", itr+1);
		FOR(cave, 10000) {
			int cr = -1, cc = -1;
			FOR(r, R)
				FOR(c, C) {
					if (in[r][c] == cave + '0') {
						cr = r;
						cc = c;
					}
				}
			if (cr == -1)
				break;

			cerr << cr << " " << cc << endl;
			canReach = 0;
			reachCount = 0;
			reachable(cr, cc);
			printf("%d: %d ", cave, reachCount);

			vis.clear();
			goal = TO_BIT(cr, cc);
			if (dfs(canReach))
				printf("Lucky\n");
			else
				printf("Unlucky\n");
		}
	}
	return 0;
}
