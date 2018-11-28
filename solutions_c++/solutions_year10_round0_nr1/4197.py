#include <iostream>
#include <fstream>
#include <vector>

using namespace std;
int main(int argc, char **argv) {
	ifstream inputFile("A-small-attempt.in", ios_base::in);
	ofstream outputFile("output.txt", ios_base::out);
	int noOfCases, N, K;

	inputFile >> noOfCases;
	for (int caseNo = 0; caseNo < noOfCases; caseNo++) {
		inputFile >> N >> K;
		vector<bool> prevSnapperState;
		vector<bool> currentSnapperState;
		for (int i = 0; i < N; i++) {
			prevSnapperState.push_back(false);
			currentSnapperState.push_back(false);
		}

		for (int i = 0; i < K; i++ ) {
			currentSnapperState[0] = ! prevSnapperState[0];
			for (int j = 1; j < N; j++ ) {
				bool isActive = true;
				for (int k = 0; k < j; k++) {
					if (!prevSnapperState[k]) {
						isActive = false;
						break;
					}
				}
				if (isActive) {
					currentSnapperState[j] = !prevSnapperState[j];
				} else {
					break;
				}
			}
			prevSnapperState = currentSnapperState;
		}
		bool isActive = true;
		for (int k = 0; k < N; k++) {
			if (!prevSnapperState[k]) {
				isActive = false;
				break;
			}
		}		
		outputFile << "Case #" << (caseNo+1) << ": " << (isActive? "ON":"OFF") << endl;
	}
}
