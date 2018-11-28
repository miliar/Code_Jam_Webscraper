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
#define SWAP(a, b, t) do {t = a; a = b; b = t;} while (0);
#define INF 1000000000
#define EPS 1e-9

static inline double getTime () {
   timeval tv;
   gettimeofday(&tv, 0);
   return tv.tv_sec + tv.tv_usec * 1e-6;
}

int start[1111], finish[1111], speed[1111];

int main () {
	int T;
	scanf("%d", &T);
	FORU(itr, 1, T) {
		int length, walk, run, stamina, N;
		scanf("%d%d%d%d%d", &length, &walk, &run, &stamina, &N);

		FOR(i, N)
			scanf("%d%d%d", start+i, finish+i, speed+i);

		for (int i = 1; i < N; ++i)
			for (int j = i; j > 0 && start[j] < start[j-1]; --j) {
				int t;
				SWAP(start[j], start[j-1], t);
				SWAP(finish[j], finish[j-1], t);
				SWAP(finish[j], finish[j-1], t);
			}

		VPII totWalks;
		int prev = 0;
		FOR(i, N) {
			if (prev < start[i])
				totWalks.PB(MP(start[i]-prev, 0));
			totWalks.PB(MP(finish[i]-start[i], speed[i]));
			prev = finish[i];
		}
		if (prev < length)
			totWalks.PB(MP(length-prev, 0));

		for (int i = 1; i < SIZE(totWalks); ++i)
			for (int j = i; j > 0 && totWalks[j].second < totWalks[j-1].second; --j) {
				PII t;
				SWAP(totWalks[j], totWalks[j-1], t);
			}

		double out = 0;
		double stamLeft = stamina;
		FOREACH(i, totWalks) {
			if (stamLeft > EPS) {
				double time = (double)i->first / (run + i->second);
				if (time <= stamLeft) {
					out += time;
					stamLeft -= time;
				}
				else {
					out += stamLeft + (i->first - (run + i->second) * stamLeft) / (walk + i->second);
					stamLeft = 0;
				}
			}
			else
				out += (double)i->first / (walk + i->second);
		}

		printf("Case #%d: %f\n", itr, out);
	}
	return 0;
}
