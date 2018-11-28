#include <iostream>
#include <fstream>
#include <list>

using namespace std;
int main(int argc, char **argv) {
	ifstream inputFile("C-small.in", ios_base::in);
	ofstream outputFile("output.txt", ios_base::out);
	int noOfCases, noOfRides, cap, N;
	list<int> groups;

	inputFile >> noOfCases;
	for (int caseNo = 0; caseNo < noOfCases; caseNo++) {
		groups.clear();
		inputFile >> noOfRides >> cap >> N;
		for (int groupNo = 0; groupNo < N; groupNo++) {
			int size;
			inputFile >> size;
			groups.push_back(size);
		}
		int income = 0;
		for (int i = 0; i < noOfRides; i++ ) {
			int noOfPersons = 0;
			int embarkedGroups = 0;
			while (1) {
				if (noOfPersons + groups.front() > cap) break;
				int firstGroupSize = groups.front();
				groups.pop_front();
				groups.push_back(firstGroupSize);
				noOfPersons += firstGroupSize;
				embarkedGroups++;
				if (embarkedGroups == N) break;
			}
			income += noOfPersons;
		}
		outputFile << "Case #" << (caseNo+1) << ": " << income << endl;
	}
}
