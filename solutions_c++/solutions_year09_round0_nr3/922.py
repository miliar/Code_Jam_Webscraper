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
#include<sstream>
#include<iomanip>

using namespace std;

#define FOR(i,a,b) for(int i=a ; i<b ; i++)
#define pb(a) push_back(a)
#define pf(a) push_front(a)
#define VI vector<int>
#define max(a,b) (a>b)?a:b
#define min(a,b) (a<b)?a:b

/*
string intToString(long long int n) {
	stringstream ss;
	ss << n;
	return ss.str();
}
*/
int countAll(string &r,string &s,int indr,int inds,vector<vector<int> > &v) {
	if(indr==r.size()) {
		return 1;
	}
	if(inds==s.size()) {
		return 0;
	}
	if(v[inds][indr] != -1) {
		return v[inds][indr];
	}
	else {
		int ret=0;
		if(s[inds] == r[indr]) {
			//include it and call countAll
			ret += countAll(r,s,indr+1,inds+1,v);
		}
		//count if not included
		ret += countAll(r,s,indr,inds+1,v);
		ret %= 10000;
		v[inds][indr]=ret;
		return ret;
	}
}

int main() {
	int N,caseN=1;
	for(cin >> N ; caseN<=N ; caseN++) {
		char ch=' ';
		while (isspace(ch)) {
			ch = cin.get();
		}
		cin.putback(ch);

		string s;
		getline(cin,s);
		//input taken correctly..pheeww..
		string r = "welcome to code jam";
		vector<vector<int> > v(s.size(),vector<int> (r.size(),-1));
		long long int ret = countAll(r,s,0,0,v);
		
		cout << "Case #"<<caseN<<": "<< setfill('0') << setw(4)<< ret   << endl;
	}
	return 0;
}
