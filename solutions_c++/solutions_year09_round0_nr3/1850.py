#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <cassert>
#include <algorithm>
#include <iomanip>

using namespace std;

template <class FwdIt1, class FwdIt2> inline
int GetPatternCount(FwdIt1 itInB, FwdIt1 itInE, FwdIt2 itFB, FwdIt2 itFE, int curCount = 0)
{
	if ((itInB == itInE) || (itFB == itFE))
		return curCount;

	FwdIt2 itFN = itFB;
	++itFN;
	for (FwdIt1 it = find(itInB, itInE, *itFB); it != itInE; it = find(it, itInE, *itFB)) {
		++it;
		if (itFN == itFE)
			++curCount;
		else
			curCount = GetPatternCount(it, itInE, itFN, itFE, curCount);
	}

	return curCount % 10000;
}

int main(int argc, char* argv[])
{
	if (argc != 2)
		return 1;

	ifstream ifs(argv[1]);
	string dummy;

	int N;
	ifs >> N;
	getline(ifs, dummy);

	const string welcome("welcome to code jam"); 
	for (int n = 0; n < N; ++n) {
		int total = 0;
		string input;
		getline(ifs, input);

		// output
		cout << "Case #" << n + 1 << ": "
			<< setw(4) << setfill('0') << GetPatternCount(input.begin(), input.end(), welcome.begin(), welcome.end()) << endl;
	}

	return 0;
}
