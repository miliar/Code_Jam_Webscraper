#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> makePatternMask(string& word) {
	vector<int> result = vector<int>(0, word.size());
	for (int i = 0; i < word.size(); i++) {
		int mask = 0;
		if (word[i] == '(') {
			while (word[++i] != ')')
				mask |= 1 << (word[i] - 'a');
		} else {
			mask = 1 << (word[i] - 'a');
		}
		result.push_back(mask);
	}
	return result;
}

bool patternMatch(vector<int>& word, vector<int>& pattern) {
	for (int i = 0; i < word.size(); i++) 
		if (!(word[i] & pattern[i])) 
			return false;
	return true;
}

int main (int argc, char * const argv[]) {
	int L, D, N;
	string line;

	cin >> L >> D >> N;
	getline(cin, line);
	
	vector<vector<int> > dict;
	for (int i = 0; i < D; i++) {
		getline(cin, line);
		dict.push_back(makePatternMask(line));
	}
	
	for (int i = 0; i < N; i++ ) {
		getline(cin, line);
		vector<int> pattern = makePatternMask(line);
		int count = 0;
		for (int j = 0; j < D; j++) 
			if (patternMatch(dict[j], pattern)) 
				count++;
		cout << "Case #" << i + 1 << ": " << count << endl;
	}
	
    return 0;
}
