using namespace std;

#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <vector>
#include <sstream>
#include <algorithm>
#include <cstdlib>
#include <cstring>

#define FORI(p, X) for (__typeof( (X).begin() ) p = (X).begin(); p != (X).end(); ++p)
#define ALL(X) (X).begin(), (X).end()
#define PB push_back
#define MP make_pair

const int INF = 0x3f3f3f3f;
const int MOD = 10000;
const char text[] = "welcome to code jam";
const int L = 19;

typedef pair <int, int> PII;
typedef vector <int> VI;
typedef long long lint;

int DP[32];

int main(void) {
	FILE *fin = fopen("C-large.in", "rt");
	FILE *fout = fopen("output.out", "wt");

	int NCASE, ncase;
	char S[1024];
	int i, j;

	fscanf(fin, " %d", &NCASE);
	fgets(S, 1024, fin);

	for (ncase = 1; ncase <= NCASE; ++ncase) {

		fgets(S, 1024, fin);
		memset(DP, 0x00, sizeof(DP));

		for (i = 0; S[i] != '\n' && S[i]; ++i) {
			if (text[0] == S[i]) ++DP[0];

			for (j = 1; j < L; ++j)
				if (text[j] == S[i])
					DP[j] = (DP[j] + DP[j-1]) % MOD;
/*
			printf("%c\t", S[i]);
			for (j = 0; j < L; ++j)
				printf("%d ", DP[j]);
			printf("\n");
*/

		}

		fprintf(fout, "Case #%d: %.4d\n", ncase, DP[L-1]);
	}


	fclose(fin);
	fclose(fout);

	return 0;
}
