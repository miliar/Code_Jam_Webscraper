#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

char* sentence = "welcome to code jam";

int main() {
	int memo[512][20];
	int N;
	int als = 19;
	char buf[512];

	gets(buf);
	sscanf(buf, "%d", &N);

	int i,j,k,x;

	for (i = 0; i < N; ++i) {
		gets(buf);
		int n = strlen(buf);
		memset(memo,0,sizeof(memo));
		int res = 0;
		for (j = 0; j < n; ++j) {
			for (k = 0; k < als; ++k) {
				if (sentence[k] != buf[j])
					continue;

				int ways = 0;
				if (k == 0) {
					memo[j][k] = 1;
					continue;
				}
				for (x = 0; x < j; ++x) {
					ways += memo[x][k-1];
				}
				memo[j][k] = ways % 10000;
			}

			res += memo[j][als-1];
			res %= 10000;
		}

		printf("Case #%d: %04d\n", i+1, res);
	}
}