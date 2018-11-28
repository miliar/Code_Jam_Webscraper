#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <sstream>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)

typedef long long int64;
typedef pair <int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const int64 inf64 = ((int64)1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;
const string task = "";

template <class T> T sqr (T x) {return x * x;}

string s[5000];
int n, m, l;

bool eq (string s, string t)
{
	int p = 0;
	forn (i, s.length())
		if (t[p] != '(')
		{
			if (t[p] != s[i])
				return 0;
			p ++;
		}
		else
		{
			p ++;
			bool ok = 0;
			while (t[p] != ')')
			{
				if (t[p] == s[i])
					ok = 1;
				p ++; 
			}
			if (!ok)
			{
				return 0;
			}
			p ++;
		}
	return 1;
}

int calc ()
{
	string t;
	cin >> t;
	int res = 0;
	forn (i, n)
		if (eq (s[i], t))
			res ++;
	return res;
}

int main ()
{
	scanf ("%d%d%d", &l, &n, &m);
	forn (i, n)
		cin >> s[i];
	forn (i, m)
		printf ("Case #%d: %d\n", i+1, calc());
	return 0;
}
