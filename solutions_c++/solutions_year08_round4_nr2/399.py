#include <stdio.h>
#include <string>
using namespace std;
bool mul[2600];
int fro[2600][2];
int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int cas, tes, n, m, a, i, j;
	for (scanf("%d", &cas), tes = 1; tes <= cas; ++tes) {
		scanf("%d%d%d", &n, &m, &a);
		memset(mul, false, n * m + 1);
		for (i = 0; i <= n; ++i)
			for (j = 0; j <= m; ++j) {
				mul[i * j] = true;
				fro[i * j][0] = i; fro[i * j][1] = j;
			}
		for (i = a; i <= n * m; ++i) 
			if (mul[i] && mul[i - a])
				break;
		printf("Case #%d: ", tes);
		if (i <= n * m) 
			printf("0 0 %d %d %d %d\n", fro[i][0], fro[i - a][1], fro[i - a][0], fro[i][1]);
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}