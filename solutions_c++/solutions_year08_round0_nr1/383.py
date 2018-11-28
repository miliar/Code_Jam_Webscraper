/*
FROM: GCJ (Google Code Jam) Qualification Round 2008
PROB: A Saving the Universe
KEYW: dynamical programming

LANG: GNU C++ (g++ (GCC) 4.3.1 20080612 (Red Hat 4.3.1-2))
OPT: -lm -O2
*/

#include <cstdio>
#include <algorithm>
#include <cstring>

const int MAXQ = 1 << 10;
const int MAXS = 1 << 7;
const int MAXL = 1 << 7;

int dp[MAXS];
char se_names[MAXS][MAXL];
int se_idx[MAXS];

bool cmp_cstr (int a, int b) {
	return strcmp (se_names[a], se_names[b]) < 0;
}

int main () {
	int tc;
	scanf ("%d", &tc);

	for (int ctc = 1; ctc <= tc; ++ctc) {
		int s, q;
		scanf ("%d ", &s);

		for (int i = 0; i < s; ++i) {
			fgets (se_names[i], MAXL, stdin);
			se_idx[i] = i;
		}
		std::sort (se_idx, se_idx + s, cmp_cstr);
		/*
		for (int i = 0; i < s; ++i)
			printf ("\t%d %s\n", i, se_names[se_idx[i]]);
		*/
		memset (dp, 0, sizeof (dp));

		scanf ("%d ", &q);
		//printf ("--->%d\n", q);
		for (int i = 0; i < q; ++i) {
			fgets (se_names[s], MAXL, stdin);
			//printf ("search %s\n", se_names[s]);
			int ci = std::lower_bound (se_idx, se_idx + s, s, cmp_cstr) - se_idx;
			//printf ("found %d (%s)\n", ci, se_names[se_idx[ci]]);
			for (int j = 0; j < s; ++j) {
				if (dp[j] > dp[ci] + 1)
					dp[j] = dp[ci] + 1;
			}
			dp[ci] = q + 1;//cannot use this engine now so put infinity
		}

		printf ("Case #%d: %d\n", ctc, *std::min_element (dp, dp + s));
	}

	return 0;
}
