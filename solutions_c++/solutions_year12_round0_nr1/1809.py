#include <algorithm>  
#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list> 

using namespace std;

typedef map<char,char> dict;
typedef vector<int> VI;
typedef long long LL;
#define VLL vector<long long>
#define SZ(v) ((int)(v).size())  
#define FOR(i,a,b) for(int i=(a);i<(b);++i)  
#define REP(i,n) FOR(i,0,n)  
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)  
#define REPE(i,n) FORE(i,0,n)  
#define FORSZ(i,a,v) FOR(i,a,SZ(v))  
#define REPSZ(i,v) REP(i,SZ(v))  

char buf[1024];

int ni(){
	int i;
	scanf("%d", &i);
	return i;
}

double nd(){
	double i;
	scanf("%f", &i);
	return i;
}

string ns() { 
	scanf( "%s", buf ); return buf; 
}

string nl() {
	return gets(buf);
}

void solve_a(int cases)
{
	dict d;
	d['a'] = 'y';
	d['b'] = 'h';
	d['c'] = 'e';
	d['d'] = 's';
	d['e'] = 'o';
	d['f'] = 'c';
	d['g'] = 'v';
	d['h'] = 'x';
	d['i'] = 'd';
	d['j'] = 'u';
	d['k'] = 'i';
	d['l'] = 'g';
	d['m'] = 'l';
	d['n'] = 'b';
	d['o'] = 'k';
	d['p'] = 'r';
	d['q'] = 'z';
	d['r'] = 't';
	d['s'] = 'n';
	d['t'] = 'w';
	d['u'] = 'j';
	d['v'] = 'p';
	d['w'] = 'f';
	d['x'] = 'm';
	d['y'] = 'a';
	d['z'] = 'q';
	d[' '] = ' ';

	for (int i = 0; i < cases; i++) {
		string s = nl();
		for (int j = 0; j < s.length(); j++) {
			s[j] = d[s[j]];
		}
		printf("Case #%d: %s\n", i+1, s.c_str());
	}
}

int main(void)
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("a1.out", "w", stdout);

	int cases = ni();
	gets(buf);

	solve_a(cases);
}