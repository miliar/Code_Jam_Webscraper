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

void solve_b(int cases)
{
	int N, S, p;
	for (int i = 0; i < cases; i++) {
		VI normal;
		VI surprising;

		N = ni();
		S = ni();
		p = ni();

		for (int n = 0; n < N; n++) {
			int s = ni();
			normal.push_back((s+2)/3);
			surprising.push_back(s == 0 ? 0 : (s+4)/3);
		}

		int nii = count_if(normal.begin(), normal.end(), [=](int n){ return n >= p; });
		int pii = count_if(surprising.begin(), surprising.end(), [=](int n){ return n >= p; });

		int r = nii + min(pii-nii,S);
		printf("Case #%d: %d\n", i+1, r);
	}

}

int main(void)
{
	freopen("B-large.in", "r", stdin);
	freopen("b1.out", "w", stdout);

	int cases = ni();

	solve_b(cases);
}