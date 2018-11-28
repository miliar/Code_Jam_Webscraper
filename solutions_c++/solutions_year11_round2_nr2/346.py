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

int pts[1111111];

int compare (const void * a, const void * b)
{
	return ( *(int*)a - *(int*)b );
}

int main () {
	int T;
	scanf("%d", &T);
	FORU(itr, 1, T) {
		int C, D;
		scanf("%d %d", &C, &D);

		int N = 0;
		FOR(i, C) {
			int p, v;
			scanf("%d %d", &p, &v);
			FOR(j, v)
				pts[N++] = p;
		}
		qsort(pts, N, sizeof(int), compare);
//		FOR(i, N)
//			printf("%d ", pts[i]);
//		printf("\n");

		double out = 0;
		FOR(i, N)
			FORU(j, i+1, N-1) {
				int goal = D * (j - i) - (pts[j] - pts[i]);
				out = max(out, .5 * goal);
			}

		printf("Case #%d: %f\n", itr, out);
	}
	return 0;
}
