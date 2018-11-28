#include <stdio.h>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<string> dictionary, candidates;

bool Try(string &s){
	for(int i = 0; i < s.length(); i++)
		if(candidates[i].find(s[i]) == string::npos)
			return false;
	return true;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.txt", "w", stdout);

    int L, D, N;
    cin >> L >> D >> N;
    for (int i = 0; i < D; i++) {
        string s;
        cin >> s;
        dictionary.push_back(s);
    }

    for (int n = 1; n <= N; n++) {
		string pattern;
        cin >> pattern;
		candidates.clear();
		for(int i = 0; i < pattern.length(); i++){
			if(pattern[i] == '('){
				int e = pattern.find(')', i + 1);
				candidates.push_back(pattern.substr(i + 1, e - (i + 1)));
				i = e;
			}
			else if(pattern[i] >= 'a' && pattern[i] <= 'z')
				candidates.push_back(pattern.substr(i, 1));
		}
        
		int cnt = 0;
		for(int i = 0; i < D; i++)
			if(Try(dictionary[i]))
				cnt++;

		cout << "Case #" << n << ": " << cnt << endl;
    }

    return 0;
}
