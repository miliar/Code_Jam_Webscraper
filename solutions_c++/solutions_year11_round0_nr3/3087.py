/*
 * main.cpp
 *
 *  Created on: May 7, 2011
 *      Author: greenvirag
 */


#include <iostream>
#include <cstdio>
#include <map>
#include <set>
#include <vector>
#include <algorithm>

struct State {
	std::vector<int> pilesA;
	std::vector<int> pilesB;
	int pilesASum;
	int pilesBSum;
};

void generatePiles(std::vector<int> freeCandies, State currentState, State** bestState, const int possibleMaximum)
{
	if (*bestState != NULL && (*bestState)->pilesASum == possibleMaximum) {
		return;
	}

	if (freeCandies.empty()) {

		if (currentState.pilesASum == currentState.pilesBSum) {

			if (!currentState.pilesA.empty() && !currentState.pilesB.empty()) {

				if (*bestState == NULL) {
					*bestState = new State;
					(*bestState)->pilesASum = 0;
				}

				int ASum = 0; int BSum = 0;
				for (unsigned int i = 0; i<currentState.pilesA.size(); i++) {
					ASum += currentState.pilesA.at(i);
				}
				for (unsigned int i = 0; i<currentState.pilesB.size(); i++) {
					BSum += currentState.pilesB.at(i);
				}

				int max = (ASum > BSum) ? ASum : BSum;
				if((*bestState)->pilesASum < max) {
					(*bestState)->pilesASum = max;
				}

			}
		}
		return;
	}

	std::vector<int> n_freeCandies = freeCandies;
	int candy = n_freeCandies.back();
	n_freeCandies.pop_back();

	/* Give to A */
	State n_currentState_A = currentState;
	n_currentState_A.pilesA.push_back(candy);
	n_currentState_A.pilesASum = currentState.pilesASum ^ candy;
	generatePiles(n_freeCandies, n_currentState_A, bestState, possibleMaximum);

	/* Give to B */
	State n_currentState_B = currentState;
	n_currentState_B.pilesB.push_back(candy);
	n_currentState_B.pilesBSum = currentState.pilesBSum ^ candy;
	generatePiles(n_freeCandies, n_currentState_B, bestState, possibleMaximum);
}


int main(int argc, char** argv)
{
	register unsigned char i, j, k;		// index variables
	register int l;

	unsigned char T; 		// number of test cases
	unsigned char N; 		// number of candies

	std::vector <int> candies;


	FILE* input = fopen("C-small-attempt0.in", "r");
	if (input == NULL) {
		std::cerr << "Error while opening input file..";
		return -1;
	}

	FILE* output = fopen("C-small-attempt0.out", "w");
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

		candies.clear();

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



		/* Make calculations */


		/* Skip empty parts in the line */
		while(k == ' ' || k == '\t' || k == '\r' || k == '\n') {
			fread(&k,1,1,input);
		}

		for (j = 0; j < N; j++) {

			l = 0;
			while('0' <= k && k <= '9' ) {
				l = l*10 + k - '0';
				fread(&k,1,1,input);
				if (feof(input)) {
					break;
				}
			}
			candies.push_back(l);

			while(k == ' ' || k == '\t') {
				fread(&k,1,1,input);
				if (feof(input)) {
					break;
				}
			}
			if (feof(input)) {
				break;
			}
		}

		std::vector<int> pilesA;
		std::vector<int> pilesB;

		State currentState = {pilesA, pilesB, 0,0};
		State *bestState = NULL;

		sort(candies.begin(), candies.end());
		int possibleMaximum = 0;
		for (unsigned int i = 1; i<candies.size(); i++) {
			possibleMaximum += candies.at(i);
		}

		generatePiles(candies, currentState, &bestState, possibleMaximum);

		if (bestState == NULL) {
			fprintf(output, "Case #%u: NO\n", (unsigned int)i + 1);
			std::cout << "Case #" << (unsigned int)i + 1 << ": NO" << std::endl;
		} else {
			fprintf(output, "Case #%u: %d\n", (unsigned int)i + 1, bestState->pilesASum);
			std::cout << "Case #" << (unsigned int)i + 1 << ": " << bestState->pilesASum << std::endl;
		}

		delete bestState;

		std::cout << (unsigned int)T << "/" << (unsigned int)i << ". test case ends.." << std::endl << std::endl;
	}

	fclose(input);
	fclose(output);

	return 0;
}
