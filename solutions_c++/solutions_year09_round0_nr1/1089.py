#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
using namespace std;

const int MAX_L = 100;
const int MAX_D = 5010;

int l, d, n;
string pattern;
string word[MAX_D];

bool check(const string &pattern, const string &word) {
	bool hash[256] = {0};
	for (int i = 0, j = 0; i < word.length(); i++, j++) {
		memset(hash, 0, sizeof(hash));

		if (pattern[j] == '(') {
			j++;
			while (pattern[j] != ')')
				hash[pattern[j++]] = true;
		}
		else {
			hash[pattern[j]] = true;
		}

		if (!hash[word[i]])
			return false;
	}
	return true;
}

int main() {
	cin >> l >> d >> n;
	for (int i = 0; i < d; i++)
		cin >> word[i];

	int t = 0;
	while (cin >> pattern) {
		int cnt = 0;
		for (int i = 0; i < d; i++)
			if (check(pattern, word[i]))
				cnt++;
		printf("Case #%d: %d\n", ++t, cnt);
	}
}
