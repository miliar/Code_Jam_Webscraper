/*
 * A.cpp
 *
 *  Created on: Apr 14, 2012
 *      Author: yassery
 */


#include<iostream>
#include<cstring>
#include<algorithm>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include<sstream>
#include<cstdio>
#include<cmath>
#include<stack>
#include<complex>

using namespace std;

map<char, char> m;

void init(){
	m['a'] = 'y';
	m['b'] = 'h';
	m['c'] = 'e';
	m['d'] = 's';
	m['e'] = 'o';
	m['f'] = 'c';
	m['g'] = 'v';
	m['h'] = 'x';
	m['i'] = 'd';
	m['j'] = 'u';
	m['k'] = 'i';
	m['l'] = 'g';
	m['m'] = 'l';
	m['n'] = 'b';
	m['o'] = 'k';
	m['p'] = 'r';
	m['q'] = 'z';
	m['r'] = 't';
	m['s'] = 'n';
	m['t'] = 'w';
	m['u'] = 'j';
	m['v'] = 'p';
	m['w'] = 'f';
	m['x'] = 'm';
	m['y'] = 'a';
	m['z'] = 'q';
	m[' '] = ' ';
}



int main(){
#ifndef ONLINE_JUDGE
	freopen("test.in","rt",stdin);
	freopen("test.txt","wt",stdout);
#endif

	init();
	int n;
	string s;
	cin>>n;
	getline(cin,s);
	int t= 1;
	while(n--){
		string s2;
		getline(cin,s);
		for(int i=0;i<s.size();i++)
			s2+= m[s[i]];

		cout<<"Case #"<<t++<<": "<<s2<<endl;
	}



	return 0;
}
