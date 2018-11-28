// Q2

// MACROS
#define MAX(A,B) (A > B) ? A : B;
#define PRINT(X, K) cout << "Case #" << X << ": "; cout << setfill ('0') << setw (4) << (K%10000) << endl;
#define FOREACH(T, I, J) for (T::iterator I = J.begin(); I != J.end(); ++I)
#define FOREACH_CONST(T, I, J) for (T::const_iterator I = J.begin(); I != J.end(); ++I)

#include <iostream>
#include <iomanip>
#include <string>
#include <map>
#include <utility>

using namespace std;

typedef unsigned** MappingCount;

unsigned countSubsequence(unsigned **mapping, bool **visits, string &base, string &haystack, unsigned baseIndex, unsigned hayIndex) {

	unsigned count(0);
	char c = base[baseIndex];
	while((hayIndex = haystack.find(c, hayIndex)) != string::npos) {
		if ((baseIndex + 1) == base.size()) {
			count++;
		} else {
			if (!visits[baseIndex][hayIndex]) {
				unsigned c = countSubsequence(mapping, visits, base, haystack, baseIndex+1, hayIndex+1);
				mapping[baseIndex][hayIndex] += c;
				visits[baseIndex][hayIndex] = true;
			}
			count += mapping[baseIndex][hayIndex];
		}
		++hayIndex;
	}

	return count;

}

int main(void) {

	/**
	 * N = number of test cases
	 */
	unsigned N;
	cin >> N;

	string base;
	// dummy get new line for trailing after N
	getline(cin, base);

	base = "welcome to code jam";

	for (unsigned i = 0; i != N; ++i) {
		string s;
		getline(cin, s);

		unsigned bs = base.size(), ss = s.size();
		MappingCount mapping = new unsigned*[bs];
		bool **visits = new bool*[bs];
		for (unsigned si = 0; si != bs; ++si) {
			mapping[si] = new unsigned[ss];
			visits[si] = new bool[ss];
			for (unsigned sii = 0; sii != ss; ++sii) {
				mapping[si][sii] = 0;
				visits[si][sii] = false;
			}
		}

		unsigned c = countSubsequence(mapping, visits, base, s, 0, 0);
		PRINT(i+1,c);

	}

	return 0;

}
