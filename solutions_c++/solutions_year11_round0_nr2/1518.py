#include <cstdio>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

struct combine {
	char map[26][26];
	combine() {
		for (int i=0; i<26; i++) 
			for (int j=0; j<26; j++)
				map[i][j]=0;
	}
	void operator()(char x, char y, char c) {
		map[x-'A'][y-'A'] = c;
	}
	char operator()(char x, char y) {
		return map[x-'A'][y-'A'];
	}
};

struct opposed {
	bool map[26][26];
	opposed() {
		for (int i=0; i<26; i++) 
			for (int j=0; j<26; j++)
				map[i][j]=false;
	}
	void set(char x, char y) {
		map[x-'A'][y-'A'] = true;
	}
	bool operator()(char x, char y) {
		return map[x-'A'][y-'A'];
	}
};

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int C, D, N;
		string s;
		combine comb;
		opposed opps;		
		cin >> C;
		for (int k = 0; k < C; k++) {
			cin >> s;
			comb(s[0],s[1],s[2]);
			comb(s[1],s[0],s[2]);
		}
		cin >> D;
		for (int k = 0; k < D; k++) {
			cin >> s;
			opps.set(s[0],s[1]);
			opps.set(s[1],s[0]);
		}
		cin >> N;
		cin >> s;
		vector<char> el;
		for (int j=0; j<s.length();j++) {
			if (el.empty()) {
				el.push_back(s[j]);
				continue;
			}	
			char ne = s[j];
			while (!el.empty() && comb(el.back(),ne)!=0) {
				ne = comb(el.back(), s[j]);
				el.pop_back();
			}

			el.push_back(ne);
			for (int k=0; k<el.size()-1; k++) {
				if (opps(el[k],ne)) {
					el.clear();
					break;
				}	
			}
		}

		printf("Case #%d: [", i+1);
		for (int k = 0; k < el.size(); k++) {
			printf("%c", el[k]);
			if (k == el.size()-1)
				break;
			printf(", ");
		}
		printf("]\n");
	}
}

