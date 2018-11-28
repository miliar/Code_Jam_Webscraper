#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
	int l, d, n;
	cin >> l >> d >> n;
	vector<string> language;
	for(int i = 0; i < d; i++) {
		string word;
		cin >> word;
		language.push_back(word);
	}
	for(int i = 0; i < n;) {
		string pattern;
		cin >> pattern;
		int matches = 0;
		for(int j = 0; j < d; j++) {
			int patternpos = 0, k = 0;
			for(; k < l; k++) {
				bool matched = false;
				if(pattern[patternpos] == '(') {
					while(pattern[++patternpos] != ')')
						if(pattern[patternpos] == language[j][k]) {
							matched = true;
							while(pattern[++patternpos] != ')');
							break;
						}
					patternpos++;
				} else {
					if(pattern[patternpos++] == language[j][k])
						matched = true;
				}
				if(!matched) break;
			}
			if(k == l) matches++;
		}
		cout << "Case #" << ++i << ": " << matches << endl;
	}
	return 0;
}
