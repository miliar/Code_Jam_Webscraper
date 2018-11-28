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

int main(void) {
	FILE *fin = fopen("A-large.in", "rt");
	FILE *fout = fopen("A.out", "wt");

	int L, D, N;
	int i, j, k, t, count;
	bool found;
	char A[1 << 13][16], S[1024];

	fscanf(fin, " %d %d %d", &L, &D, &N);

	for (i = 0; i < D; ++i)
		fscanf(fin, " %s", A[i]);

	for (i = 1; i <= N; ++i) {
		fscanf(fin, " %s", S);
		count = 0;

		for (j = 0; j < D; ++j) {
			k = 0;
			for (t = 0; t < L; ++t, ++k) {
				found = false;
				if (S[k] == '(') {
					for (++k; S[k] != ')'; ++k)
						if (S[k] == A[j][t])
							found = true;
				} else if (S[k] == A[j][t])
					found = true;
				if (!found) break;
			}
			if (t == L) ++count;
		}

		fprintf(fout, "Case #%d: %d\n", i, count);
	}

	fclose(fin);
	fclose(fout);

	return 0;
}
