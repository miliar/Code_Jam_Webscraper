#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//                  0123456789012345678
const char* strb = "welcome to code jam"; // len = 19


char        stra[600];


int lena;

int dp[502][20];

void trimit(char* b) {
	for (;;) {
		if ('\0' == *b || '\r' == *b || '\n' == *b) {
			*b = '\0';
			return;
		}
		++b;
	}
}


// How many times does the substring stra[posa..] occur inside strb[posb..]
// Can always advance posa, if chars match, can also advance both.
//
// posa is from 0..len, inclusive
// posb is from 0..19, inclusive
//
// solve(len, 19) = 1;
// solve(x, 19) = 1;
// solve(len, x) = 0;

int solve(int posa, int posb) {
	if (-1 != dp[posa][posb]) return dp[posa][posb];

	return dp[posa][posb] = (solve(posa + 1, posb) + ((strb[posb]==stra[posa])?solve(posa+1, posb+1):0)) % 10000;
}

int main() {
	FILE* fid = fopen("C-large.in", "r");
	FILE* fout = fopen("C.out", "w");

	int N = 0;




	fgets(stra, 550, fid);
	trimit(stra);

	N = atoi(stra);

	for (int cas = 1; cas <= N; ++cas) {


		fgets(stra, 550, fid);
		trimit(stra);

		lena = strlen(stra);

		for (int pa = 0; pa <= lena; pa++) {
			for (int pb = 0; pb <= 19; pb++) {
				if (pb >= 19) dp[pa][pb] = 1; else
				if (pa >= lena) dp[pa][pb] = 0; else
				dp[pa][pb] = -1;
			}
		}

		fprintf(fout, "Case #%d: %04d\n", cas, solve(0,0));

	}


	return 0;
}

