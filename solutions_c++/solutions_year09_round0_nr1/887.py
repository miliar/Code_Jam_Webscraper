#include<iostream>
#include<vector>
#include<string>
#include<list>
#include<map>
#include<queue>
#include<deque>
#include<algorithm>
#include<iterator>
#include<stack>
#include<sstream>
#include<numeric>
#include<cctype>
#include<cmath>
#include<cstdio>

using namespace std;

#define FOR(i,a,b) for(int i=a ; i<b ; i++)
#define pb(a) push_back(a)
#define pf(a) push_front(a)
#define VI vector<int>
#define max(a,b) (a>b)?a:b
#define min(a,b) (a<b)?a:b

vector<string> breakToChars(string &s) {
	int sz = s.size();
	vector<string> ret;
	string temp="";
	bool begin = false;
	FOR(i,0,sz) {
		if(s[i] == '(') begin=true;
		else if(s[i] == ')') {
			ret.pb(temp);
			temp = "";
			begin = false;
		}
		else if(isalpha(s[i])) {
			if(begin)
				temp+=s[i];
			else {
				string push = "";
				push += s[i];
				ret.pb(push);
			}
		}
	}
	return ret;
}
int check(vector<string> &v,vector<string> &m) {
	int ret=0;
	FOR(i,0,v.size()) {
		//for word v[i] check m
		int sz=v[i].size();
		int ctr=0;
		FOR(j,0,sz) {
			//check if v[i][j] exists in m[j]
			bool found = false; 
			FOR(k,0,m[j].size()) {
				if(m[j][k] == v[i][j]) { found = true; ctr++ ;break; }
			}
			if(!found) break;

		}
		if(ctr == sz) { // all characters match were found
			ret++;
		}
	}
	return ret;
}
int main() {
	int L,D,N;
	cin >> L >> D >> N;
	vector<string> v(D);
	FOR(i,0,D) cin >> v[i];
	string s;
	FOR(j,0,N) {
		//take a word, check with all dictionary words and return
		cin >> s;
		vector<string> m = breakToChars(s);
		//check for every word in v
		int ret = check(v,m);
		cout << "Case #" << j+1 << ": " << ret << endl; 	
		
	}
		
	return 0;
}
