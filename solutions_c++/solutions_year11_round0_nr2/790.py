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

int combine[26][26];
vector<PII> forbid;

int main () {
	int T;
	scanf("%d", &T);
	FORU(itr, 1, T) {
		memset(combine, 0, sizeof(combine));
		forbid.clear();

		int C;
		scanf("%d ", &C);
		FOR(i, C) {
			char in1, in2, out;
			scanf("%c%c%c ", &in1, &in2, &out);

			combine[in1-'A'][in2-'A'] = out-'A';
			combine[in2-'A'][in1-'A'] = out-'A';
		}

		int D;
		scanf("%d ", &D);
		FOR(i, D) {
			char in1, in2;
			scanf("%c%c ", &in1, &in2);

			forbid.PB(MP(in1-'A', in2-'A'));
		}

		int N;
		scanf("%d ", &N);
		vector<int> spell;
		int count[26];
		memset(count, 0, sizeof(count));
		FOR(i, N) {
			char next;
			scanf("%c", &next);
			spell.PB(next-'A');
			++count[next-'A'];

			while (SIZE(spell) >= 2) {
				int combined = combine[spell[SIZE(spell)-1]][spell[SIZE(spell)-2]];
				if (combined != 0) {
					--count[spell[SIZE(spell)-1]];
					--count[spell[SIZE(spell)-2]];
					++count[combined];
					spell.pop_back();
					spell.pop_back();
					spell.PB(combined);
				}
				else
					break;
			}

			if (SIZE(spell) >= 2) {
				FOREACH(p, forbid) {
					if (count[p->first] > 0 && count[p->second] > 0) {
						spell.clear();
						memset(count, 0, sizeof(count));
						break;
					}
				}
			}
		}

		printf("Case #%d: [", itr);
		FOR(i, SIZE(spell)) {
			printf("%c", spell[i]+'A');
			if (i < SIZE(spell)-1)
				printf(", ");
		}
		printf("]\n");
	}
	return 0;
}
