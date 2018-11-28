#include <iostream>
#include <cstdio>
#include <cstring>
#include <map>
#include <vector>
#include <list>
#include <sstream>
#include <cmath>
#include <ctime>
#include <algorithm>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define FOD(i, a, b) for (int i = (a); i >= (b); i--)
#define REP(i, a) for (int i = 0; i < (a); i++)
#define sz(a) ((int)a.size())
#define cl clear()
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define ALL(a) a.begin(), a.end()
#define sqr(a) ((a) * (a))

typedef long long ll;

int t;
string b[50];
int a[50];

int my_move(int x, int y)
{
	FOD(i, x, y + 1)
		swap(a[i], a[i - 1]);
	return (x - y);
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d\n", &t);
	REP(tt, t)
	{
		int n;
		scanf("%d\n", &n);
		REP(i, n)
			getline(cin, b[i]);
		REP(i, n)
		{
			int e = 0;
			REP(j, n)
				if (b[i][j] == '1')
					e = j;
			a[i] = e;
		}
		int ans = 0;
		REP(i, n)
			if (a[i] > i)
				FOR(j, i + 1, n)
					if (a[j] <= i)
					{
						ans += my_move(j, i);
						break;
					}
		printf("Case #%d: %d\n", tt + 1, ans);
	}
	return 0;
}
