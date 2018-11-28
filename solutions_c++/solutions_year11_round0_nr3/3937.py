#include <stdio.h>
#include <string.h>


// input and output files ..
FILE* input = fopen("C-large.in","r");
FILE* output = fopen("C-large.out","w");

// number of tests T ..
int T = 0;

// number of candies ..
int N = 0;
// candy-values ..
int* C = NULL;

// 'candy-values' ..
int SeansSum = 0;
int PatricksSum = 0;
int PatricksSeansSum = 0;

int Result = -1;


void sortC(void) {

	int Buffer = 0;
	bool Event = true;

	while(true == Event) {

		Event = false;

		for(int i = 0; i < N; i++) {
			if(i > 0) {
				if(C[(i - 1)] > C[i]) {
					Buffer = C[i];
					C[i] = C[(i - 1)];
					C[(i - 1)] = Buffer;
					Event = true;
				}
			}
		}
	}

	return;
}

int main()
{

	// get T ..
	fscanf(input, "%i\n", &T);

	// test-loop
	for(int i = 0; i < T; i++) {

		// get N ..
		fscanf(input, "%i\n", &N);

		// get C[] ..
		C = new int[N];


		for(int j = 0; j < N; j++) {
			fscanf(input, "%i ", &C[j]);
		}

		// sort C[] ..
		sortC();

		for(int j = 1; j < N; j++) {

			// generate Seans sum ..
			for(int k = 0; k < j; k++) {
				PatricksSum ^= C[k];
			}

			// generate Patricks 'sum' ..
			for(int l = j; l < N; l++) {
				SeansSum += C[l];
				PatricksSeansSum ^= C[l];
			}

			// ...
			if((PatricksSeansSum == PatricksSum) && (Result < SeansSum))
				Result = SeansSum;

			// reset ..
			PatricksSum = 0;
			SeansSum = 0;
			PatricksSeansSum = 0;
		}

		// generate output ..
		fprintf(output, "Case #%i: ", (i + 1));
		if(-1 == Result) fprintf(output, "NO\n");
		else fprintf(output,"%i\n", Result);

		// clean up ..
		N = 0;
		delete[] C;
		SeansSum = 0;
		PatricksSum = 0;
		PatricksSeansSum = 0;
		Result = -1;

	}

    return 0;
}
