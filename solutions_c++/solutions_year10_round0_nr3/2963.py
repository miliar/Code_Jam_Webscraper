#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

void main() {

	ofstream myFile;
	myFile.open ("out.out");
	ifstream in("C-small-attempt0.in");

	int turns;
	in >> turns;

	for (int t = 1; t <= turns; t++) {
		unsigned int R;
		unsigned int k;
		unsigned int* q;
		unsigned int N;

		in >> R >> k >> N;

		q = new unsigned int[N];

		for (int i = 0; i < N; i++) {
			in >> q[i];
		}

		unsigned int totalMoney = 0;

		unsigned int currentHead = 0;

		for (unsigned int rideNum = 0; rideNum < R; rideNum++) {
			unsigned int currOnBoard = 0;
			for (unsigned int i = 0; i < N; i++) {
				if (currOnBoard + q[currentHead] <= k) {
					currOnBoard += q[currentHead];
					totalMoney += q[currentHead];
					currentHead = (currentHead + 1) % N;
				} else {
					break;
				}
			}
		}

		myFile << "Case #" << t << ": " << totalMoney << endl;
		cout << t << endl;
	}

}

