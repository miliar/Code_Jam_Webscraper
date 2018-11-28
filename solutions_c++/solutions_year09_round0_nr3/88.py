#include <string.h>
#include <stdio.h>
int count[501][30];
char str1[501], str2[30] = "welcome to code jam";
int main()
{
	int n;
	gets(str1);
	sscanf(str1, "%d", &n);
	for (int cases = 1; cases <= n; cases++)
	{
		gets(str1);
		memset(count, 0, sizeof(count));
		for (int i = 0; i <= 500; i++)
			count[i][0] = 1;
		int len = strlen(str1);
		int len2 = strlen(str2);
		for (int i = 1; i <= len; i++) {
			for (int j = len2; j >= 1; j--) {
				count[i][j] = count[i - 1][j] % 10000;
				if (str1[i - 1] == str2[j - 1])
					count[i][j] = (count[i][j] + count[i - 1][j - 1]) % 10000;
				//printf("%d %d %d\n", i, j, count[i][j]);
			}
		}
		printf("Case #%d: %04d\n", cases, count[len][len2]);
	}
}