#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <sys/time.h>
#include <sys/stat.h>
#include <fstream>

using namespace std;

typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
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
#define INF 1000000000

static inline double getTime () {
   timeval tv;
   gettimeofday(&tv, 0);
   return tv.tv_sec + tv.tv_usec * 1e-6;
}

#define WIN 0
#define LOSE 1
#define NP 2

int res[111][111];
double wp[111];
double owp[111];
double oowp[111];

int main () {
	int T;
	scanf("%d", &T);
	FORU(itr, 1, T) {
		int N;
		scanf("%d", &N);
		FOR(i, N) {
			scanf("\n");
			FOR(j, N) {
				char c;
				scanf("%c", &c);
				if (c == '1')
					res[i][j] = WIN;
				else if (c == '0')
					res[i][j] = LOSE;
				else
					res[i][j] = NP;
			}
//			scanf(" ");
		}

		FOR(i, N) {
			int wins = 0, loses = 0;
			FOR(j, N) {
				if (res[i][j] == WIN)
					++wins;
				else if (res[i][j] == LOSE)
					++loses;
			}
			wp[i] = 1.0 * wins / (wins + loses);
		}

		FOR(i, N) {
			double sum = 0;
			int cnt = 0;
			FOR(j, N) {
				if (res[i][j] == NP)
					continue;
				int wins = 0, loses = 0;
				FOR(k, N) {
					if (i == k)
						continue;
					if (res[j][k] == WIN)
						++wins;
					else if (res[j][k] == LOSE)
						++loses;
				}
				sum += 1.0 * wins / (wins + loses);
				++cnt;
			}
			owp[i] = sum / cnt;
		}

		FOR(i, N) {
			double sum = 0;
			int cnt = 0;
			FOR(j, N) {
				if (res[i][j] == NP)
					continue;
				sum += owp[j];
				++cnt;
			}
			oowp[i] = sum / cnt;
		}

		printf("Case #%d:\n", itr);
		FOR(i, N) {
			printf("%f\n", .25*wp[i] + .5*owp[i] + .25*oowp[i]);
		}
	}
	return 0;
}
