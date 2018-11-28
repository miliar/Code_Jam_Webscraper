#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

class SnapperChain {
public:
	int solve(int n, unsigned long long k)
	{
		unsigned long long dev = 0;
		for (int i = 0; i < n; i++)
			dev |= 1ULL << i;
		if ((dev & k) == dev) return true;
		return false;
	}
};

int main()
{
//	fstream fs("test.in", ios_base::in);
	fstream fs("A-large.in", ios_base::in);
	string line;
	stringstream ss;

	SnapperChain sc;

	getline(fs, line);
	ss.str(line);
	int T, N, K;
	ss >> T;
	ss.clear();  ss.str("");
	int cnt = 0;
	for (int i = 0; i < T; i++) {
		getline(fs, line);
		ss.str(line);
		ss >> N >> K;
		ss.clear();  ss.str("");
		cout << "Case #" << ++cnt << ": " << (sc.solve(N, K) ? "ON" : "OFF") << endl;
	}

	return 0;
}
