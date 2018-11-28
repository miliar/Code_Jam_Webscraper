#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <assert.h>
#include <string.h>

/*
1 <= T <= 42
2 <= N_B <= 3
*/

int T;

#define T_MAX 100
#define LEN_N_MAX 61 + 3
//#define LEN_N_MAX 10 + 3

FILE *fin;
int len_n;

char n[LEN_N_MAX + 1];

void Solve(int numTestCase) {
    int i;

#define NUM_LETTERS_MAX 256
	int translate[NUM_LETTERS_MAX];

	for (i = 0; i < NUM_LETTERS_MAX; i++)
		translate[i] = -1;

	translate[n[0]] = 1;

	for (i = 1; i < len_n; i++)
		if (n[i] != n[i - 1])
			break;

	translate[n[i]] = 0;
	i++;

	int base = 2;
	for (; i < len_n; i++)
		if (translate[n[i]] == -1) {
			translate[n[i]] = base;
			base++;
		}

	//here base represents exactly the minimum base

	//long long!!!!
	//long int n10 = 0;
	//long int rank = 1;
	long long unsigned n10 = 0;
	long long unsigned rank = 1;
	
	for (i = 0; i < len_n; i++) {
		n10 += translate[n[len_n - i - 1]] * rank;
		rank *= base;
	}

	printf("Case #%d: ", numTestCase);
	//printf("%ld\n", n10);
	//printf("%Lu\n", n10); //!!!!
	printf("%llu\n", n10); //!!!!

	//printf("Case #%d: %s\n", numTestCase, solStr + i);
}

void ReadData() {
    int i;

    fgets(n, LEN_N_MAX, fin);
    sscanf(n, "%d", &T);
    //fscanf(fin, "%d", &T);
    assert(T >= 1 && T <= T_MAX);

    for (i = 0; i < T; i++) {
        fgets(n, LEN_N_MAX, fin);

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
    //freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\A-small-attempt0.in", "rt", stdin);
	freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\A-large.in", "rt", stdin);
    /*
    freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\C\\A-large.in", "rt", stdin);
    freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\C\\A-large.out", "wt", stdout);
    */

	/*
	freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\B-small-attempt0.in", "rt", stdin);
    freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\B-small-attempt0.out", "wt", stdout);
	*/

	//freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\B-large_mine.in", "rt", stdin);
		//freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\B-small-attempt0.out", "wt", stdout);

    fin = stdin;
    ReadData();


    fclose(fin);

    return 0;
}
