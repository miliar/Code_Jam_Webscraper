#pragma comment(linker,"/STACK:64000000")
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <memory.h>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <cassert>
#include <time.h>
#include <bitset>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a,b) memset( (a), b, sizeof( a ) )
#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()
#ifdef _DEBUG
#define dbg(...) {fprintf(stderr, __VA_ARGS__); fflush(stderr);}
#define dbgx(x) {cerr << #x << " = " << x << endl;}
#define dbgv(v) {cerr << #v << " = {"; for (typeof(v.begin()) it = v.begin(); it != v.end(); it ++) cerr << *it << ", "; cerr << "}"; cerr << endl;}
#else
#define dbg(...) { }
#define dbgx(x) { }
#define dbgv(v) { }
#endif

typedef unsigned long long ull;
typedef long long lint;
typedef pair < int , int > pii;
typedef long double ld;

const int INF = 1000 * 1000 * 1000;
const lint LINF = 1000000000000000000LL;
const double eps = 1e-9;

void prepare()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
}

const int nmax = 10;
string s[nmax];
int dx[] = { 1, -1, 0, 0, 1, 1, -1, -1 };
int dy[] = { 0, 0, 1, -1, 1, -1, 1, -1 };
int n;

bool in(int x, int y)
{
	return 0 <= x && x < n && 0 <= y && y < n;
}

bool hasDot()
{
	for (int i = 0; i < n; i ++)
	{
		for (int j = 0; j < n; j ++)
		{
			if (s[i][j] == '.') return true;
		}
	}
	return false;
}

bool match(char c, char pat)
{
	return c == pat || c == 'T';
}

bool win(char c)
{
	for (int i = 0; i < n; i ++)
	{
		for (int j = 0; j < n; j ++)
		{
			for (int k = 0; k < 8; k ++)
			{
				bool ok = true;
				for (int len = 0; len < 4; len ++)
				{
					int x = i + dx[k] * len, y = j + dy[k] * len;
					if (!in(x,y) || !match(s[x][y], c))
						ok = false;
				}
				if (ok) return true;
			}
		}
	}
	return false;
}

bool solve()
{
	n = 4;
	for (int i = 0; i < 4; i ++)
		cin >> s[i];
	if (win('X')) printf("X won");
	else if (win('O')) printf("O won");
	else if (!hasDot()) printf("Draw");
	else printf("Game has not completed");
	printf("\n");
	return false;
}

int main()
{
	prepare();
	int t;
	scanf("%d",&t);
	for (int i = 0; i < t; i ++)
	{
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}
