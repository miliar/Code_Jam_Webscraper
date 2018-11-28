#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
#include <utility>
#include <set>
#include <map>
#include <vector>

#define ll long long int
#define clr(a) memset(a, 0, sizeof(a))
#define FOR(a, b) for(int a = 0; a < (b); a++)
#define iter(a) typeof(a.begin())
#define foreach(a, it) for(typeof(a.begin()) it = a.begin(); it != a.end(); it++)

using namespace std;

const long double EPS = 1e-8;
const int INF = 1000000001;

char m[200][200];
set <char> o[200];
char st[200];
int cs = 0;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	//freopen("", "w", stderr);
	int t;
	scanf("%d", &t);
	for(int i0 = 1; i0 <= t; ++i0)
	{
		clr(m);
		for (char i = 'A'; i <= 'Z'; i++)
			o[i].clear();
		int c;
		scanf("%d", &c);
		FOR(i, c)
		{
			char s[4];
			scanf(" %s", &s);
			m[s[0]][s[1]] = s[2];
			m[s[1]][s[0]] = s[2];
		}
		int d;
		scanf("%d", &d);
		FOR(i, d)
		{
			char s[3];
			scanf(" %s", &s);
			o[s[0]].insert(s[1]);
			o[s[1]].insert(s[0]);
		}
		cs = 0;
		int n;
		scanf("%d ", &n);
		FOR(i, n)
		{
			char c;
			scanf("%c", &c);
			if (cs != 0)
			{
				if (m[c][st[cs - 1]] != 0) {st[cs - 1] = m[c][st[cs - 1]];continue;}
	
				bool ind = false;
				FOR(j, cs)
					if (o[c].find(st[j]) != o[c].end()) {cs = 0; ind = true; break;}
				if (ind) continue;
			}
			st[cs++] = c;
		}
		printf("Case #%d: [", i0);
		FOR(i, cs - 1)
			printf("%c, ", st[i]);
		if (cs != 0)printf("%c]\n", st[cs - 1]);
			else printf("]\n");



	}
	return 0;
}




