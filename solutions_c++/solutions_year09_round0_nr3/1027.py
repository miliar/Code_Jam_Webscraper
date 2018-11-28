#include <numeric>
#include <cstdio>
#include <cstring>

using namespace std;

const char* welcome_stg = "welcome to code jam";

const int MAX = 1024;
const int MODULE = 10000;

int L;
char stg[MAX];
int S[2][MAX];

int solve()
{
	gets(stg);
	L = strlen(stg);

	int cur = 0;
	for (int i = 0; i <= L; i++)
		S[cur][i] = 0;
	S[cur][0] = 1;

	for (int i = 0; welcome_stg[i]; i++) {
		int prev = cur;
		cur ^= 1;
		S[cur][0] = 0;
		for (int j = 1; j <= L; j++) {
			if (welcome_stg[i] != stg[j-1]) {
				S[cur][j] = 0;
				continue;
			}

			int &r = S[cur][j];
			r = 0;
			for (int k = 0; k < j; k++)
				r += S[prev][k];
			r %= MODULE;
		}
	}

	return accumulate(S[cur], S[cur]+L+1, 0) % MODULE;
}

int main()
{
	// freopen("input.txt", "rt", stdin);

	int N;
	scanf("%d\n", &N);
	for (int i = 0; i < N; i++)
		printf("Case #%d: %04d\n", i+1, solve());
	return 0;
}
