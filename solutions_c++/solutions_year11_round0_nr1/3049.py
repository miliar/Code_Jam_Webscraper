/*
 * main.cpp
 *
 *  Created on: May 7, 2011
 *      Author: greenvirag
 */

//The first line of the input gives the number of test cases, T. T test cases follow.
//Each test case consists of a single line beginning with a positive integer N,
//representing the number of buttons that need to be pressed.
//This is followed by N terms of the form "Ri Pi" where Ri is a robot color (always 'O' or 'B'),
//and Pi is a button position.



#include <iostream>
#include <cstdio>

#define NMAX 100

enum Robots {BLUE, ORANGE};

int main(int argc, char** argv)
{
	register unsigned char i, j, k;		// index variables

	unsigned char T; 		// number of test cases
	unsigned char N;		// number of buttons

	Robots R[NMAX];				// j. player -- identifies a robot
	unsigned char P[NMAX];		// j. button -- identifies a place
	unsigned char I[2][NMAX];	// instructions grouped by the robots

	FILE* input = fopen("A-large.in", "r");
	if (input == NULL) {
		std::cerr << "Error while opening input file..";
		return -1;
	}

	FILE* output = fopen("A-large-attempt0.out", "w");
	if (output == NULL) {
		std::cerr << "Error while opening output file..";
		return -1;
	}


	T = 0;
	fread(&k,1,1,input);
	while(k == ' ' || k == '\t' ) {
		fread(&k,1,1,input);
	}
	while('0' <= k && k <= '9' ) {
		T = T*10 + k - '0';
		fread(&k,1,1,input);
	}
	std::cout << "T = " << (unsigned int)T << std::endl;

	for (i = 0; i < T; i++) {
		std::cout << std::endl << (unsigned int)T << "/" << (unsigned int)i << ". test case begins.." << std::endl;

		N = 0;
		fread(&k,1,1,input);
		while(k == ' ' || k == '\t' ) {
			fread(&k,1,1,input);
		}
		while('0' <= k && k <= '9' ) {
			N = N*10 + k - '0';
			fread(&k,1,1,input);
		}
		std::cout << "N = " << (unsigned int)N << std::endl;

		unsigned char numsOf[2] = {0, 0};

		for (j = 0; j < N; j++) {

			/* Skip empty parts in the line */
			fread(&k,1,1,input);
			while(k == ' ' || k == '\t' ) {
				fread(&k,1,1,input);
			}

			if (k == 'B') {
				R[j] = BLUE;
			}
			else if (k == 'O') {
				R[j] = ORANGE;
			}

			/* Skip empty parts in the line */
			fread(&k,1,1,input);
			while(k == ' ' || k == '\t') {
				fread(&k,1,1,input);
			}

			P[j] = 0;
			while('0' <= k && k <= '9' ) {
				P[j] = P[j]*10 + k - '0';
				fread(&k,1,1,input);
				if (feof(input)) {
					break;
				}
			}

			I[R[j]][numsOf[R[j]]] = P[j];
			numsOf[R[j]]++;

			std::cout << "R[" << (unsigned int)j << "] = " << R[j] << "\t";
			std::cout << "P[" << (unsigned int)j << "] = " << (unsigned int) P[j] << std::endl;

		}

		std::cout << "Nums of B " << (unsigned int)numsOf[BLUE] << std::endl;
		for (j = 0; j < numsOf[BLUE]; j++) {
			std::cout << (unsigned int)I[BLUE][j] << " ";
		}
		std::cout << std::endl;

		std::cout << "Nums of O " << (unsigned int)numsOf[ORANGE] << std::endl;
		for (j = 0; j < numsOf[ORANGE]; j++) {
			std::cout << (unsigned int)I[ORANGE][j] << " ";
		}
		std::cout << std::endl;

		/* Make calculations */
		unsigned short int time = 0;
		unsigned char positions[2] = {1, 1};

		/* Make instructions */
		if (numsOf[BLUE] == 0) {
			for (j = 0; j < numsOf[ORANGE]; j++) {
				short temp = I[ORANGE][j] - positions[ORANGE];
				positions[ORANGE] = I[ORANGE][j];
				unsigned char dist = temp > 0 ? temp : -1*temp;
				time += dist + 1;
			}
		} else if (numsOf[ORANGE] == 0) {
			for (j = 0; j < numsOf[BLUE]; j++) {
				short temp = I[BLUE][j] - positions[BLUE];
				positions[BLUE] = I[BLUE][j];
				unsigned char dist = temp > 0 ? temp : -1*temp;
				time += dist + 1;
			}
		} else {

			j = 0;

			/* Initialize */

			unsigned char counter[2] = {0, 0};
			unsigned char waiting[2] = {0, 0};

			while ( j < N) {

				if (R[j] == BLUE) {
					waiting[BLUE] = false;
					waiting[ORANGE] = true;
				} else {
					waiting[BLUE] = true;
					waiting[ORANGE] = false;
				}


				/* Is at a good place? */
				if (counter[BLUE] < numsOf[BLUE]) {
					if (positions[BLUE] == I[BLUE][counter[BLUE]]) {
						/* Wait for the other robot? */
						if (waiting[BLUE]) {
							/* Do nothing, just wait. */
						} else {
							/* Push! */
							counter[BLUE]++;
							j++;

						}
					} else {
						/* Move */
						if (I[BLUE][counter[BLUE]] > positions[BLUE]) {
							positions[BLUE]++;
						} else {
							positions[BLUE]--;
						}
					}
				}

				/* Is at a good place? */
				if (counter[ORANGE] < numsOf[ORANGE]) {
					if (positions[ORANGE] == I[ORANGE][counter[ORANGE]]) {
						/* Wait for the other robot? */
						if (waiting[ORANGE]) {
							/* Do nothing, just wait. */
						} else {
							/* Push! */
							counter[ORANGE]++;
							j++;
						}
					} else {
						/* Move */
						if (I[ORANGE][counter[ORANGE]] > positions[ORANGE]) {
							positions[ORANGE]++;
						} else {
							positions[ORANGE]--;
						}
					}
				}

				time++;
			}

		}

		fprintf(output, "Case #%u: %hd\n", (unsigned int)i + 1, time);
		std::cout << "Case #" << (unsigned int)i + 1 << ": " << time << std::endl;
		std::cout << (unsigned int)T << "/" << (unsigned int)i << ". test case ends.." << std::endl << std::endl;
	}

	fclose(input);
	fclose(output);

	return 0;
}
