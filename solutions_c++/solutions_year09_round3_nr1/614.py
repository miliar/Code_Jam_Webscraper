#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <map>
using namespace std;
#define FOR(i,n) for(i=0;i<n;i++)
#define VI vector<int>
#define FORR(i,a,b) for(i=a;i<b;i++)
#define pb(a) push_back(a)
ifstream fin("AAA.in.txt");
ofstream fout("AAA.txt");


unsigned __int64 l;

int val(char c) {
	if (c>='0' && c<='9') return c-'0'; else return c-'a'+10;
}

int main() {
	int i,j,k,n,m,p,r,t;
	fin >> r;
	string s;
	int a[300];
	bool c[300];
	FORR(t,1,r+1) {
		fin >> s;
		memset(a,0,sizeof(a));
		memset(c,0,sizeof(c));
		a[s[0]] = 1;
		c[s[0]] = 1;
		p = 0;
		FORR(i, 1, s.length()) if (!c[s[i]]) {
			a[s[i]]=p++;
			if (p==1) p = 2;
			c[s[i]] = 1;
		}
		if (p<2) p = 2;
		l = 0;
		FOR(i, s.length()) {
			l = l*(p)+a[s[i]];
		}
		fout << "Case #"<<t << ": " << l << endl;
	}
	return 0;
}