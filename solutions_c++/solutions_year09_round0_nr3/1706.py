#include <cstdio>
#include <cstring>

const char *str = "welcome to code jam";
char buf[501];

int getAns(char *buf)
{
	int temp[501][strlen(str)+1];
	memset(temp, 0, sizeof(temp));
	temp[0][0] = 1;
	for (int i=1; i<=strlen(buf); ++i) {
		temp[i][0] = 1;
		for (int j=1; j<=strlen(str); ++j) {
			temp[i][j] = temp[i-1][j];
			if (buf[i-1] == str[j-1])
				temp[i][j] += temp[i-1][j-1];

		}
	}
	return temp[strlen(buf)][strlen(str)];
}

int main()
{
	int N;
	scanf("%d\n", &N);
	for (int i=1; i<=N; ++i) {
		fgets(buf, 501, stdin);
		int ans = getAns(buf);
		printf("Case #%d: %04d\n", i, ans);
	}
	return 0;
}

