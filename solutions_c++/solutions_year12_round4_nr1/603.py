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

#define MAXN 10111

int compare (const void * a, const void * b) {
	return ( (*(PII*)a).first - (*(PII*)b).first );
}

int mem[MAXN][MAXN]; // [pos][held]
PII vines[MAXN];
int N, D;

bool dfs (int pos, int held) {
	if (mem[pos][held] >= 0)
		return mem[pos][held];

	int end = vines[held].first + min(vines[held].second, vines[held].first - vines[pos].first);
	if (end >= D)
		return mem[pos][held] = 1;

	FORU(i, held+1, N-1) {
		if (vines[i].first <= end) {
			if (dfs(held, i))
				return mem[pos][held] = 1;
		}
		else
			break;
	}
	return mem[pos][held] = 0;
}

int main () {
	int T;
	scanf("%d", &T);
	FOR(itr, T) {
		cerr << itr << endl;
		scanf("%d", &N);
		FOR(i, N) {
			int a, b;
			scanf("%d%d", &a, &b);
			vines[i] = MP(a, b);
		}
		scanf("%d", &D);

		PII first = vines[0];
		qsort(vines, N, sizeof(PII), compare);
//		if (N <= 5) {
//			cerr << itr << " " << D << " (" << first.first << ", " << first.second << ")" << endl;
//			FOR(i, N)
//				cerr << vines[i].first << " " << vines[i].second << endl;
//			cerr << endl;
//		}
		FOR(i, N+5)
			FOR(j, N+5)
				mem[i][j] = -1;
		int start = -1;
		FOR(i, N)
			if (vines[i].first == first.first && vines[i].second == first.second) {
				start = i;
				break;
			}

		bool out = first.first + min(first.first, first.second) >= D;
		FOR(i, N) {
			if (vines[i].first <= first.first + min(first.first, first.second) && dfs(start, i)) {
				out = true;
				break;
			}
		}

		printf("Case #%d: ", itr+1);
		if (!out)
			printf("NO\n");
		else
			printf("YES\n");
	}
}
