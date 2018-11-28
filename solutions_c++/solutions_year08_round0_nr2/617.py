#include <stdio.h>
#include <algorithm>
using namespace std;
typedef int arr[110];
arr ta, tb, fa, fb;
int main() {
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	int cas, t, tur, na, nb, ansa, ansb, i, j, k;
	for (scanf("%d", &cas), t = 1; t <= cas; ++t) {
		scanf("%d%d%d", &tur, &na, &nb);
		for (i = 0, ansa = na; i < na; ++i) {
			scanf("%d:%d", &j, &k);
			fa[i] = j * 60 + k;
			scanf("%d:%d", &j, &k);
			tb[i] = j * 60 + k + tur;
		}
		for (i = 0, ansb = nb; i < nb; ++i) {
			scanf("%d:%d", &j, &k);
			fb[i] = j * 60 + k;
			scanf("%d:%d", &j, &k);
			ta[i] = j * 60 + k + tur;
		}
		sort(&fa[0], &fa[na]); sort(&tb[0], &tb[na]);
		sort(&fb[0], &fb[nb]); sort(&ta[0], &ta[nb]);
		for (i = 0, j = 0; i < na && j < nb; ++j)
			if (tb[i] <= fb[j]) {
				++i;
				--ansb;
			}
		for (i = 0, j = 0; i < nb && j < na; ++j)
			if (ta[i] <= fa[j]) {
				++i;
				--ansa;
			}
		printf("Case #%d: %d %d\n", t, ansa, ansb);
	}
	return 0;
}