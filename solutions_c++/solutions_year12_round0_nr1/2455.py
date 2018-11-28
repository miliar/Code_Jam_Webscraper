#include <string>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>

using namespace std;

#define all(x) x.begin(),x.end()
#define bits(x) __builtin_popcount(x)
#define FOR(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)

string a[] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi","rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","de kr kd eoya kw aej tysr re ujdr lkgc jv","yeq"};
string b[] = {"our language is impossible to understand","there are twenty six factorial possibilities","so it is okay if you want to just give up","aoz"};

int main() {
	int n;
	string line;
	map<char, char> mapa;
	vector<bool> from(128, false), to(128, false);
	
	for (int i=0;i<4;i++) {
		for (int j=0;j<a[i].size();j++) {
			from[a[i][j]]=true;
			to[b[i][j]]=true;
			mapa[a[i][j]]=b[i][j];
		}
	}
	char f=0,t=0;
	for (char i='a';i<='z';i++) {
		if (!from[i]) f=i;
		if (!to[i]) t=i;
	}
	
	if (f!=0) mapa[f]=t;
	
	getline(cin, line);
	stringstream(line) >> n;
	
	for (int i = 0; i < n; i++) {
		getline(cin, line);
		
		for (int j=0;j<line.size();j++) line[j]=mapa[line[j]];
		
		cout << "Case #" << (i+1) << ": " << line << endl; 
	}
	return 0;
}
