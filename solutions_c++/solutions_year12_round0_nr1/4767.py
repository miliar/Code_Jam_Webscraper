#include <iostream>
#include <cstdio>
#include <algorithm>
#include <map>
#include <string>
using namespace std;

#pragma comment(linker, "/STACK:67108864")

const int MAXN = 190;

char trans[MAXN];

void fill()
{
	trans['y'] = 'a';
	trans['n'] = 'b';
	trans['f'] = 'c';
	trans['i'] = 'd';
	trans['c'] = 'e';
	trans['w'] = 'f';
	trans['l'] = 'g';
	trans['b'] = 'h';
	trans['k'] = 'i';
	trans['u'] = 'j';
	trans['o'] = 'k';
	trans['m'] = 'l';
	trans['x'] = 'm';
	trans['s'] = 'n';
	trans['e'] = 'o';
	trans['v'] = 'p';
	trans['z'] = 'q';
	trans['p'] = 'r';
	trans['d'] = 's';
	trans['r'] = 't';
	trans['j'] = 'u';
	trans['g'] = 'v';
	trans['t'] = 'w';
	trans['h'] = 'x';
	trans['a'] = 'y';
	trans['q'] = 'z';
	trans['\n'] = '\n';
	trans[' '] = ' ';
}

void solve()
{
	string s;
	int n;
	cin >> n;
	getline(cin, s);
	for (int i = 0; i < n; ++i)
	{
		cout << "Case #" << i + 1 << ": ";
		getline(cin, s);
		for (int j = 0; j < (int)s.size(); ++j)
			cout << trans[s[j]];
		cout << endl;
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	fill();
	solve();
	return 0;
}