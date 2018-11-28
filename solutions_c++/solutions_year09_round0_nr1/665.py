#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>

using namespace std;

int match(const string& pattern, const string& word) {
	size_t cp=0,cw=0;
	while(cw < word.length()) {
		if (pattern[cp] == '(') {
			bool matched = false;
			cp++;
			while (pattern[cp] != ')') {
				matched |= (pattern[cp] == word[cw]);
				cp++;
			}
			cp++; cw++;
			if (!matched)
				return 0;
		}
		else if (pattern[cp] == word[cw]) {
			cp++; cw++;
		}
		else
			return 0;
	}
	return 1;
}

int match(const string& pattern, const vector<string>& words) {
	int res = 0;
	for (size_t i=0;i<words.size();i++)
		res += match(pattern, words[i]);
	return res;
}

int main() {
	int L,D,N;
	vector<string> words;

	cin >> L >> D >> N;
	
	for (int i=0;i<D;i++) {
		string word;
		cin >> word;
		words.push_back(word);
	}
	
	for (int i=1;i<=N;i++) {
		string pattern;
		cin >> pattern;
		cout << "Case #" << i << ": " << match(pattern, words) << endl;
	}

	return 0;
}
