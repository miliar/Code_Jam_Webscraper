#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cassert>
#include <ctime>
#include <algorithm>
#include <queue>
#include <memory.h>
#include <stack>

using namespace std;

#define pb push_back
#define mp make_pair
#define fir first
#define fi first
#define sec second
#define y1 botva23
typedef long long int64;
typedef long double ld;

const int inf = 2000000000;
const ld eps = 1e-07;

map <char, char> lib;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	lib['a'] = 'y';
	lib['b'] = 'h';
	lib['c'] = 'e';
	lib['d'] = 's';
	lib['e'] = 'o';
	lib['f'] = 'c';
	lib['g'] = 'v';
	lib['h'] = 'x';
	lib['i'] = 'd';
	lib['j'] = 'u';
	lib['k'] = 'i';
	lib['l'] = 'g';
	lib['m'] = 'l';
	lib['n'] = 'b';
	lib['o'] = 'k';
	lib['p'] = 'r';
	lib['q'] = 'z';
	lib['r'] = 't';
	lib['s'] = 'n';
	lib['t'] = 'w';
	lib['u'] = 'j';
	lib['v'] = 'p';
	lib['w'] = 'f';
	lib['x'] = 'm';
	lib['y'] = 'a';
	lib['z'] = 'q';
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		string s;
		scanf(" ");
		getline(cin, s);
		for (int j = 0; j < s.size(); ++j) 
			if (s[j] >= 'a' && (s[j] <= 'z'))
				s[j] = lib[s[j]];
		printf("Case #%d: %s\n", i + 1, s.c_str());
	}

	return 0;
}