//============================================================================
// Name        : gcj2012qualA.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <cassert>
#include <cstdio>
using namespace std;

#define For(i,a,b) for(int i = a; i < b; i++)
#define rep(i,x) For(i,0,x)
#define foreach(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define sz(x) (int((x).size()))
#define F first
#define S second
#define mp make_pair

using namespace std;

string A = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
string B = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

int main() {

	set<int> c;
	rep(i, 26) c.insert(i+'a');

	char map[26];
	memset(map, '?', sizeof(map));
	rep(i, sz(A)){
		map[A[i] - 'a'] = B[i];
		c.erase(B[i]);
	}

	map['z' - 'a'] = 'q';
	map['q' - 'a'] = 'z';

	int np; cin>>np;
	int tp = 0;
	string s;
	getline(cin,s);
	while(getline(cin, s)){
		printf("Case #%d: ", ++tp);
		rep(i, sz(s)) cout<<map[s[i] - 'a'];
		cout<<endl;
	}
	assert(tp == np);
}
