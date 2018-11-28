
#include <cstdio>
#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

const int MAX_P = 10;

int P;
int miss[1 << MAX_P];
int cost[1 << MAX_P];

inline vector<int> get(int at) {
	vector<int> res;
	for (int i = 0; i < P; ++i) {
		res.push_back(at);
		at = (at - 1) / 2;
	}
	reverse(res.begin(), res.end());
	return res;
}

int main() {
	int tst;
	scanf("%d", &tst);
	for (int cas = 0; cas < tst; ++cas) {
		scanf("%d", &P);
		for (int i = 0; i < (1 << P); ++i)
			scanf("%d", &miss[i]);
		for (int i = 0; i < P; ++i)
			for (int j = 0; j < (1 << (P - i - 1)); ++j) {
				scanf("%d", &cost[(1 << (P - i - 1)) - 1 + j]);
			}
		
		static int best[1 << MAX_P + 1][1 << MAX_P];
		memset(best, 0x3f, sizeof(best));
		vector<int> path = get(0 / 2 + (1 << (P - 1)) - 1);
		for (int set = 0; set < (1 << P); ++set) {
			int sum = 0;
			for (int i = 0; i < P; ++i)
				if (((set >> i) & 1) > 0) {
					sum += cost[path[i]];
				}
			if (P - __builtin_popcount(set) <= miss[0])
				best[1][set] = sum;
		}
		for (int tid = 1; tid < (1 << P); ++tid) {
			int at = tid / 2 + (1 << (P - 1)) - 1;
			int pat = (tid - 1) / 2 + (1 << (P - 1)) - 1;
			vector<int> cpath = get(at);
			vector<int> ppath = get(pat);
			int common = 0;
			for (int i = 0; i < P; ++i)
				if (cpath[i] == ppath[i]) {
					++common;
				} else {
					break;
				}
			for (int set = 0; set < (1 << P); ++set)
				if (best[tid][set] < 0x3f3f3f3f) {
					for (int nset = 0; nset < (1 << P); ++nset) {
						if ((set & ((1 << common) - 1)) != (nset & ((1 << common) - 1)))
							continue;
						int sum = 0;
						for (int j = common; j < P; ++j)
							if (((nset >> j) & 1) > 0) {
								sum += cost[cpath[j]];
							}
						if (best[tid + 1][nset] > best[tid][set] + sum) {
							if (P - __builtin_popcount(nset) <= miss[tid])
								best[tid + 1][nset] = best[tid][set] + sum;
						}
					}
				}
		}
		printf("Case #%d: %d\n", cas + 1, *min_element(best[1 << P], best[1 << P] + (1 << P)));
		fprintf(stderr, "Solved test case %d..\n", cas + 1);
		fflush(stderr);
	}
	return 0;
}