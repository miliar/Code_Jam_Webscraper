#include <algorithm>
#include <cmath>
#include <cstring>
#include <cctype>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(c) (c).begin(),(c).end()
#define TRACE(x) cerr << "TRACE(" #x ")" << endl;
#define DEBUG(x) cerr << #x << " = " << x << endl;

typedef long long ll;
typedef long double ld;
typedef unsigned long ulong;
typedef unsigned long long ull;

char o[256];

int main() {
	//freopen("problem.in", "r", stdin);
	//freopen("problem.out", "w", stdout);
	o['a'] = 'y';
	o['b'] = 'h';
	o['c'] = 'e';
	o['d'] = 's';
	o['e'] = 'o';
	o['f'] = 'c';
	o['g'] = 'v';
	o['h'] = 'x';
	o['i'] = 'd';
	o['j'] = 'u';
	o['k'] = 'i';
	o['l'] = 'g';
	o['m'] = 'l';
	o['n'] = 'b';
	o['o'] = 'k';
	o['p'] = 'r';
	o['q'] = 'z';
	o['r'] = 't';
	o['s'] = 'n';
	o['t'] = 'w';
	o['u'] = 'j';
	o['v'] = 'p';
	o['w'] = 'f';
	o['x'] = 'm';
	o['y'] = 'a';
	o['z'] = 'q';
	REP(c,256)
		if ('a' <= c && c <= 'z')
			continue;
		else if ('A' <= c && c <= 'A')
			o[c] = o[c-'A'+'a']-'a'+'A';
		else
			o[c] = c;
	int tnum;
	scanf("%d", &tnum);
	while (getchar() != '\n');
	REP(ti,tnum) {
		string s;
		getline(cin, s);
		cout << "Case #" << 1+ti << ": ";
		REP(i,s.size())
			cout << o[s[i]];
		cout << endl;
	}
	return 0;
}