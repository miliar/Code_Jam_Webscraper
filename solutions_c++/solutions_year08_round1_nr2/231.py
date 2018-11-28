/*
 * q2.cpp
 *
 *  Created on: Jul 25, 2008
 *      Author: AliJ
 */




#include <iostream>
#include <string>



using namespace std;

void processCase(int caseNum) {
	int N;
	cin >> N;
	int M;
	cin >> M;
	int* truth = new int[N];
	int impossible  = 0;

	for (int i = 0; i < N; i++){
		truth[i] = 0;
	}

	int* malted = new int[M];
	int* numUnmalted = new int[M];
	int* happy = new int[M];

	for (int j = 0; j < M; j++) {
		malted[j] = -1;
		happy[j] = 0;
		numUnmalted[j] = 0;
	}

	int** unmalted = new int*[M];

	//Read stuff in.
	int k;
	for (k = 0; k < M; k++) {
		int T;
		cin >> T;
		numUnmalted[k] = T;
		unmalted[k] = new int[T];
		for (int k2 = 0; k2 < T; k2++){
			int X, Y;
			cin >> X;
			X--;
			cin >> Y;
			if (Y==0) {
				unmalted[k][k2] = X;
			}
			else {
				unmalted[k][k2] = -1;
				malted[k] = X;
			}
		}
	}

	int done = 0;

	for (int round = 0; round < N; round++) {
		done = 1;
		for (int cust = 0; cust < M; cust++) {
			if (happy[cust]==0) {
				if ((malted[cust] != -1) && (truth[malted[cust]]== 1)) {
					happy[cust] = 1;
					continue;
				}
				int allUnmaltedTrue = 1;
				for (k = 0; k < numUnmalted[cust]; k++) {
					if ((unmalted[cust][k] != -1) && (truth[unmalted[cust][k]] == 0)) {
						allUnmaltedTrue = 0;
						break;
					}
				}
				if (allUnmaltedTrue == 1) {
					if (malted[cust]== -1) {
						impossible = 1;
						break;
					} else {
						truth[malted[cust]] = 1;
						happy[cust] = 1;
						done = 0;
						break;
					}

				}
			}
		}

		if ((done == 1) || (impossible == 1)) {
			break;
		}

	}

	// don't already know it's impossible, so make sure we satisfy.
	if (impossible == 0) {
		for (int cust = 0; cust < M; cust++) {
			if (happy[cust]==0) {
				int allUnmaltedTrue = 1;
				for (k = 0; k < numUnmalted[cust]; k++) {
					if ((unmalted[cust][k] != -1) && (truth[unmalted[cust][k]] == 0)) {
							allUnmaltedTrue = 0;
							break;
					}
				}
				if (allUnmaltedTrue == 1) {
					if ((malted[cust]== -1) || (truth[malted[cust]]==0)) {
						impossible = 1;
						break;
					}

				}
			}
		}


	}

	if (impossible == 1) {
		cout << "Case #" << caseNum << ": " << "IMPOSSIBLE" << endl;
	} else {
		cout << "Case #" << caseNum << ": ";
		for (k = 0; k < N; k++) {
			cout << truth[k] << " ";
		}
		cout << endl;
	}

	// free memory;

	for (k = 0; k < M; k++) {
		delete [] unmalted[k];
	}

	delete [] unmalted;
	delete [] malted;
	delete [] numUnmalted;
	delete [] happy;
	delete [] truth;


}


int main() {

	// HORN-SAT!
	int numCases;

	cin >> numCases;


	for (int i = 0; i < numCases; i++) {
		processCase(i+1);

	}

	return 0;
}
