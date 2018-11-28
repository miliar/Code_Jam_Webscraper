#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:64000000")

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
//#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef long long ll;
typedef vector<ll> vll;
typedef vector<string> vs;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<bool> vb;

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define sz(x) ((int)((x).size()))

#define forn(i, x) for (int i = 0; i < int(x); i++)
#define fors(i, x) forn(i, sz(x))

template<typename T> T sqr(T x) { return x * x;            }
template<typename T> T abs(T x) { return (x > 0) ? x : -x; }

int m, v;
int gate[15000], change[15000], value[15000];
int opt[15000][2];
int op[2][2][2];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int nt;
	cin >> nt;
	forn(i, 2) forn(j, 2)
	{
		op[0][i][j] = i | j;
		op[1][i][j] = i & j;
	}
	forn(it, nt)
	{
		cin >> m >> v;
		forn(i, (m - 1) / 2)
			cin >> gate[i] >> change[i];
		for (int i = (m - 1) / 2; i < m; i++)
			cin >> value[i];
		for (int i = m - 1; i >= 0; i--)
		{
			if (i >= (m - 1) / 2)
			{
				opt[i][value[i]] = 0;
				opt[i][1 - value[i]] = 123456789;
			}
			else
			{
				opt[i][0] = 123456789;
				opt[i][1] = 123456789;
				int a = 2 * i + 1;
				int b = 2 * i + 2;
				for (int j = 0; j < 2; j++)
					for (int k = 0; k < 2; k++)
					{
						opt[i][op[gate[i]][j][k]] <?= opt[a][j] + opt[b][k];
						if (change[i]) opt[i][op[1 - gate[i]][j][k]] <?= opt[a][j] + opt[b][k] + 1;
					}
			}
		}
		if (opt[0][v] > 1000000) printf("Case #%d: IMPOSSIBLE\n", it + 1);
		else printf("Case #%d: %d\n", it + 1, opt[0][v]);
	}
	return 0;
}
