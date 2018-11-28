// A C++ program for solving Google Code Jam 2010, Round 1, Problem 3.

#include <queue>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

void InitRide(ifstream &infile, int &R, int &k, int &N, queue<int> &Q) {
	// Obtain R, k and N.
	string line;
	getline(infile, line);
	stringstream(line) >> R >> k >> N;
	// cout << "DEBUG: " << R << " " << k << " " << N << endl;
	// Obtaining the groups.
	getline(infile, line);
	stringstream SS(line);
	for (int j = 0 ; j < N ; ++j) {
		int nextGroupSize;
		SS >> nextGroupSize;
		Q.push(nextGroupSize);
	}
	// cout << "DEBUG: " << Q.front() << " " << Q.size() << endl;
}

int CalcEuros(const int R, const int k, const int N, queue<int> &Q) {
	int profit = 0;
	// One iteration per ride.
	for (int i = 0 ; i < R ; ++i) {
		// Trying to fit as many groups as possible to this ride. Stopping when all groups fit in or when not enough seats for the next group.
		int remainingSeats = k;
		for (int j = 0 ; j < N ; ++j) {
			int nextGroup = Q.front();
			// If the next group cannot fit in, this ride is full.
			if (nextGroup > remainingSeats)
				break;
			// The group fits in, so deducting it from the number of remaining seats, collecting profit and moving it to the end of the queue.
			remainingSeats -= nextGroup;
			profit += nextGroup;
			Q.pop();
			Q.push(nextGroup);
		}
	}
	return profit;
}

int main(int argc, char *argv[]) {
	ifstream infile(argv[1]);
	if (!infile.is_open()) {
		cout << "ERROR: could not open " << argv[1] << endl;
		return 1;
	}
	// The line first has the number of test cases.
	string line;
	getline(infile, line);
	int numCases;
	stringstream(line) >> numCases;
	for (int i = 1 ; i <= numCases ; ++i) {
		int R, k, N;
		queue<int> Q;
		InitRide(infile, R, k, N, Q);
		const int profit = CalcEuros(R, k, N, Q);
		cout << "Case #" << i << ": " << profit << endl;
	}
	// Repeating until there are no more test cases
	return 0;
}
