#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

#define MAXL 512
#define MOD  10000
#define P    19

const char *phrase = "welcome to code jam";

int  N;
char line[MAXL];
int  t[P][MAXL];

int main() {
	scanf("%d", &N);
	fgets(line, sizeof line, stdin);

	for (int tc = 1; tc <= N; ++tc) {
		fgets(line, sizeof line, stdin);
		line[strlen(line)-1] = '\0';

		memset(t, 0, sizeof t);

		int L = strlen(line);
		for (int i = 0; i < L; ++i) {
			t[0][i] = i > 0 ? t[0][i-1] : 0;
			if (line[i] == phrase[0])
				t[0][i]++;
		}

		for (int i = 1; i < P; ++i)
			for (int j = i; j < L; ++j) {
				t[i][j] = t[i][j-1];
				if (line[j] == phrase[i])
					t[i][j] = (t[i][j] + t[i-1][j-1]) % MOD;
			}

		printf("Case #%d: %04d\n", tc, t[P-1][L-1]);
	}

	return EXIT_SUCCESS;
}
