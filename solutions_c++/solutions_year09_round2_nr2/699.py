#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <list>
#include <cmath>
#include <sstream>
#include <algorithm>
#include <ctime>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define FOD(i, a, b) for (int i = (a); i >= (b); i--)
#define REP(i, a) for (int i = 0; i < (a); i++)
#define sz(a) ((int)a.size())
#define cl clear()
#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define ALL(a) a.begin(), a.end()
#define sqr(a) ((a)*(a))

typedef long long ll;

int main()
{
//	freopen("B.in", "r", stdin);
//	freopen("B.out", "w", stdout);
	int t;
	scanf("%d\n", &t);
	REP(i, t)
	{
		string s;
		getline(cin, s);
		if (!next_permutation(s.begin(), s.end()))
		{
			sort(ALL(s));
			int t = 0;
			while (t < sz(s) && s[t] == '0')
				t++;
			printf("Case #%d: %c", i + 1, s[t]);
			REP(e, t + 1)
				printf("0");
			FOR(i, t + 1, sz(s))
				printf("%c", s[i]);
			printf("\n");
		}
		else
			printf("Case #%d: %s\n", i + 1, s.c_str());
	}
	return 0;
}
