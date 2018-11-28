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

typedef pair <int, int> PII;
typedef vector <int> VI;
typedef long long lint;

int next(int x) {
	if (x == 1) return 0;
	if (x == 0) return 2;
	return x + 1;
}

int main(void) {
	FILE *fin = fopen("a-large.in", "rt");
	FILE *fout = fopen("output.out", "wt");
	int ncase, NCASE;
	lint ans, putere;
	int i, o[256], N, base, t;
	char S[64];

	fscanf(fin, " %d", &NCASE);

	for (ncase = 1; ncase <= NCASE; ++ncase) {

		fscanf(fin, " %s", S);

		memset(o, 0xff, sizeof(o));
		N = strlen(S);

		base = 0; t = 1;
		for (i = 0; i < N; ++i)
			if (o[ S[i] ] == -1)
				o[ S[i] ] = t, ++base, t = next(t);

		if (base == 1 && N == 1)
			ans = 1;
		else {
			ans = 0;
			if (base == 1) base = 2;

			for (i = N - 1, putere = 1; i >= 0; --i, putere *= base)
				ans += (lint) o[ S[i] ] * putere;
		}

		fprintf(fout, "Case #%d: %lld\n", ncase, ans);
	}


	fclose(fin);
	fclose(fout);

	return 0;
}
