#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <fstream>
#include <sstream>
#include <algorithm>
using namespace std;
#define FOR(i,n) for(i=0;i<n;i++)
#define VI vector<int>
#define FORR(i,a,b) for(i=a;i<b;i++)
#define pb(a) push_back(a)
ifstream fin("BB.in.txt");
ofstream fout("BB.txt");

int main() {
	int i,j,k,l,n,m,p,r,t;
	fin >> r;
	string s;
	FORR(t,1,r+1) {
		fin >> s;
		s = "0" + s;
		i = s.length();
		//m = i -1;
		while(s[--i]=='0') {};
		m = i;
		while (i--) {
			if (s[i]<s[i+1]) {
				m = i+1;
				FORR(j, i+1, s.length()) if (s[j] > s[i] && s[j]<s[m]) m=j;

				swap(s[i],s[m]);
				sort(s.begin()+i+1, s.end());
				break;
			}
			if (s[i]<s[m]) m = i;
		}
		if (s[0] == '0') s = s.substr(1);
		fout << "Case #"<<t << ": " << s << endl;
	}
	return 0;
}