#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cstring>

using namespace std;

#define MN			1024
#define MP			32
#define MOD			10000

int tests;
char T[MN];
char P[MP] = "welcome to code jam";
int N, M;

int f[MN][MP];

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	gets(T);
	tests = atoi(T);
	//printf("%d\n", tests);

	for (int test=0; test<tests; ++test) {
		gets(T);
		N = strlen(T);
		M = strlen(P);
		//printf("%d %d\n", N, M);

		memset(f, 0, sizeof f);
		f[0][0] = 1;

		for (int i=0; i<N; ++i) {
			for (int j=0; j<=M; ++j) {
				f[i+1][j] = (f[i+1][j] + f[i][j]) % MOD;
				if (j<M && T[i]==P[j]) {
					f[i+1][j+1] = (f[i+1][j+1] + f[i][j]) % MOD;
				}
			}
		}

		printf("Case #%d: %04d\n", test+1, f[N][M]);
	}

	return 0;
}