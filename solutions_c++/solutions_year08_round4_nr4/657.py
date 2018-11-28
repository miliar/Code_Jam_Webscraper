#include <iostream>
#include <vector>

using namespace std;


const int MAX_S = 4000;


int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		int K;
		string S;
		
		cin >> K;
		cin >> S;

		vector<int> perm;
		for (int i = 1; i <= K; i++) {
			perm.push_back(i);
		}

		int len = S.length();
		int ret = len + 7;
		char after[MAX_S];
		do {
			
			for (int start = 0; start < len; start += K) {
				for (int permPos = 0, afterPos = start; permPos < K; permPos++, afterPos++) {
					int p = perm[permPos];
					char ch = S[start + p - 1];
					after[afterPos] = ch;
				}
			}

			int cur = 1;
			for (int pos = 1; pos < len; pos++) {
				if (after[pos] != after[pos - 1]) cur++;
			}
			
			if (cur < ret) ret = cur;

		} while (next_permutation(perm.begin(), perm.end()));

		cout << "Case #" << t << ": " << ret << endl;
	}

	return 0;
}
			
