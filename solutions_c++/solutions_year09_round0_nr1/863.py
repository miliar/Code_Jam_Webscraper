#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int mask(char c) {
	return 1 << (c-'a');
}

int count_match(int l, const string& pattern, const vector<string>& dict) {
	vector<int> pat(l);
	//compile the pattern
	for (int i=0, j=0; i<l; i++, j++) {
		if (pattern[j] == '(') {
			while (pattern[++j] != ')') {
				pat[i] |= mask(pattern[j]);
			}
		} else 
			pat[i] = mask(pattern[j]);
	}

	int cnt = 0;
	for (size_t i=0; i<dict.size(); i++) {
		size_t j;
		for (j=0; j<l && pat[j] & mask(dict[i][j]); j++);
		cnt += j==l;
	}
	return cnt;
}

int main() {
	ios_base::sync_with_stdio(false);
	int l, d, n;
	cin >> l >> d >> n;
	vector<string> dict(d);
	for (int i=0; i<d; i++) 
		cin >> dict[i];
	for (int t=1; t<=n; t++) {
		string pattern;
		cin >> pattern;
		cout << "Case #" << t << ": " << count_match(l, pattern, dict) << "\n";
	}
	return 0;
}
