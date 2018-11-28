#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

const int MaxN = 1005;
const double eps = 1e-8;
struct Node {
	int L, p;
} node[MaxN];
bool vst[MaxN];
int ret[MaxN];
int N;

int sgn(double x) {
	return x < -eps ? -1 : x > eps;
}

int main() {
	int T, cas = 1;
	bool exist;
	
	//freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	scanf("%d", &T);
	while (T--) {
		printf("Case #%d: ", cas++);
		scanf("%d", &N);
		exist = false;
		for (int i = 0; i < N; i++) scanf("%d", &node[i].L);
		for (int i = 0; i < N; i++) {
			scanf("%d", &node[i].p);
			exist |= node[i].p == 100;
			node[i].p = 100 - node[i].p;
			vst[i] = false;
		}
		if (exist) {
			for (int i = 0; i < N; i++) {
				if (i) putchar(' ');
				printf("%d", i);
			}
			puts("");
			continue;
		}
		double E = 0.0;
		for (int i = 0; i < N; i++) {
			int idx = -1, mx = -1;
			for (int j = 0; j < N; j++) if (!vst[j]) {
				if (mx <= node[j].p) {
					mx = node[j].p;
					idx = j;
				}
			}
			vst[idx] = true;
			E = 100.0 * E / node[idx].p + node[idx].L;
			ret[N - 1 - i] = idx;
		}
		for (int i = 0; i < N; i++) {
			if (i) putchar(' ');
			printf("%d", ret[i]);
		}
		puts("");
	}
	
	return 0;
}

