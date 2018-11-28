#include <cstdio>
#include <cstring>
#include <vector>
#include <map>

using namespace std;

typedef long long LL;

int R, k, N;
// number of groups
int a[1000];
// next[i]: the starting group in the next run
// 			when this run starts at group i
int next[1000];
// earn[i]: the money earned for a run if starts
// 			at group i
int earn[1000];

void init() {
	scanf("%d%d%d", &R, &k, &N);
	LL sum = 0;
	for (int i = 0; i < N; i++) {
		scanf("%d", a + i);
		sum += a[i];
	}
	if (sum <= k) {
		for (int i = 0; i < N; i++) {
			next[i] = i;
			earn[i] = sum;
		}
	} else {
		for (int i = 0; i < N; i++) {
			earn[i] = 0;
			for (int j = 0; j < N; j++) {
				int t = (i + j) % N;
				if (earn[i] + a[t] > k) {
					next[i] = t;
					break;
				} else {
					earn[i] += a[t];
				}
			}
		}
	}
}

LL run() {
	LL ret = 0;
	vector <int> table(N, -1);
	vector <int> v;
	table[0] = 0;
	v.push_back(0);
	int start = -1, end = -1;
	for (int i = 1, pre = 0; i < R; i++) {
		pre = next[pre];
		if (table[pre] != -1) {
			start = table[pre];
			end = i;
			break;
		} else {
			v.push_back(pre);
			table[pre] = i;
		}
	}
	if (end == -1) {
		for (int i = 0; i < R; i++) {
			ret += earn[v[i]];
		}
		return ret;
	}
	for (int i = 0; i < start; i++) {
		ret += earn[v[i]];
	}
	R -= start;
	LL sum = 0;
	for (int i = start; i < end; i++) {
		sum += earn[v[i]];
	}
	ret += R / (end - start) * sum;
	R %= end - start;
	for (int i = 0; i < R; i++) {
		ret += earn[v[start + i]];
	}
	return ret;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		init();
/*		for (int i = 0; i < N; i++) {
			printf("%d ", next[i]);
		}
		printf("\n");
		for (int i = 0; i < N; i++) {
			printf("%d ", earn[i]);
		}
		printf("\n");
		fflush(stdout);*/
		LL res = run();
		printf("Case #%d: %lld\n", cas, res);
	}
	return 0;
}
