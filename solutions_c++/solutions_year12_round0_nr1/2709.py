#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <conio.h>
#define ll long
#define FOR(i,a,b) for(ll i=a;i<=b;i++)
#define FO(i,a,b) for(ll i=a;i<b;i++)
#define FORD(i,a,b) for(ll i=a;i>=b;i--)
#define FOD(i,a,b) for(ll i=a;i>b;i--)
#define pb push_back
#define mp make_pair
using namespace std;
map <char,string> m;
ll number (char x) {
	if (x==' ') return 0;
	if (x>='a' && x<='o') return (x-'a')/3+2;
	if (x>='p' && x<='s') return 7;
	if (x>='t' && x<='v') return 8;
	if (x>='w' && x<='z') return 9;
}
void init() {
	m['a']="y";
	m['b']="h";
	m['c']="e";
	m['d']="s";
	m['e']="o";
	m['f']="c";
	m['g']="v";
	m['h']="x";
	m['i']="d";
	m['j']="u";
	m['k']="i";
	m['l']="g";
	m['m']="l";
	m['n']="b";
	m['o']="k";
	m['p']="r";
	m['q']="z";
	m['r']="t";
	m['s']="n";
	m['t']="w";
	m['u']="j";
	m['v']="p";
	m['w']="f";
	m['x']="m";
	m['y']="a";
	m['z']="q";
	m[' ']=" ";
}
ll nTest,test;
string s;
main() {
	freopen("A-small-attempt0.in","r",stdin);
	freopen("test.out","w",stdout);
	init();
	cin >> nTest;
	getline(cin,s);
	FOR (test,1,nTest) {
		printf("Case #%d: ",test);
		getline(cin,s);
		FO (i,0,s.size()) {
			cout << m[s[i]];
		}
		cout << endl;
	}
}
