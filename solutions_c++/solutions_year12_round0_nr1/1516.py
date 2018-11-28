/*
 * in the name of god
 *
 *
 *
 *
 *
 *
 *
 */

#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <complex>
#include <stack>
#include <deque>
#include <queue>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef complex<double> point;
typedef long double ldb;

map <char,char> mp;

int main(){

	mp['a'] = 'y' ;
	mp['b'] = 'h' ;
	mp['c'] = 'e' ;
	mp['d'] = 's' ;
	mp['e'] = 'o' ;
	mp['f'] = 'c' ;
	mp['g'] = 'v' ;
	mp['h'] = 'x' ;
	mp['i'] = 'd' ;
	mp['j'] = 'u' ;
	mp['k'] = 'i' ;
	mp['l'] = 'g' ;
	mp['m'] = 'l' ;
	mp['n'] = 'b' ;
	mp['o'] = 'k' ;
	mp['p'] = 'r' ;
	mp['q'] = 'z' ;
	mp['r'] = 't' ;
	mp['s'] = 'n' ;
	mp['t'] = 'w' ;
	mp['u'] = 'j' ;
	mp['v'] = 'p' ;
	mp['w'] = 'f' ;
	mp['x'] = 'm' ;
	mp['y'] = 'a' ;
	mp['z'] = 'q' ;
	mp[' '] = ' ';

	int t; cin >> t; string s; getline(cin,s);

	for (int o=1; o<=t; o++){
		getline(cin,s);
		cout << "Case #" << o << ": ";
		for (int i=0; i<(int)s.size(); i++)
			cout << mp[s[i]];
		cout << endl;
	}
	return 0;
}
