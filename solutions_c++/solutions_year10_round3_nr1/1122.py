/*
Probably the simplest way to implement this problem is to use Python and create directories (where root is actually 
a given directory) and then count the number of folders created :) .
*/

//#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <assert.h>
#include <string.h>

#include <vector>

using namespace std;

/*
1 <= T <= 42
2 <= N_B <= 3
*/

int T, N;

#define T_MAX 15
//#define N_MAX 9
#define M_MAX 1000

int a[M_MAX], b[M_MAX];

FILE *fin;


void Solve(int numTestCase) {
    //int i, j;
}

#define STRLEN_MAX 102


bool Intersect(int hLeft1, int hRight1, int hLeft2, int hRight2) {
    if ( double(hLeft1 - hLeft2) * double(hRight1 - hRight2) < 0.0) {
        return true;
    }

    return false;
}

void ReadData() {
    int i, j, k;

    fscanf(fin, "%d\n", &T);
    assert(T >= 1 && T <= T_MAX);

    for (i = 0; i < T; i++) {
        fscanf(fin, "%d", &N);

        for (j = 0; j < N; j++)
            fscanf(fin, "%d %d", &a[j], &b[j]);

        int numIntersect = 0;
        for (j = 0; j < N; j++)
            for (k = j + 1; k < N; k++)
                if (Intersect(a[j], b[j], a[k], b[k]))
                    numIntersect++;

        printf("Case #%d: %d\n", i + 1, numIntersect);
        fflush(stdout);
    }
}

int main() {
    //freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\C\\A.in", "rt", stdin);
    /*
    freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\C\\A-large.in", "rt", stdin);
    freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\C\\A-large.out", "wt", stdout);
    */
    //freopen("A-large-practice.in", "rt", stdin);
    //freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\C\\A-large-practice.out", "wt", stdout);

    //freopen("A.in", "rt", stdin);
    //freopen("A-small-attempt0.in", "rt", stdin);
    //freopen("A_orig.in", "rt", stdin);
    //freopen("A-small-attempt2.in", "rt", stdin);
    freopen("A-large.in", "rt", stdin);
    freopen("A-large.out", "wt", stdout);

    fin = stdin;
    ReadData();

    fclose(fin);

    return 0;
}
