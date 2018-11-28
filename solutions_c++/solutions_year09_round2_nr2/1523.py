#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <assert.h>
#include <string.h>

/*
1 <= T <= 42
2 <= N_B <= 3
*/

int T;

#define T_MAX 500
#define LEN_N_MAX 20 + 3
//#define LEN_N_MAX 6 + 3

FILE *fin;
int len_n;

#define STRLEN_MAX 1000

char n[STRLEN_MAX + 1];
char nStr[LEN_N_MAX + 1];
char solStr[LEN_N_MAX + 1];

int perm[LEN_N_MAX];
int taken[LEN_N_MAX];
void Permute(int pos) {
	int i;

	if (pos == len_n) {
		char permutedStr[LEN_N_MAX + 1];
		for (i = 0; i < LEN_N_MAX - len_n; i++)
			permutedStr[i] = '0';
		for (i = 0; i < len_n; i++)
			permutedStr[LEN_N_MAX - len_n + i] = (perm[i] == len_n - 1) ? '0' : n[perm[i]];
		permutedStr[LEN_N_MAX] = 0;
		
		//assert(nStr[LEN_N_MAX - 1] == '0');
		//nStr[LEN_N_MAX - 1] = 0;

		if (strcmp(nStr, permutedStr) < 0)
			if (strcmp(solStr, permutedStr) > 0)
				strcpy(solStr, permutedStr);
		
		//nStr[LEN_N_MAX - 1] = '0';
	}

	for (i = 0; i < len_n; i++) 
		if (! taken[i]) {
			taken[i] = 1;
			perm[pos] = i;
			Permute(pos + 1);
			taken[i] = 0;
		}
}

void Solve(int numTestCase) {
    int i;
    //#define RESLEN_MAX 1000
    //static char res[RESLEN_MAX + 1];

	for (i = 0; i < len_n; i++)
		taken[i] = 0;

	for (i = 0; i < LEN_N_MAX - len_n; i++)
		nStr[i] = '0';
	for (i = 0; i < len_n; i++)
		nStr[LEN_N_MAX - len_n + i] = n[i];
	nStr[LEN_N_MAX] = 0;

	//add a '0', in case we don't find solution with only the digits of the original number n
	//n[len_n++] = '0';
	//n[len_n] = 0;
	//strcpy(solStr, nStr);
	//solStr[LEN_N_MAX - len_n - 1] = '9';
	/*
	for (i = 0; i < LEN_N_MAX - len_n - 1; i++)
		nStr[i] = '0';
	for (i = 0; i < len_n; i++)
		nStr[LEN_N_MAX - len_n + i - 1] = n[i];
	nStr[LEN_N_MAX - 1] = '0';
	nStr[LEN_N_MAX] = 0;
	strcpy(solStr, nStr);
	*/

	for (i = 0; i < LEN_N_MAX - len_n - 1; i++)
		solStr[i] = '0';
	for (i = 0; i < len_n; i++)
		solStr[LEN_N_MAX - len_n + i - 1] = n[i];
	solStr[LEN_N_MAX - 1] = '0';
	solStr[LEN_N_MAX] = 0;

	len_n++;


	Permute(0);

	for (i = 0; i < LEN_N_MAX; i++)
		if (solStr[i] != '0')
			break;

	printf("Case #%d: %s\n", numTestCase, solStr + i);
}

void ReadData() {
    int i;

    fgets(n, STRLEN_MAX, fin);
    sscanf(n, "%d", &T);
    //fscanf(fin, "%d", &T);
    assert(T >= 1 && T <= T_MAX);

    for (i = 0; i < T; i++) {
        fgets(n, STRLEN_MAX, fin);

        if (n[strlen(n) - 1] == '\n')
            n[strlen(n) - 1] = 0;
        if (n[strlen(n) - 1] == '\r')
            n[strlen(n) - 1] = 0;

        len_n = strlen(n);
		assert(len_n <= LEN_N_MAX);

		Solve(i + 1);
        fflush(stdout);
    }
}

int main() {
    //freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\C\\A.in", "rt", stdin);
    /*
    freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\C\\A-large.in", "rt", stdin);
    freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\C\\A-large.out", "wt", stdout);
    */

	freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\B-small-attempt2.in", "rt", stdin);
    freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\B-small-attempt2.out", "wt", stdout);

	//freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\B-large_mine.in", "rt", stdin);
    //freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\B-small-attempt0.out", "wt", stdout);

    fin = stdin;
    ReadData();


    fclose(fin);

    return 0;
}
