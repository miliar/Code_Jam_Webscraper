#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <numeric>

using namespace std;

int solve( vector<int>& sequences) 
{
	int ret = 0;
	for (int i = 0; i < sequences.size(); ++i) {
		if (sequences[i] != i+1) {
			++ret;
		}
	}
	return ret;
}

int main(int argc, char* argv[]) {
	int numOfCases;
	int curCase = 1;
	cin >> numOfCases;
	for (;curCase <= numOfCases; ++curCase) {
		int numOfSeq;
		cin >>numOfSeq;
		vector<int> sequences;
		for (int i = 0; i < numOfSeq; ++i) {
			int val;
			cin >> val;
			sequences.push_back(val);
		} // for (int i = 0; i < numOfSeq; ++i)
		int result = solve(sequences);
		cout << "Case #" <<curCase << ": " << result <<".000000" <<endl;
	}
}