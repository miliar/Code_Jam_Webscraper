#define FILENAME "a"

#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <string.h>

using namespace std; 

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define CTO500 1000000000
#define EPS 0.0000000001
#define X first
#define Y second
#define pb push_back
#define sz size()
#define VI vector<int>
#define VII vector<VI >
#define CL(a,b) memset(a,b,sizeof(a))  
#define UN(v) SORT(v),v.erase(unique(ALL(v)),v.end())  

typedef pair<int, int> PII;
typedef long long i64; 

void init(string file) {
  string ifile = file + ".in";
  string ofile = file + ".out";
	freopen(ifile.c_str(), "rt", stdin);
	freopen(ofile.c_str(), "wt", stdout);
}

void solve() {
  map<char,char> m;
  m[' '] = ' ';
  m['e'] = 'o'; m['q'] = 'z'; m['y'] = 'a'; m['z'] = 'q';

  m['e'] = 'o'; m['j'] = 'u'; m['p'] = 'r'; m['m'] = 'l'; m['y'] = 'a'; m['s'] = 'n'; m['l'] = 'g'; m['j'] = 'u'; m['y'] = 'a'; m['l'] = 'g'; m['c'] = 'e'; m['k'] = 'i'; m['d'] = 's'; m['k'] = 'i'; m['x'] = 'm'; m['v'] = 'p'; m['e'] = 'o'; m['d'] = 's'; m['d'] = 's'; m['k'] = 'i'; m['n'] = 'b'; m['m'] = 'l'; m['c'] = 'e'; m['r'] = 't'; m['e'] = 'o'; m['j'] = 'u'; m['s'] = 'n'; m['i'] = 'd'; m['c'] = 'e'; m['p'] = 'r'; m['d'] = 's'; m['r'] = 't'; m['y'] = 'a'; m['s'] = 'n'; m['i'] = 'd'; 
  m['r'] = 't'; m['b'] = 'h'; m['c'] = 'e'; m['p'] = 'r'; m['c'] = 'e'; m['y'] = 'a'; m['p'] = 'r'; m['c'] = 'e'; m['r'] = 't'; m['t'] = 'w'; m['c'] = 'e'; m['s'] = 'n'; m['r'] = 't'; m['a'] = 'y'; m['d'] = 's'; m['k'] = 'i'; m['h'] = 'x'; m['w'] = 'f'; m['y'] = 'a'; m['f'] = 'c'; m['r'] = 't'; m['e'] = 'o'; m['p'] = 'r'; m['k'] = 'i'; m['y'] = 'a'; m['m'] = 'l'; m['v'] = 'p'; m['e'] = 'o'; m['d'] = 's'; m['d'] = 's'; m['k'] = 'i'; m['n'] = 'b'; m['k'] = 'i'; m['m'] = 'l'; m['k'] = 'i'; m['r'] = 't'; m['k'] = 'i'; m['c'] = 'e'; m['d'] = 's'; 
  m['d'] = 's'; m['e'] = 'o'; m['k'] = 'i'; m['r'] = 't'; m['k'] = 'i'; m['d'] = 's'; m['e'] = 'o'; m['o'] = 'k'; m['y'] = 'a'; m['a'] = 'y'; m['k'] = 'i'; m['w'] = 'f'; m['a'] = 'y'; m['e'] = 'o'; m['j'] = 'u'; m['t'] = 'w'; m['y'] = 'a'; m['s'] = 'n'; m['r'] = 't'; m['r'] = 't'; m['e'] = 'o'; m['u'] = 'j'; m['j'] = 'u'; m['d'] = 's'; m['r'] = 't'; m['l'] = 'g'; m['k'] = 'i'; m['g'] = 'v'; m['c'] = 'e'; m['j'] = 'u'; m['v'] = 'p'; 

  int T; scanf("%d\n", &T);
  REP(test,T){
    printf("Case #%d: ", test+1);
    string s1,s2;
    getline(cin, s1);
    //getline(cin, s2);
    REP(i,s1.sz){
      //if (s1[i] == ' ') continue;
      //cout << "m['" << s1[i] << "'] = '" << s2[i] << "'; ";
      cout << m[s1[i]];
    }
    cout << endl;
  }
}

int main() {
	init(FILENAME);
	solve();
	return 0;
}
