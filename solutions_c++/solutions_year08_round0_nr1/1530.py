#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <limits>

using namespace std;

int main() {
	int N;
	cin >> N;

	for (int caseNo = 1; caseNo <= N; ++caseNo) {
		int S;
		cin >> S;
		cin.ignore(numeric_limits<int>::max(), '\n');

		vector<string> engines(S);
		map<string, int> engineIndices;
		for (int i = 0; i < S; ++i) {
			getline(cin, engines[i]);
			engineIndices[engines[i]] = i;
		}

		int Q, curDefault = 1;
		int seenCount = 0;
		int s[105] = {0};

		cin >> Q;
		cin.ignore(numeric_limits<int>::max(), '\n');
		for (int i = 0; i < Q; ++i) {
			string str;
			getline(cin, str);
			int index = engineIndices[str];
			if (s[index] < curDefault) {
				++s[index];
				++seenCount;

				if (seenCount == S) {
					++s[index];
					++curDefault;
					seenCount = 1;
				}
			}
		}

		cout << "Case #" << caseNo << ": " << curDefault - 1 << endl;
	}
}
