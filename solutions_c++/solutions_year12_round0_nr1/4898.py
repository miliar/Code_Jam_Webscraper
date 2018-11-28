/**					Be name Khoda					**/
#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <map>
#include <vector>
#include <set>
#include <queue>
#include <algorithm>
#include <bitset>
#include <limits>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <memory.h>
#include <ctime>
#include <cassert>
using namespace std;

#define ll long long
#define un unsigned
#define IT iterator
#define VAL(x) #x << " = " << x << "   "
#define SQR(a) ((a) * (a))
#define SZ(x) ((int) x.size())
#define ALL(x) x.begin(), x.end()
#define CLR(x, a) memset(x, a, sizeof x)
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define SAL cout << "Salam!\n"
#define MAXN 1000
#define cout fout
#define cin fin

map<char, char> m;

int main ()
{
	ifstream fin("A-small-attempt0.in");
	ofstream fout("A.out");
	m['e'] = 'o';
	m['j'] = 'u';
	m['p'] = 'r';
	m['m'] = 'l';
	m['y'] = 'a';
	m['s'] = 'n';
	m['l'] = 'g';
	m['c'] = 'e';
	m['k'] = 'i';
	m['d'] = 's';
	m['x'] = 'm';
	m['v'] = 'p';
	m['n'] = 'b';
	m['r'] = 't';
	m['i'] = 'd';
	m['b'] = 'h';
	m['t'] = 'w';
	m['a'] = 'y';
	m['h'] = 'x';
	m['w'] = 'f';
	m['f'] = 'c';
	m['o'] = 'k';
	m['j'] = 'u';
	m['u'] = 'j';
	m['l'] = 'g';
	m['g'] = 'v';
	m['z'] = 'q';
	m['q'] = 'z';
	int tc, k = 0;
	cin >> tc;
	string s;
	getline(cin, s);
	while (tc --)
	{
		k ++;
		getline(cin, s);
		string ans;
		for (int i = 0; i < (int) s.size(); i ++)
			if (isalpha(s[i]))
				ans.pb(m[s[i]]);
		else
			ans.pb(s[i]);
		cout << "Case #" << k << ": " << ans << endl;
	}
	return 0;
}


