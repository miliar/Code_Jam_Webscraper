#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <cmath>
#include <utility>
#include <cassert>

using namespace std;

int main() {
	int N; cin >> N;
	for (int i = 0; i < N; i++) {
		int k; string S; cin >> k >> S;
		vector<int> perm;
		int best = 999999;
		for (int j = 0; j < k; j++) perm.push_back(j+1);
		do {
			string T(S.size(),'-');
			for (int j = 0; j < S.size(); j++) {
				int group = j / k;
				T[j] = S[group*k + perm[j % k] - 1];
			}
			char last = '{';
			int cnt = 0;
			for (int j = 0; j < T.size(); j++) {
				if (T[j] != last) {
					cnt++;
					last = T[j];
				}
			}
			best = min(best,cnt);
		} while (next_permutation(perm.begin(),perm.end()));
		cout << "Case #" << i+1 << ": " << best << "\n";
	}
	return 0;
}