#include <stdio.h>
#include <string.h>

// input and output files ..
FILE* input = fopen("B-small-attempt1.in", "r");
FILE* output = fopen("B-small-attempt1.out", "w");

// variables ..
int T = 0;

int C = 0;
int D = 0;
int N = 0;

int m = 0;

char** Combinations = NULL;
char** Opposites = NULL;
char InputString[10];
char OutputString[10];


int CheckForCombination(char lastElement, char newElement) {

	for(int i = 0; i < C; i++) {

		if(lastElement == Combinations[i][0]) {
			if(newElement == Combinations[i][1])
				return (int)Combinations[i][2];
		}
		else if(newElement == Combinations[i][0]) {
			if(lastElement == Combinations[i][1])
				return (int)Combinations[i][2];
		}

	}

	return -1;

}


bool isOppossed(char Element) {

	for(int i = 0; i < m; i++) {

		for(int j = 0; j < D; j++) {

			if(Element == Opposites[j][0]){
				if(OutputString[i] == Opposites[j][1])
					return true;
			}
			else if(OutputString[i] == Opposites[j][0]){
				if(Element == Opposites[j][1])
					return true;
			}

		}

	}

	return false;

}


int main()
{
	// get T ..
	fscanf(input, "%i\n", &T);

	// test cases ..
	for(int i = 0; i < T; i++) {

		// process C ..
		fscanf(input, "%i ", &C);

		if(0 != C) Combinations = new char*[C];

		for(int j = 0; j < C; j++) {
			Combinations[j] = new char[3];
			fscanf(input, "%c%c%c ", &Combinations[j][0], &Combinations[j][1], &Combinations[j][2]);

		}

		// process D ..
		fscanf(input, "%i ", &D);

		if(0 != D) Opposites = new char*[D];

		for(int k = 0; k < D; k++) {
			Opposites[k] = new char[2];
			fscanf(input, "%c%c", &Opposites[k][0], &Opposites[k][1]);
		}

		// process N ..
		fscanf(input, "%i ", &N);

		memset(InputString, '\0', 10);
		memset (OutputString,'\0',10);

		fscanf(input, "%s", InputString);

		// process input ..
		for(int l = 0; l < N; l++) {

			if(0 != m) {
				if(-1 == CheckForCombination(OutputString[(m - 1)], InputString[l])) {
					OutputString[m] = InputString[l];

					if(true == isOppossed(OutputString[m])) {
						m = 0;
						memset (OutputString,'\0',10);

					}
					else m++;
				}
				else OutputString[(m - 1)] = CheckForCombination(OutputString[(m - 1)], InputString[l]);


			}
			else {
				OutputString[m] = InputString[l];
				m++;
			}

		}



		// generate output ..
		fprintf(output, "Case #%i: [", (i + 1));

		//cout << OutputString << endl;

		for(int n = 0; n < m; n++) {
			if(0 == n) {
				if(m == (n + 1)) fprintf(output, "%c", OutputString[n]);
				else fprintf(output, "%c,", OutputString[n]);
			}
			else if(m == (n + 1)) fprintf(output, " %c", OutputString[n]);
			else fprintf(output, " %c,", OutputString[n]);
		}

		fprintf(output, "]\n");


		// clean up ..
		for(int o = 0; o < C; o++)
			delete[] Combinations[o];

		for(int p = 0; p < D; p++)
			delete[] Opposites[p];

		C = 0;
		D = 0;
		N = 0;

		m = 0;

		memset(InputString, '\0', 10);
		memset (OutputString,'\0',10);

	}

    return 0;
}
