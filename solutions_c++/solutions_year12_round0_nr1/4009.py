#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <cmath>
using namespace std;

#define FORZ(i,n) for(typeof(n)i=0;i<n;i++)
#define all(x) (x).begin(),(x).end()
#define PB push_back
#define sz size()
#define FF first
#define SS second
typedef vector<int> VI;
typedef pair<int,int> pII;
typedef vector<string> VS;
typedef long long LL;

int main () {

	map <char, char> mp;
	
	mp['a'] = 'y';
	mp['b'] = 'h';
	mp['c'] = 'e';
	mp['d'] = 's';
	mp['e'] = 'o';
	mp['f'] = 'c';
	mp['g'] = 'v';
	mp['h'] = 'x';
	mp['i'] = 'd';
	mp['j'] = 'u';
	mp['k'] = 'i';
	mp['l'] = 'g';
	mp['m'] = 'l';
	mp['n'] = 'b';
	mp['o'] = 'k';
	mp['p'] = 'r';
	mp['q'] = 'z';
	mp['r'] = 't';
	mp['s'] = 'n';
	mp['t'] = 'w';
	mp['u'] = 'j';
	mp['v'] = 'p';
	mp['w'] = 'f';
	mp['x'] = 'm';
	mp['y'] = 'a';
	mp['z'] = 'q';
	
	string tc;
	getline (cin, tc);
	istringstream iss (tc);
	int T;
	iss >> T;
	
	for (int t = 1 ; t <= T ; t ++) {
		string str;
		getline(cin, str);		
		istringstream iss(str);
		string s;
		while (iss) {
			string st;
			iss >> st;
			s += st;
			s += ' ';
		}
		s = s.substr(0, s.sz - 1);
		FORZ (i, s.sz) s[i] = (s[i] == ' ') ? ' ' : mp [ s[i] ];
		cout << "Case #" << t << ": " << s << "\n";
	}	
	
	return 0;
}
