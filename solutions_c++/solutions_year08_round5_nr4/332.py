#include <stdio.h>

#define MAX 128

int h, w, r;
int arr[MAX][MAX], rock[MAX][MAX];

void find_ans() {
	int i, j;
	int x, y;

	scanf("%d %d %d", &h, &w, &r);
	for(i = 0; i <= h; i++)
		for(j = 0; j <= w; j++) {
			arr[i][j] = 0;
			rock[i][j] = 0;
		}

	for(i = 0; i < r; i++) {
		scanf("%d %d", &x, &y);
		rock[x][y] = 1;
	}

	arr[1][1] = 1;
	for(i = 2; i <= h; i++)
		for(j = 2; j <= w; j++) {
			if(rock[i][j])continue;
			arr[i][j] = (arr[i - 1][j - 2] + arr[i - 2][j - 1]) % 10007;
		}

	printf(" %d", arr[h][w] % 10007);
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
