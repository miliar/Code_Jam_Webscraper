#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <cassert>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

int main(int argc, char* argv[])
{
	if (argc != 2)
		return 1;

	ifstream ifs(argv[1]);
	string dummy;

	int T;
	ifs >> T;
	getline(ifs, dummy);

	for (int testCase = 0; testCase < T; ++testCase) {
		cerr << "Case #" << testCase + 1 << "..." << endl;

		string str;
		getline(ifs, str);
		set<char> digits;
		for (int i = 0; i < (int)str.size(); ++i) {
			digits.insert(str[i]);
		}

		__int64 base = digits.size();
		if (base < 2)
			base = 2;
		__int64 powN = 1;
		for (int i = 0; i < (int)str.size() - 1; ++i) {
			powN *= base;
		}

		__int64 remainTime = powN;
		map<char, __int64> digitMap;
		digitMap.insert(make_pair(str[0], __int64(1)));
		powN /= base;
		__int64 next = 0;
		for (int i = 1; i < (int)str.size(); ++i) {
			map<char, __int64>::const_iterator it = digitMap.find(str[i]);
			if (it == digitMap.end()) {
				remainTime += powN * next;
				digitMap.insert(make_pair(str[i], next));
				if (next == 0)
					next = 2;
				else
					++next;
			}
			else {
				remainTime += powN * it->second;
			}
			powN /= base;
		}

		// output
		cout << "Case #" << testCase + 1 << ": " << remainTime << endl;
	}

	return 0;
}
