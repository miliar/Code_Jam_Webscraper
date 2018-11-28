#define _CRT_SECURE_NO_DEPRECATE
#define _ASSERTE

#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <ctime>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define fore(i, a, b) for(int i = a; i < (int)(b); ++i)
#define pii pair<int,int>
#define pb push_back
#define mp make_pair
#define all(a) a.begin,a.end()
#define ll long long


int tt, n, s, p, c[123], a[123], b[123];

int d[123][123];
int used[123][123];

int get(int i, int su)  {
	if (used[i][su])return d[i][su];
	if (i == n){
		if (su)
			return -1000000;
		return 0;
	}

	used[i][su] = 1;

	// not surprising
	int res = get(i + 1, su);
	if (c[i] >= p * 3 - 2)
		++res;
	
	// surprising
	if (c[i] > 1 && c[i] < 29)
		res = max(res, get(i + 1, su - 1));
	for(int pp = max(0, p - 2); pp <= 8; pp++){
		if (c[i] >= pp * 3 + 2 && c[i] <= pp * 3 + 4){
			res = max(res, get(i + 1, su - 1) + 1);
			break;
		}
	}

	return d[i][su] = res;
}

int main(){
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	char z[1234];
	z['a'] = 'y';
	z['b'] = 'h';
	z['c'] = 'e';
	z['d'] = 's';
	z['e'] = 'o';
	z['f'] = 'c';
	z['g'] = 'v';
	z['h'] = 'x';
	z['i'] = 'd';
	z['j'] = 'u';
	z['k'] = 'i';
	z['l'] = 'g';
	z['m'] = 'l';
	z['n'] = 'b';
	z['o'] = 'k';
	z['p'] = 'r';
	z['q'] = 'z';
	z['r'] = 't';
	z['s'] = 'n';
	z['t'] = 'w';
	z['u'] = 'j';
	z['v'] = 'p';
	z['w'] = 'f';
	z['x'] = 'm';
	z['y'] = 'a';
	z['z'] = 'q';
	z[' '] = ' ';

	cin >> tt;
	string s;
	getline(cin, s);
	forn(t, tt) {
		getline(cin, s);

		printf("Case #%d: ", t + 1);
		forn(i, s.length())
			printf("%c", z[s[i]]);
		puts("");

		/*
		cin >> n >> s >> p;
		memset(used, 0, sizeof used);
		int res = 0;
		forn(i, n){
			cin >> c[i];
		}

		res = get(0, s);
		printf("Case #%d: %d\n", t + 1, res);
		*/
	}
	
	return 0;
}