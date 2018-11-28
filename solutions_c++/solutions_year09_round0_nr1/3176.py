#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

const int MAX_WORDS = 10000;
vector<string> words(MAX_WORDS);

vector<string> parse(const string& phrase) {
	vector<string> ret;
	for (int i = 0; i < phrase.size(); ++i) {
		if (isalpha(phrase[i])) {
			ret.push_back(string(1, phrase[i]));
		} else {
			++i;
			string concat;
			while (isalpha(phrase[i])) {
				concat += phrase[i++];
			}
			ret.push_back(concat);
		}
	}
	return ret;
}

int main () {

	freopen("alien.txt", "r", stdin);
	freopen("alien.out", "w", stdout);
	int l, d, n;
	cin >> l >> d >> n;
	for (int i = 0; i < d; ++i) {
		cin >> words[i] ;
	}
	// for every expression
	int cases = 1;
	for (int i = 0; i < n; ++i) {
		string phrase;
		cin >> phrase;
		vector<string> parsed = parse(phrase);
		vector<bool> good(d, true);
		// iterate through all the phrase
		for (int j = 0; j < l; ++j) {
			// for each word check if it is still valid
			for (int k = 0; k < d; ++k) {
				if(!good[k]) continue;
				// check the possible combinations of this word.
				bool ok = false;
				for (int a = 0; a < parsed[j].size(); ++a) {	
					string aux = words[j];
					if (parsed[j][a] == words[k][j]) {
						ok = true;
						break;
					}
				}
				if (!ok) good[k] = false;
			}
		}
		int count = 0;
		for (int j = 0; j < good.size(); ++j) {
			if (good[j]) ++count;
		}
		printf("Case #%d: %d\n", cases++, count);
	}
}