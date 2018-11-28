#pragma comment(linker, "/STACK:128777216")
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <vector>
#include <memory.h>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <cstring>
#include <string.h>
#include <math.h>
#include <queue>
#include <stack>
#include <cassert>

#define forn(i,n) for (int i = 0; i < (int)n; i++)
#define fornd(i, n) for (int i = (int)n - 1; i >= 0; i--)
#define forab(i,a,b) for (int i = (int)a; i <= (int)b; i++)
#define forba(i,b,a) for (int i = (int)b; i >= (int)a; i--)
#define zero(a) memset (a, 0, sizeof (a))
#define _(a, val) memset (a, val, sizeof (a))
#define pb push_back
#define mp make_pair
#define all(v) (v).begin(), (v).end()
typedef long long ll;
typedef unsigned long long ull;

const ll LINF= 1000000000000000000LL;
const int INF = 1000000000;
const long double eps = 1e-9;
const long double PI = 3.1415926535897932384626433832795l;

using namespace std;

void prepare (string s)
{
#ifdef _DEBUG
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
#else
	if (s.length() != 0)
	{
		freopen ((s + ".in").c_str(), "r", stdin);
		freopen ((s + ".out").c_str(), "w", stdout);
	}
#endif
}

const int NMAX = 100100;
char ch[4][4];
int dx[] = {1, -1, 0, 0, 1, 1, -1, -1},
	dy[] = {0, 0, -1, 1, 1, -1, 1, -1};
bool used[4][4];

bool in(int x, int y)
{
	return x >= 0 && x < 4 && y >= 0 && y < 4;
}

int check(int x, int y, char c, int k)
{
	used[x][y] = true;

	int cnt = 0;
	if (k == -1)
	{
		forn(i, 8)
		{
			int xx = x + dx[i],
				yy = y + dy[i];
			if (in(xx, yy) && !used[xx][yy] && (ch[xx][yy] == c || ch[xx][yy] == 'T'))
				cnt = max(cnt, check(xx, yy, c, i));
		}
	}
	else
	{
		int xx = x + dx[k],
			yy = y + dy[k];
		if (in(xx, yy) && !used[xx][yy] && (ch[xx][yy] == c || ch[xx][yy] == 'T'))
			cnt = check(xx, yy, c, k);
	}

	used[x][y] = false;
	return cnt + 1;
}

int main ()
{
	prepare ("");

	int n = 0;
	cin >> n;

	int pl, t;
	bool flag = false;
	forn(k, n)
	{
		pl = -1;
		flag = false;

		forn(i, 4) forn(j, 4) cin >> ch[i][j];
		forn(i, 4)
		{
			forn(j, 4)
			{
				if (ch[i][j] == 'T') continue;
				if (ch[i][j] == '.')
				{
					flag = true;
					continue;
				}
				if ((t = check(i, j, ch[i][j], -1)) >= 4)
				{
					if (ch[i][j] == 'X') pl = 0;
					if (ch[i][j] == 'O') pl = 1;
					break;
				}
			}
			if (pl != -1) break;
		}

		cout << "Case #" << k+1 << ": ";
		if (pl == 0)
			cout << "X won";
		else if (pl == 1)
			cout << "O won";
		else if (flag)
			cout << "Game has not completed";
		else
			cout << "Draw";
		cout << endl;
	}


	return 0;
}