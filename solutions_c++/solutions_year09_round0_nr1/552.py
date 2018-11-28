#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
using namespace std;

#define REP(i, n) for(int i = 0; i<(n); i++)
#define abs(a) ((a) >= 0 ? (a) : -(a))
#define inf 2000000001
typedef vector<int> VI;
typedef vector<string> VS;

typedef long long i64;
typedef unsigned long long u64;

int l, d, n;
VS words;

bool match(string &word, VS &terms) {
	REP(i, word.size()) {
		if (terms[i].find(word[i]) == -1) return false;
	}
	return true;
}

int main() {
	cin>>l>>d>>n;
	REP(i, d) {
		string str;
		cin>>str;
		words.push_back(str);		
	}
	
	REP(t, n) {
		string p;
		cin>>p;
		VS terms;
		int cur = 0;
		REP(j, l) {
			string term = "";	
			if (p[cur] == '(') {
				for (; ;cur++) {
					if (p[cur] == ')') break;
					term += p[cur];
				}
			} else {
				term += p[cur];
			}
			terms.push_back(term);
			cur++;
		}
	
		
		int ret = 0;
		REP(i, words.size()) {
			if (match(words[i], terms)) ret++;
		}
		
		cout << "Case #" << t + 1 << ": " << ret <<endl;
	}
	return 0;
}