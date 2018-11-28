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

//#define P_MAX 10000
//#define Q_MAX 100
#define P_MAX 100
#define Q_MAX 5

FILE *fin;


int P, Q;
int Qs[Q_MAX];


int cells[P_MAX + 1];
int costOpt;
//int permOpt[Q_MAX];

int perm[Q_MAX];
int taken[Q_MAX];
void Permute(int pos) {
    int i;

    if (pos == Q) {
		int cost = 0;

		for (i = 1; i <= P; i++)
			cells[i] = 1;
		
		
		for (i = 0; i < Q; i++) {
			cells[Qs[perm[i]]] = 0;

			//add cost
			int j;
			for (j = Qs[perm[i]] - 1; j >= 1; j--) {
				if (cells[j] == 0)
					break;
				cost++;
			}
			for (j = Qs[perm[i]] + 1; j <= P; j++) {
				if (cells[j] == 0)
					break;
				cost++;
			}
		}
		if (costOpt > cost)
			costOpt = cost;
    }

    for (i = 0; i < Q; i++) 
        if (! taken[i]) {
            taken[i] = 1;
            perm[pos] = i;

			//!!!!
            
            //if (strcmp(permutedStr, solStr) < 0)
            Permute(pos + 1);
            taken[i] = 0;
        }
}



void Solve(int numTestCase) {
    //int i;

	#define COST_MAX 100000000
	costOpt = COST_MAX;

    Permute(0);

    printf("Case #%d: ", numTestCase);
    printf("%d\n", costOpt);
    //printf("Case #%d: %s\n", numTestCase, solStr + i);
}

void ReadData() {
    int i;

    //fgets(n, LEN_N_MAX, fin);
    //sscanf(n, "%d", &T);
    
	fscanf(fin, "%d", &T);
    assert(T >= 1 && T <= T_MAX);

    for (i = 0; i < T; i++) {
        fscanf(fin, "%d%d", &P, &Q);

		int j;
		for (j = 0; j < Q; j++)
			fscanf(fin, "%d", &Qs[j]);
		//assert(len_n <= LEN_N_MAX);

		Solve(i + 1);
        fflush(stdout);
    }
}

int main() {
    //freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\A-small-attempt0.in", "rt", stdin);
	//freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\A-large.in", "rt", stdin);
	
	freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\C-small-attempt0.in", "rt", stdin);
	freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\C-small-attempt0.out", "wt", stdout);
	//freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\C.in", "rt", stdin);

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
