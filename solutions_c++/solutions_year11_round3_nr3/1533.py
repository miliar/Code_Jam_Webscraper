#include <stdio.h>
#include <string.h>

int main()
{

	// input and output file ..
	FILE* input = fopen("C-small-attempt0.in","r");
	FILE* output = fopen("C-small-attempt0.out","w");

	// some variables ..
	int T = 0; // number of test cases

	int N = 0;
	int L = 0;
	int H = 0;

	int* frequencies = NULL;

	int Note = -1;
	bool valid = true;


	// get T..
	fscanf(input, "%i\n", &T);

	for(int t = 0 ; t < T; t++) {

	// get N, L and H ..
	fscanf(input, "%i %i %i\n", &N, &L, &H);

	// get N tones ..
	frequencies = new int[N];
	for(int n = 0; n < N; n++) {
		fscanf(input, "%i", &frequencies[n]);

	}


	// test ..
	for(int f = L; f <= H; f++) {

		valid = true;

		for(int n = 0; n < N; n++) {

			if( (0 != (f % frequencies[n])) && (0 != (frequencies[n] % f)) )
				valid = false;

		}

		if(true == valid) {
			Note = f;
			f = H + 1;
		}

	}

	// output ..
	if(-1 == Note)
		fprintf(output, "Case #%i: NO\n", (t + 1));
	else
		fprintf(output, "Case #%i: %i\n", (t + 1), Note);


	// reset variables ..
	Note = -1;
	delete[] frequencies;


	}

	return 0;
}
