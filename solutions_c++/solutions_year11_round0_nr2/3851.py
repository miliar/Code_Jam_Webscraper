#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
using namespace std;

int N;
int c, d, n, sz;
string s;
char res[1000];
char p[300][300];
char o[300];
bool use[500];

void make_move(char c)
{
	if (sz > 0)
	{
		if (p[c][res[sz-1]] != 0)
			res[sz-1] = p[c][res[sz-1]];
		else if (use[o[c]])
			sz = 0;
		else
			res[sz++] = c;
	}
	else
		res[sz++] = c;

	memset(use, 0, sizeof (use));
	for (int i = 0; i < sz; i++)
		use[res[i]] = true;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> N;

	for (int test = 1; test <= N; test++)
	{
		sz = 0;
		memset(o, 0, sizeof o);
		memset(p, 0, sizeof p);
		memset(use, 0, sizeof (use) );

		cin >> c;
		for (int i = 0; i < c; i++)
		{
			cin >> s;
			p[s[0]][s[1]] = s[2];
			p[s[1]][s[0]] = s[2];
		}

		cin >> d;
		for (int i = 0; i < d; i++)
		{
			cin >> s;
			o[s[0]] = s[1];
			o[s[1]] = s[0];
		}

		cin >> n;
		cin >> s;

		for (int i = 0; i < n; i++)
			make_move(s[i]);

		cout << "Case #" << test << ": [";
		for (int i = 0; i < sz-1; i++)
			cout << res[i] << ", ";
		if (sz > 0)
			cout << res[sz-1];
		cout << "]" << endl;
	}

	return 0;
}