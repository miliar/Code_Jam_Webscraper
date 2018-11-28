#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <assert.h>
#include <string.h>

/*
1 <= T <= 42
2 <= N_B <= 3
*/

int T, N_B;

#define T_MAX 42
#define N_B_MAX 3
#define B_MAX 10

FILE *fin;
int bases[N_B_MAX];
int numBases;


char *Base(int base, int valDecimal) {
    #define RESLEN_MAX 1000
    static char res[RESLEN_MAX + 1];
	int digit = 0;
	
	for (; ;digit++) {
		res[digit] = valDecimal % base + '0';
		valDecimal /= base;
		if (valDecimal == 0)
			break;
	}

	digit++;
	res[digit] = 0;

	return res;
}

void Solve(int numTestCase) {
	int i, j;
	int crtVal;
	int val;
	int sum;
    //#define RESLEN_MAX 1000
    //static char res[RESLEN_MAX + 1];
	char *str;

	for (crtVal = 2; ; crtVal++) {
		for (i = 0; i < numBases; i++) {
			//see if it is perfect number in bases[i]
			int lastSum = -1;
			int numTrials = 0;
			for (val = crtVal; ;numTrials++) {
				str = Base(bases[i], val);
				//sum the squares of digits
				sum = 0;
				for (j = 0; j < (int)strlen(str); j++)
					sum += (str[j] - '0') * (str[j] - '0');
				if (sum == 1) {
					//happy in bases[i]
					break;
				}
				else
				/*
				if (sum < bases[i]) {
					//not happy in bases[i]
					goto NOT_HAPPY;
				}
				else
				*/
				if (sum == lastSum) {
					//prevent self-loops, that clearly do not go to 1
					goto NOT_HAPPY;
				}
				if (numTrials > 15*9*9) {
					//prevent more complex self-loops (more than 1 elem in loop), that probably do not go to 1
					goto NOT_HAPPY;
				}

				val = sum;
				lastSum = sum;
			}
		}
		if (i == numBases) {
			//happy in all bases
			printf("Case #%d: %d\n", numTestCase, crtVal);
			return;
		}
		
		NOT_HAPPY:
		;
	}
}

void ReadData() {
    int i;
	//int B;
	int res;
    #define STRLEN_MAX 1000
    char str[STRLEN_MAX + 1];

    fgets(str, STRLEN_MAX, fin);
    sscanf(str, "%d", &T);
    //fscanf(fin, "%d", &T);
    assert(T >= 1 && T <= T_MAX);

	for (i = 0; i < T; i++) {
	    fgets(str, STRLEN_MAX, fin);

        if (str[strlen(str) - 1] == '\n')
            str[strlen(str) - 1] = 0;
        if (str[strlen(str) - 1] == '\r')
            str[strlen(str) - 1] = 0;

		char *str1 = str;
		for (numBases = 0; ; numBases++) {
			res = sscanf(str1, "%d", &bases[numBases]);
			if (res <= 0)
				break;
			assert(bases[numBases] >= 2 && bases[numBases] <= B_MAX);

			for (; ; str1++) {
				if (*str1 == ' ') {
					str1++;
					break;
				}
					
				if (*str1 == 0)
					break;
			}

		}
		assert(numBases >= 2 && numBases <= N_B_MAX);

        Solve(i + 1);
    }
}

int main() {
	//freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\C\\A.in", "rt", stdin);
	freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\C\\A-small-attempt0.in", "rt", stdin);

    fin = stdin;
    ReadData();

    fclose(fin);

    return 0;
}
