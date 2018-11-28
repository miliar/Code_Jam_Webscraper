#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <deque>

using namespace std;

ifstream fin("input.txt");

int C,D,N;

map<pair<char,char>,char> compose;
set<pair<char,char> > opposed;
string invoke;
deque<char> invoked;

void input() {
	compose.clear();
	opposed.clear();
	invoked.clear();
	fin >> C;
	string s;
	for (int i=0;i<C;i++) {
		fin >> s;
		compose[make_pair(s[0],s[1])] = s[2];
		compose[make_pair(s[1],s[0])] = s[2];
	}
	fin >> D;
	for (int i=0;i<D;i++) {
		fin >> s;
		opposed.insert(make_pair(s[0],s[1]));
		opposed.insert(make_pair(s[1],s[0]));
	}
	fin >> N;
	fin >> invoke;
}

string solution;

void solve() {
	for (int k=0;k<N;k++) {
		invoked.push_back(invoke[k]);
		if (invoked.size() >= 2) {
			bool found = false;
			char withWhat;
			if (compose.find(make_pair(invoked[invoked.size()-1], invoked[invoked.size()-2])) != compose.end()) {
				found = true;
				withWhat = compose[make_pair(invoked[invoked.size()-1], invoked[invoked.size()-2])];	
			} 
			if (found) {
				invoked.pop_back();
				invoked.pop_back();
				invoked.push_back(withWhat);
			}
		}
		bool found = false;
		for (int i=0;i<invoked.size()-1;i++) {
			if (opposed.find(make_pair(invoked[i], invoked[invoked.size()-1])) != opposed.end()) {
				found = true;
			}
		}
		if (found) invoked.clear();
	}
	solution = "[";
	for (int i=0;i<invoked.size();i++) {
		solution = solution + ((i > 0) ? ", " : "") + invoked[i];
	}
	solution = solution + "]";

}

int main() {
	int T;
	fin >> T;
	for (int t=1;t<=T;++t) {
		input();
		solve();		
		cout << "Case #" << t << ": " << solution << "\n";
	}	
	fin.close();
}

