#include <cstdio>
#include <cstring>
#include <cstdlib>

#define MAXN 15

int n, candys[MAXN];
int choosed[MAXN];
int max, hasmax;
int suma, sumb, xorsuma, xorsumb;

void DFS(int index)
{
	int i;
	if (index == n) {
		suma = sumb = 0;
		xorsuma = xorsumb = 0;
		for (i = 0; i < n; i++) {
			if (choosed[i]) {
				suma += candys[i];
				xorsuma ^= candys[i];
			} else {
				sumb += candys[i];
				xorsumb ^= candys[i];
			}
		}
		if (xorsuma == xorsumb && xorsuma) {
			hasmax = 1;
			if (suma > max) {
				max = suma;
			}
			if (sumb > max) {
				max = sumb;
			}
		}		

	}
	else {
		choosed[index] = 1;
		DFS(index+1);

		choosed[index] = 0;
		DFS(index+1);
	}
}
int main()
{
	int test_cnt;

	int i, j;
	FILE *fout = fopen("c.out", "w");

	scanf("%d", &test_cnt);
	for (i = 1; i <= test_cnt; i++) {
		max = hasmax = 0;
		memset(candys, 0, sizeof(candys));
		memset(choosed, 0, sizeof(choosed));
		scanf("%d", &n);
		for (j = 0; j < n; j++) {
			scanf("%d", &candys[j]);
		}

		DFS(0);
		fprintf(fout, "Case #%d: ", i); 
		if (hasmax) {
			fprintf(fout, "%d\n", max);
		} else {
			fprintf(fout, "NO\n");
		}
	}
	fclose(fout);
	return 0;
}