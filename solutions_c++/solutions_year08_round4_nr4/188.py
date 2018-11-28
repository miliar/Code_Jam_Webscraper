#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <sstream>
#include <cstdlib>
#include <cassert>
using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define forv(i, v) forn(i, v.size())
#define for1(i, n) for(int i = 1; i <= int(n); i++)

#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair

typedef  vector<int> VI;

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"
const int NMAX = 7;
int p[NMAX];

int compLength(string s) {
	int ret = 0;
	int i = 0;
	while (i < (int)s.length()) {
		int j = i + 1;
		while (j < (int)s.length() && s[j] == s[i]) j++;
		ret++;
		i = j;
	}
	return ret;
}

int apply(string s, int k) {
	string t;
	int l = 0;
	while (l < (int)s.length()) {
		forn(i, k) t += s[l + p[i]];
		l += k;
	}	
	return compLength(t);
}

int main()
{
	freopen(CIN_FILE, "rt", stdin);
	freopen(COUT_FILE, "wt", stdout);
	int tc; cin >> tc;
	forn(it, tc) {
		int k; scanf("%d\n", &k);
		string s;
		getline(cin, s);
		forn(i, k) p[i] = i;
		int ans = 10000000;
		do {
			ans = min(ans, apply(s, k));
		} while(next_permutation(p, p + k));
		printf("Case #%d: %d\n", it+1, ans);
	}

	return 0;
}
