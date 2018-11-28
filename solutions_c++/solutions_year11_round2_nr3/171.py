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

int wall[10][2];
VI walls[10];
VVI rooms;
int colors;
int coloring[10];
int N, M;

bool check () {
	FOREACH(r, rooms) {
		int b = 0;
		FOREACH(v, *r)
			b |= 1 << coloring[*v];
		if (b != (1 << colors) - 1)
			return 0;
	}
	return 1;
}

bool dfs (int p) {
	if (p == N)
		return check();

	FOR(i, colors) {
		coloring[p] = i;
		if (dfs(p+1))
			return 1;
	}
	return 0;
}

int main () {
	int T;
	scanf("%d", &T);
	FORU(itr, 1, T) {
		scanf("%d %d", &N, &M);

		FOR(i, M)
			scanf("%d", &wall[i][0]);
		FOR(i, M)
			scanf("%d", &wall[i][1]);

		FOR(i, N) {
			walls[i].clear();
			walls[i].PB((i + 1) % N);
		}
		FOR(i, M) {
			walls[wall[i][0]-1].PB(wall[i][1]-1);
			walls[wall[i][1]-1].PB(wall[i][0]-1);
		}

		int smallest = N;
		rooms.clear();
		FOR(i, N) {
			FOREACH(j, walls[i]) {
				VI room;
				room.PB(i);
				int cur = *j, prev = i;
				while (cur != i) {
					if (cur < i)
						break;
					room.PB(cur);
					int next = (cur + 1) % N, idist = (i - cur + N) % N;
					FOREACH(k, walls[cur]) {
						int dist = (*k - cur + N) % N;
						if (*k != prev && dist <= idist && dist > (next - cur + N) % N)
							next = *k;
					}
					prev = cur;
					cur = next;
				}

				if (cur == i) {
					rooms.PB(room);
					smallest = min(smallest, SIZE(room));
				}
			}
		}

//		printf("%d rooms:\n", SIZE(rooms));
//		FOREACH(v, rooms) {
//			FOREACH(i, *v)
//				printf("%d ", *i);
//			printf("\n");
//		}

		FORD(i, smallest, 1) {
			colors = i;
			if (dfs(0)) {
				printf("Case #%d: %d\n", itr, i);
				FOR(j, N)
					printf("%d ", coloring[j]+1);
				printf("\n");
				break;
			}
		}
	}
	return 0;
}
