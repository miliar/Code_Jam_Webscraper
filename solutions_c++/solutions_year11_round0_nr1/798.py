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
#define SIGN(x) (x > 0 ? 1 : (x < 0 ? -1 : 0))

static inline double getTime () {
   timeval tv;
   gettimeofday(&tv, 0);
   return tv.tv_sec + tv.tv_usec * 1e-6;
}

#define O 0
#define B 1

int main () {
	int T;
	scanf("%d", &T);
	FORU(itr, 1, T) {
		int N;
		scanf("%d", &N);

		VI seq, orange, blue;
		FOR(i, N) {
			char c;
			int t;
			scanf(" %c %d", &c, &t);
			if (c == 'O') {
				seq.PB(O);
				orange.PB(t);
			}
			else {
				seq.PB(B);
				blue.PB(t);
			}
		}
		orange.PB(INF);
		blue.PB(INF);

		int ox = 1, bx = 1, out = 0, op = 0, bp = 0;
		FOR(i, N) {
			int time = 0;
			if (seq[i] == O) {
				time = abs(orange[op]-ox) + 1;
				ox = orange[op++];
				bx += SIGN(blue[bp] - bx) * min(time, abs(blue[bp]-bx));
			}
			else {
				time = abs(blue[bp]-bx) + 1;
				bx = blue[bp++];
				ox += SIGN(orange[op]-ox) * min(time, abs(orange[op]-ox));
			}
			out += time;
		}

		printf("Case #%d: %d\n", itr, out);
	}
	return 0;
}
