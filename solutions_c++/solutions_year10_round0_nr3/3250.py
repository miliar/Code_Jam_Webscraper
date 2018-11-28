/*
 *  ProblemC.cpp
 *  CodeJam10
 *
 *  Created by Victor Ochikubo on 5/8/10.
 *  Copyright 2010 Stanford University. All rights reserved.
 *
 */



#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <fstream>
#include <numeric>

using namespace std;

const string INPUT_FILE = "C-small-attempt0.in";
const string OUTPUT_FILE = "C-small.out";

template <typename T>
void PrintVector(vector<T>& vec) {
	for (int i = 0; i < vec.size(); ++i) {
		cout << vec[i] << endl;
	}
}

int GetNumCases(ifstream& infile) {
	stringstream sstream;
	string n_str;
	getline(infile, n_str);
	sstream.str(n_str);
	int retval;
	sstream >> retval;
	return retval;
}

struct IntTrip {
	int R; // number of rides
	int k; // number of people that fit at once
	int N; // number of grops
};

IntTrip GetTriple(ifstream& infile) {
	stringstream sstream;
	string triple_str;
	getline(infile, triple_str);
	sstream.str(triple_str);
	IntTrip newTrip;
	sstream >> newTrip.R >> newTrip.k >> newTrip.N;
	return newTrip;
}

int FindFirstLoop(vector<int>& positionOrders, int& cycleLength) {
	vector<int>::iterator result;
	for (int i = 0; i < positionOrders.size(); ++i) {
		result = find(positionOrders.begin() + i + 1, positionOrders.end(), positionOrders[i]);
		if (result == positionOrders.end()) {} // must not have been the right number
		else {
			cycleLength = result - positionOrders.begin();
			cycleLength -= i;
			return i;
		}
	}
	return -1; // should never get here
}

int FindAmount(ifstream& infile, IntTrip& trip) {
	stringstream sstream;
	string groupsStr;
	getline(infile, groupsStr);
	sstream.str(groupsStr);
	
	vector<int> groups;
	int groupSize;
	// Reads in a list of the groups
	for (int i = 0; i < trip.N; ++i) {
		sstream >> groupSize;
		groups.push_back(groupSize);
	}
	
	// Iterate through the groups and make a new vector to find the cycles
	vector<int> positionOrders;
	vector<int> numCanRide;
	int currPos = 0;
	positionOrders.push_back(currPos);
	for (int i = 0; i < (trip.N + 1); ++i) {
		int numOnRide = 0;
		int startPos = currPos;
		while (numOnRide + groups[currPos] <= trip.k) {
			numOnRide += groups[currPos];
			++currPos;
			if (currPos >= groups.size()) currPos = 0;
			if (currPos == startPos) break; // can't have the same group be on it twice
		}
		numCanRide.push_back(numOnRide);
		positionOrders.push_back(currPos);
	}
	
	// numCanRide is one element shorter than positionOrders
	
	//cout << "Num can ride are : " << endl;
	//PrintVector(numCanRide);
	
	//cout << "Position orders are : " << endl;
	//PrintVector(positionOrders);
	
	// Find the first one that loops
	int cycleLength;
	int firstCycleBeginIndex = FindFirstLoop(positionOrders, cycleLength);
	if (firstCycleBeginIndex == -1) cout << "An error occured in FindFirstLoop" << endl;
	
	//cout << "firstCycleBeginIndex = " << firstCycleBeginIndex << " cycleLength = " << cycleLength << endl;
	
	// calculate the first, before the cycle
	// divide however many rides are left by the cycle length, add total sum of that * numCycles
	// then go through one at a time, starting at firstCycleBeginIndex
	
	int numDollarsMade = 0;
	for (int i = 0; i < firstCycleBeginIndex; ++i) {
		numDollarsMade += numCanRide[i];
		--trip.R;
		if (trip.R == 0) return numDollarsMade;
	}
	
	int numCycles = trip.R / cycleLength;
	int oneCycleMoney = accumulate(numCanRide.begin() + firstCycleBeginIndex, numCanRide.begin() + firstCycleBeginIndex + cycleLength, 0);
	numDollarsMade += numCycles * oneCycleMoney;
	trip.R -= numCycles * cycleLength;
	int leftOverCurr = firstCycleBeginIndex;
	while (trip.R > 0) {
		numDollarsMade += numCanRide[leftOverCurr];
		++leftOverCurr;
		--trip.R;
	}
	
	return numDollarsMade;
}

int main(int argc, char *argv[]) {
	ifstream infile(INPUT_FILE.c_str());
	ofstream outfile(OUTPUT_FILE.c_str());
	if (infile.fail()) cout << "infile failed" << endl;
	int num_cases = GetNumCases(infile);
	
	for (int i = 0; i < num_cases; ++i) {
		IntTrip trip = GetTriple(infile);
		int numDollars = FindAmount(infile, trip);
		outfile << "Case #" << i + 1 << ": " << numDollars << endl;
	}
	
	infile.close();
	outfile.close();
	
}


// memoize? starting at each position, the number of people that go
// then just update the position that you're looking up
// should eventually be a multiple of each number because it cycles
// maybe it doesn't cycle? maybe the beginning never gets reached again but otherwise it cycles
// 1 4 2 1 , k = 6
// starts at 0 (about to ride)
// then sequence is: 0 2 1 3 2 1 3 go n + 1 look at where it repeats?
// linear search forward for the first number that appears more than once
// then subtract all the rides and all the money that comes before the repeat
// and cut off everything that comes afterwards

// roller coaster holds k people at once
// runs R times
// let N be the number of groups that queue
// and let g_i be the size of each group (N groups)

// make a vector of the groups g_i