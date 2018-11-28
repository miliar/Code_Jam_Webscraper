#include <iostream>
#include <cstring>

#define MOD 10000
#define MAXN 512

using namespace std;

char str1[MAXN];
int len1;

const char str2[] = "welcome to code jam";
const int len2 = 19;

int pd[MAXN][len2+1];

int main(int argc, char ** argv)
{
	int ntest;

	scanf("%d", &ntest);
	fgets(str1, MAXN, stdin);

	for (int t = 0; t < ntest; t++) {
		fgets(str1, MAXN, stdin);
		len1 = strlen(str1);

		memset(pd, 0, sizeof(pd));

		for (int i = 0; i <= len1; i++)
			pd[i][len2] = 1;

		for (int i = len1-1; i >= 0; i--) {
			for (int j = 0; j < len2; j++) {
				pd[i][j] = pd[i+1][j];

				if (str1[i] == str2[j])
					pd[i][j] = (pd[i][j] + pd[i+1][j+1]) % MOD;
			}
		}

		printf("Case #%d: %04d\n", t+1, pd[0][0]);
	}

	return 0;
}
