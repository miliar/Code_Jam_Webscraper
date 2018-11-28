#include <cstdio>
#include <algorithm>
using namespace std;

const int M = 6;

int main() {
	int t, n;
	scanf("%d", &t);
	for (int k = 0; k < t; ++k) {
		int perm[M], ret = 0x7fffffff;
		char str[1024];
		scanf("%d", &n);
		scanf("%s", str);
		int round = 1;
		for (int i = 0; i < n; ++i) {
			perm[i] = i;
			round *= i + 1;
		}
		for (int i = 0; i < round; ++i) {
/*
			for (int j = 0; j < n; ++j) {
				printf("%d ", perm[j]);
			}
			printf("\n");
*/
			char obj[1024];
			memset(obj, 0, sizeof(obj));
			for (int index = 0; str[index]; index += n) {
				for (int j = 0; j < n; ++j)
					obj[index + j] = str[index + perm[j]];
			}
			//printf("%s\n", obj);
			char p = obj[0];
			int tmp = 1;
			for (int j = 0; obj[j]; ++j) {
				if (obj[j] != p) {
					tmp ++;
					p = obj[j];
				}
			}
			ret <?= tmp;
			next_permutation(perm, perm + n);
		}
		printf("Case #%d: %d\n", k + 1, ret);
	}
	return 0;
}
