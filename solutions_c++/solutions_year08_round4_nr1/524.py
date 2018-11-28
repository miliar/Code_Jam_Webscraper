#include <stdio.h>

#define MAX 10240

int data[MAX][2], value[MAX], best[MAX][2];

int max(int x, int y) {
	if(x > y)
		return x;
	return y;
}

int min(int x, int y) {
	if(x < y)
		return x;
	return y;
}

void find_ans() {
	int n;
	int i, j;

	scanf("%d %d", &n, &value[0]);
	for(i = 1; i <= n; i++)
		best[i][0] = best[i][1] = MAX;
	for(i = 1; i <= (n - 1) / 2; i++)
		scanf("%d %d", &data[i][0], &data[i][1]);
	for(i = n - ((n + 1) / 2) + 1; i <= n; i++) {
		scanf("%d", &value[i]);
		best[i][value[i]] = 0;
	}
	for(i = (n - 1) / 2; i >= 1; i--) {
		if(data[i][0] == 0) {
			best[i][0] = min(best[i][0], best[i * 2][0] + best[i * 2 + 1][0]);
			best[i][1] = min(min(best[i][1], best[i * 2][1] + best[i * 2 + 1][0]), min(best[i * 2][0] + best[i * 2 + 1][1], best[i * 2][1] + best[i * 2 + 1][1]));
		} else {
			best[i][0] = min(min(best[i][0], best[i * 2][1] + best[i * 2 + 1][0]), min(best[i * 2][0] + best[i * 2 + 1][1], best[i * 2][0] + best[i * 2 + 1][0]));
			best[i][1] = min(best[i][1], best[i * 2][1] + best[i * 2 + 1][1]);
		}

		if(data[i][1] == 1) {
			if(data[i][0] == 1) {
				best[i][0] = min(best[i][0], best[i * 2][0] + best[i * 2 + 1][0] + 1);
				best[i][1] = min(min(best[i][1], best[i * 2][1] + best[i * 2 + 1][0] + 1), min(best[i * 2][0] + best[i * 2 + 1][1] + 1, best[i * 2][1] + best[i * 2 + 1][1] + 1));
			} else {
				best[i][0] = min(min(best[i][0], best[i * 2][1] + best[i * 2 + 1][0] + 1), min(best[i * 2][0] + best[i * 2 + 1][1] + 1, best[i * 2][0] + best[i * 2 + 1][0] + 1));
				best[i][1] = min(best[i][1], best[i * 2][1] + best[i * 2 + 1][1] + 1);
			}
		}
	}

	if(best[1][value[0]] == MAX)
		printf(" IMPOSSIBLE");
	else printf(" %d", best[1][value[0]]);
}

int main(int argc, char *argv[])
{
	int i, n;

	scanf("%d", &n);
	for(i = 1; i <= n; i++) {
		printf("Case #%d:", i);
		find_ans();
		printf("\n");
	}

	return 0;
}
