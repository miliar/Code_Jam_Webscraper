#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <stack>
#include <queue>
#include <deque>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <cassert>
#include <string>
#include <cstring>

using namespace std;

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define sz(x) (int)(x).size()
#define forn(i, n) for(int i = 0;i < n;i++)

typedef long long ll;
typedef unsigned long long llu;

const int inf = 2e9;
const double eps = 1e-7;
const double pi = 3.1415926535;

int n;
string s;
map <char, char> dict;

int main() {

	dict['a'] = 'y';
	dict['b'] = 'h';
	dict['c'] = 'e';
	dict['d'] = 's';
	dict['e'] = 'o';
	dict['f'] = 'c';
	dict['g'] = 'v';
	dict['h'] = 'x';
	dict['i'] = 'd';
	dict['j'] = 'u';
	dict['k'] = 'i';
	dict['l'] = 'g';
	dict['m'] = 'l';
	dict['n'] = 'b';
	dict['o'] = 'k';
	dict['p'] = 'r';
	dict['q'] = 'z';
	dict['r'] = 't';
	dict['s'] = 'n';
	dict['t'] = 'w';
	dict['u'] = 'j';
	dict['v'] = 'p';
	dict['w'] = 'f';
	dict['x'] = 'm';
	dict['y'] = 'a';
	dict['z'] = 'q';

	cin >> n;
	getline(cin, s);
	forn(i, n) {
		getline(cin, s);
		int len = sz(s);
		forn(j, len) {
			if(s[j] >= 'a' && s[j] <= 'z') {
				s[j] = dict[s[j]];
			}
		}
		cout << "Case #" << i + 1 << ": " << s << endl;
	}
	return 0;
}
