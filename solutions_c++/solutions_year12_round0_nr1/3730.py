#if 1
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <stack>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <functional>
#include <algorithm>
#include <cmath>
#include <bitset>
#include <cstdio>
#include <list>
#include <ctime>
using namespace std;

typedef long long LL;
typedef long double LD;
typedef unsigned long long ULL;
const LD eps = 1e-9;
const LD pi = acos(-1.0);

typedef pair<int, int> pii;
typedef pair<LD, LD> pdd;
#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define iss istringstream
#define oss ostringstream
#define dbg(x) cerr << #x << " = " << x << endl;
#define dbgv(x) { cerr << #x << ": {"; for(int i = 0; i < x.size(); ++i) { if(i) cerr << ", "; cerr << x[i]; } cerr << "}" << endl; }
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define START clock_t _clock = clock();
#define END cerr << endl << "time: " << (clock() - _clock) / LD(CLOCKS_PER_SEC) << endl;
#define forn(i, n) for (int i = 0; i < n; ++i)

char k[27][2] =
{
	' ', ' ',
	'a', 'y',
	'b', 'h',
	'c', 'e',
	'd', 's',
	'e', 'o',
	'f', 'c',
	'g', 'v',
	'h', 'x',
	'i', 'd',
	'j', 'u',
	'k', 'i',
	'l', 'g',
	'm', 'l',
	'n', 'b',
	'o', 'k',
	'p', 'r',
	'q', 'z',
	'r', 't',
	's', 'n',
	't', 'w',
	'u', 'j',
	'v', 'p',
	'w', 'f',
	'x', 'm',
	'y', 'a',
	'z', 'q'
};

int main()
{
	//START
    // freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    freopen("/home/nsv/Рабочий стол/inp.txt", "r", stdin);
	freopen("/home/nsv/Рабочий стол/out.txt", "w", stdout);

	map<char, char> m;
	for (int i = 0; i < 27; ++i)
		m[k[i][0]] = k[i][1];
	
	///for (map<char, char>::const_iterator it = m.begin(); it != m.end(); ++it)
	///	cout << char(it->first) << " " << char(it->second) << endl;

	int t; cin >> t;
	string s;
	getline(cin, s);
	for (int i = 0; i < t; ++i)
	{
		getline(cin, s);
		//dbg(s)
		cout << "Case #" << i + 1 << ": ";
		for (int j = 0; j < s.length(); ++j)
			cout << char(m[s[j]]);
		cout << endl;
	}

/*
	vector<string> v(6);
	//getline(cin, v[0]);
	forn(i, 6)
		getline(cin, v[i]);

	forn(i, 6)
		dbg(v[i])

	map<char, set<char> > m;
	forn(i, 3)
		forn(j, v[i].length())
			m[v[i][j]].insert(v[i + 3][j]);

	for (map<char, set<char> >::const_iterator it = m.begin(); it != m.end(); ++it)
	{
		cout << "'" << it->X << "', '";
		for (set<char>::iterator jt = (it->Y).begin(); jt != (it->Y).end(); ++jt)
			cout << (*jt) << "',";
		cout << endl;
	}*/
		
    //END
    return 0;
}
/***************
freopen("/home/nsv/Рабочий стол/inp.txt", "r", stdin);
freopen("/home/nsv/Рабочий стол/out.txt", "w", stdout);
***************/
#endif