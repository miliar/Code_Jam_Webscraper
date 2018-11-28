#pragma comment(linker, "/STACK:60000000")
#define _CRT_SECURE_NO_WARNINGS

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
#include <iomanip>
#include <complex>
#include <queue>
#include <functional>

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

template <class T> T sqr (T x) {return x * x;}

map < pair <char, char> , char> M;
set < pair <char, char> >  S;

string add (string s, char c) {
	if (s.length() == 0) {
		s += c;
		return s;
	}
	char c2 = s[last(s)];
	s.erase (last(s));
	if (M.count (mp (c, c2))) {
		c = M[mp (c, c2)];
		return add (s, c);
	}
	s += c2;
	s += c;
	forn (i, s.length() - 1)
		if (S.count (mp (s[i], c)))
			return "";
	return s;
}

string calc () {
	M.clear ();
	int k;
	cin >> k;
	forn (i, k) {
		string tmp;
		cin >> tmp;
		M[mp (tmp[0], tmp[1])] = tmp[2];
		M[mp (tmp[1], tmp[0])] = tmp[2];
	}
	S.clear ();
	cin >> k;
	forn (i, k) {
		string tmp;
		cin >> tmp;
		S.insert (mp (tmp[0], tmp[1]));
		S.insert (mp (tmp[1], tmp[0]));
	}
	string s;
	cin >> k;
	cin >> s;
	string res = "";
	forn (i, k)
		res = add (res, s[i]);
	string ans = "[";
	forn (i, res.length() - 1) {
		ans += res[i];
		ans += ", ";
	}
	if (res.length())
		ans += res[last(res)];
	ans += "]";
	return ans;

}

int main ()
{
	int tt;
	cin >> tt;
	forn (ii, tt) {
		printf ("Case #%d: %s\n", ii+1, calc ().data());
	}
	
	return 0;
}
