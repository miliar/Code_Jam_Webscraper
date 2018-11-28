#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 50;

int N, M, cost[MAXN][MAXN];
bool mat[MAXN][MAXN];

inline int ABS(int x) {
	if (x < 0) return -x;
	return x;
}

inline void SWAP(bool * a, bool * b) {
	for (int i = 0; i < N; i++) swap(a[i], b[i]);
}

int main() {
	int task;
	scanf("%d", &task);
	for (int oo = 0; oo < task; oo++) {
		scanf("%d", &N);
		for (int i = 0; i < N; i++) {
			char tmpstr[1024];
			scanf("%s", tmpstr);
			for (int j = 0; j < N; j++) mat[i][j] = (tmpstr[j] == '1');
		}
		int cc = 0;
		for (int i = 0; i < N; i++) {
			for (int j = i; j < N; j++) {
				bool flag = true;
				for (int k = i + 1; k < N; k++) {
					if (mat[j][k]) flag = false;
				}
				if (flag) {
//					printf("i = %d j = %d\n", i, j);
					for (int k = j; k > i; k--) {
						SWAP(mat[k], mat[k - 1]);
						cc++;
					}
					break;
				}
			}
		}
/*		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) printf("%d ", cost[i][j]); putchar('\n');
		}*/
		printf("Case #%d: %d\n", oo + 1, cc);
	}
	return 0;
}
