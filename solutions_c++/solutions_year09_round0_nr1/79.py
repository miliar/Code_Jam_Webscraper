#include <iostream>
#include <string>
#include <set>
#include <vector>

#define FOR(i,a,b) for(int i=a; i<(b); i++)

using namespace std;

vector< set<char> > parsePattern(string& pattern) {
	vector< set<char> > ret(pattern.size());
	int p=0;
	bool nawias = false;
	FOR(i,0,pattern.size()) {
		if(pattern[i] == '(') nawias = true;
		else if(pattern[i] == ')') nawias = false;
		else {
			ret[p].insert(pattern[i]);
		}
		if(!nawias) p++;
	}
	return ret;
}

bool fitsPattern( vector< set<char> >& p, string& s ) {
	FOR(i,0,s.size()) {
		if(p[i].find(s[i]) == p[i].end()) {
			return false;
		}
	}
	return true;
}

int main() {
	int L, D, N;
	cin >> L >> D >> N;
	vector< string > we;
	FOR(i,0,D) {
		string s;
		cin >> s;
		we.push_back(s);
	}
	FOR(q,1,N+1) {
		string pattern;
		cin >> pattern;
		vector< set<char> > p = parsePattern(pattern);
		int ret = 0;
		FOR(i,0,D) if(fitsPattern(p, we[i])) ret++;
		cout << "Case #" << q << ": " << ret << endl;
	}
	return 0;
}