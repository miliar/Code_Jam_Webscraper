#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <set>
#include <string>
#include <list>
#include <map>
#include <cmath>

using namespace std;

int L, D, N;
vector<string> words;

void solve() {
	string pattern;
	cin >> pattern;
	bool match[256][256];
	memset(match, false, sizeof(match));

	int pos = 0;
	for(int i = 0; i < pattern.size(); i++) {
		if(pattern[i] == '(') 
			while(pattern[++i] != ')') 
				match[pos][pattern[i]] = true;				
		 else match[pos][pattern[i]] = true;	
		pos++;
	}

	int result = 0;
	for(int i = 0; i < words.size(); i++) {
		bool ok = true;
		for(int j = 0; j < words[i].size(); j++) {
			if(!match[j][words[i][j]]) {
				ok = false;
				break;
			}
		}
		if(ok) result++;
	}
	cout << result;
}




int main() {		
	cin >> L >> D >> N;
	for(int i = 0; i < D; i++) {
		string word;
		cin >> word;
		words.push_back(word);
	}
	for(int i = 1; i <= N; i++) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
}