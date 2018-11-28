#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <iostream>
#include <cassert>

using namespace std;

typedef pair<char, char> pcc;

pcc op(char a, char b){
	return make_pair(min(a, b), max(a, b));
}

void solve(int tc){
	int c;
	cin >> c;
	map<pcc, char> comb;
	for(int i = 0; i < c; i++){
		string s;
		cin >> s;
		assert(s.size() == 3);
		comb[op(s[0], s[1])] = s[2];
	}
	int d;
	cin >> d;
	map<char, set<char> > opp;
	for(int i = 0; i < d; i++){
		string s;
		cin >> s;
		assert(s.size() == 2);
		opp[s[0]].insert(s[1]);
		opp[s[1]].insert(s[0]);
	}
	int n;
	cin >> n;
	string s;
	cin >> s;
	assert(s.size() == n);
	string buf;
	for(int i = 0; i < n; i++){
		if(buf.empty()){
			buf += s[i];
		}else if(comb.count(op(s[i],*buf.rbegin()))){
			*buf.rbegin() = comb[op(s[i], *buf.rbegin())];
		}else{
			bool opposite = false;
			for(string::iterator it = buf.begin(); it != buf.end(); ++it){
				if(opp[s[i]].count(*it)){
					buf.clear();
					opposite = true;
					break;
				}
			}
			if(!opposite){
				buf += s[i];
			}
		}
	}
	printf("Case #%d: [", tc);
	for(string::iterator it = buf.begin(); it != buf.end(); ++it){
		if(it != buf.begin()){
			printf(", ");
		}
		printf("%c", *it);
	}
	printf("]\n");
}

int main(){
	int t;
	scanf("%d", &t);
	for(int i = 0; i < t; i++){
		solve(i+1);
	}
	return 0;
}
