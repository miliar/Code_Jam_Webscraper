#include <cstdio>
#include <cstdlib>
#include <string>
#include <map>
#include <set>
#include <sstream>
using namespace std;
#define PI 3.14159265358979323846264338327950288
int T, N, M;
int all[1005];
int Ans[1005][105];
map <string, int> ID;
int main() {
	int i, j, Case = 1, k;
	scanf("%d", &T);
	while (T --) {
		scanf("%d", &N);
		while (getchar() != '\n');
		for (i = 0; i < N; i ++) {
			char tmp[105];
			fgets(tmp, 103, stdin);
			ID[string(tmp)] = i;
		}
		scanf("%d", &M);
		while (getchar() != '\n');
		for (i = 0; i < M; i ++) {
			char tmp[105];
			fgets(tmp, 103, stdin);
			all[i] = ID[string(tmp)];
		}
		for (i = M - 1; i >= 0; i --)
			for (j = 0; j < N; j ++) {
				if (all[i] == j) {
					Ans[i][j] = 1000000000;
					continue;
				}
				if (i == M - 1)
					Ans[i][j] = 0;
				else {
					Ans[i][j] = 1000000000;
					for (k = 0; k < N; k ++)
						Ans[i][j] = min(Ans[i][j], Ans[i + 1][k] + (k == j ? 0 : 1));
				}
			}
		int ret = 1000000000;
		for (j = 0; j < N; j ++)
			ret = min(ret, Ans[0][j]);
		printf("Case #%d: %d\n", Case ++, ret);
	}
	return 0;
}

