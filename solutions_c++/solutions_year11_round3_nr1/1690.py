#include <stdio.h>
#include <string.h>

int arr[52][52];

int main()
{
	int Cases;
	scanf("%d", &Cases);
	char gg[6] = {'.', '#', '/', '\\', '\\', '/'};
	for (int Case = 1; Case <= Cases; ++Case) {
		int R, C;
		memset(arr, 0, sizeof(arr));
		scanf("%d %d", &R, &C);
		for (int i = 1; i <= R; ++i) {
			for (int j = 1; j <= C; ++j) {
				char c;
				do {
					scanf("%c", &c);
				} while (c != '.' && c != '#');
				if (c == '.')
					arr[i][j] = 0;
				else
					arr[i][j] = 1;
			}
		}
		int cnt = 0;
		int br = 0;
		for (int i = 1; i <= R; ++i) {
			for (int j = 1; j <= C; ++j) {
				if (arr[i][j] == 1) {
					switch (arr[i - 1][j]) {
					case 2:
						if  (arr[i][j - 1] == 2) {
							br = 1;
							break;
						}
						arr[i][j] = 4;
						++cnt;
						break;
					case 3:
						arr[i][j] = 5;
						++cnt;
						break;
					default:
						++cnt;
						if (arr[i][j - 1] == 2)
							arr[i][j] = 3;
						else
							arr[i][j] = 2;
						break;
					}
				}
			}
			if (br)
				break;
		}
		printf("Case #%d:\n", Case);
		if (br || cnt % 4) {
			printf("Impossible\n");
		} else {
			for (int i = 1; i <= R; ++i) {
				for (int j = 1; j <= C; ++j) {
					putchar(gg[arr[i][j]]);
				}
				putchar('\n');
			}
		}
	}
	return 0;
}

