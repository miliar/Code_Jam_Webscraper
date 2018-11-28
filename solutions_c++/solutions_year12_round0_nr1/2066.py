#pragma comment(linker, "/stack:64000000")
#include <algorithm>
#include <iostream>
#include <cassert>
#include <climits>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <memory.h>
#include <vector>
#include <bitset>
#include <string>
#include <deque>
#include <queue>
#include <ctime>
#include <set>
#include <map>
#include <deque>
#include <stack>
#include <cmath>
using namespace std;

typedef long long ll;
typedef long double ld;
#define forn(i, n) for (int i = 0; i < int(n); i++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define for1(i, n) for (int i = 1; i <= int(n); i++)
#define fore(i, l, r) for (int i = int(l); i < int(r); i++)
#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define pb push_back
#define pii pair <int, int>
#define vi vector <int>
#define mp make_pair

template <typename X> inline X abs (const X &a) {return a < 0? -a: a;}
template <typename X> inline X sqr (const X &a) {return a * a;}

const int INF = INT_MAX / 2;
const ll INF64 = LLONG_MAX / 2LL;
const ld EPS = 1E-9, PI = 3.1415926535897932384626433832795;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	map <char, char> p;
	p['a'] = 'y';
	p['b'] = 'h';
	p['c'] = 'e';
	p['d'] = 's';
	p['e'] = 'o';
	p['f'] = 'c';
	p['g'] = 'v';
	p['h'] = 'x';
	p['i'] = 'd';
	p['j'] = 'u';
	p['k'] = 'i';
	p['l'] = 'g';
	p['m'] = 'l';
	p['n'] = 'b';
	p['o'] = 'k';
	p['p'] = 'r';
	p['r'] = 't';
	p['s'] = 'n';
	p['t'] = 'w';
	p['u'] = 'j';
	p['v'] = 'p';
	p['w'] = 'f';
	p['x'] = 'm';
	p['y'] = 'a';
	p['z'] = 'q';
	p['q'] = 'z';

	int tests;
	scanf ("%d\n", &tests);

	forn (test, tests)
	{
		string s;
		getline (cin, s);

		printf ("Case #%d: ", test + 1);
		
		forn (i, sz (s))
		{
			if (isalpha (s[i]))
				putchar (p[s[i]]);
			else
				putchar (s[i]);
		}

		puts ("");
	}

	return 0;
}