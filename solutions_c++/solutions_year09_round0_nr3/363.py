#include <cstdio>
#include <cstring>

using namespace std;

char s[510];
char p[25] = "welcome to code jam";
int ways[20][505];

int main() {
	int nCase, len;

	//init
	for (int j = 0; j <= 500; j++) {
		ways[0][j] = 1;
	}
	for (int i = 1; i < 20; i++) {
		for (int j = 0; j < i; j++) {
			ways[i][j] = 0;
		}
	}

	scanf("%d\n", &nCase);
	for (int t = 1; t <= nCase; t++) {
		gets(s);

		len = strlen(s);
		for (int i = 1; i <= 19; i++) {
			for (int j = 1; j <= len; j++) {
				ways[i][j] = ways[i][j - 1];

				if (p[i - 1] == s[j - 1]) {
					ways[i][j] = (ways[i][j] + ways[i - 1][j - 1]) % 10000;
				}
			}
		}

		printf("Case #%d: %04d\n", t, ways[19][len]);
	}

	return 0;
}
