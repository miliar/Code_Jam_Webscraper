#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

bool opp[128][128];
char com[128][128];

char idx[9]={"ASDFQWER"};

bool oppose(string & res, char c) {
	for(int j=0;j<8;j++) {
		if(opp[c][idx[j]]) {
			for(int k=0;k<res.length();++k) {
				if(res[k]==idx[j]) {
					res.clear();
					return true;
				}
			}
		}
	}
	return false;
}

string calc(string s) {
	string res = "";
	for( int i=0;i<s.length();++i ) {
		if (res.length()==0) res += s[i]; // empty string
		else {
			// combine
			if( com[res[res.length()-1]][s[i]]!=0 ) {
				res[res.length()-1] = com[res[res.length()-1]][s[i]];
			} else if( oppose(res, s[i]) ) {
			} else {
                res += s[i];
			}
		}
	}
	if( res.length() == 0 ) return string("[]");
	string out = string("[")+res[0];
	for(int i=1;i<res.length();++i) {
		out += string(", ")+res[i];
	}
	return out+"]";
}

int main()
{
	int nCase = 1, T;
	int C, D, N;
	char c[128];
	cin >> T;
	while(T-->0) {
		memset(opp, false, sizeof opp);
		memset(com, 0, sizeof com);
		cin >> C;
		for(int i=0;i<C;++i) {
			cin >> c;
			com[c[0]][c[1]] = com[c[1]][c[0]] = c[2];
		}
		cin >> D;
		for(int i=0;i<D;++i) {
			cin >> c;
			opp[c[0]][c[1]] = opp[c[1]][c[0]] = true;
		}
		cin >> N >> c;
		
		printf( "Case #%d: %s\n", nCase++, calc(c).c_str());
	}
	return 0;
}
