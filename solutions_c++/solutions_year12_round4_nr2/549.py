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

#define MAXN 2022

int N, W, L;
int r[MAXN];
double x[MAXN], y[MAXN];

bool works () {
	FOR(i, N)
		FORU(j, i+1, N-1) {
			double xd = x[i] - x[j];
			double yd = y[i] - y[j];
			if (xd * xd + yd * yd - 1e-3 < (double)(r[i] + r[j]) * (r[i] + r[j]))
				return false;
		}
	return true;
}

int main () {
//	cerr << RAND_MAX << endl;
	int T;
	scanf("%d", &T);
	FOR(itr, T) {
		scanf("%d%d%d", &N, &W, &L);
		cerr << itr << " " << N << endl;
		FOR(i, N) {
			scanf("%d", r+i);
		}

		FOR(tries, 1000000000) {
			FOR(i, N) {
				x[i] = rand() / (double)RAND_MAX * W;
				y[i] = rand() / (double)RAND_MAX * L;
			}
			if (works()) {
				cerr << tries << endl;
				break;
			}
		}

		printf("Case #%d:", itr+1);
		FOR(i, N)
			printf(" %f %f", x[i], y[i]);
		printf("\n");
	}
	return 0;
}
