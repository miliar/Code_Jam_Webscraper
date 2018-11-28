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

char buf[1000];
int s, q;
string engine[150], query[1500];
int opt[1500][150];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	gets(buf);
	int nt;
	sscanf(buf, "%d", &nt);
	forn(it, nt)
	{
		gets(buf);
		sscanf(buf, "%d", &s);
		forn(i, s)
		{
			gets(buf);
			engine[i] = buf;
		}
		gets(buf);
		sscanf(buf, "%d", &q);
		forn(i, q)
		{
			gets(buf);
			query[i] = buf;
		}
		memset(opt, 63, sizeof(opt));
		opt[0][0] = 0;
		forn(i, q) forn(j, s + 1)
		{
			if (opt[i][j] > 1000000000) continue;
			for (int k = 1; k <= s; k++)
			{
				if (query[i] == engine[k - 1]) continue;
				int add = 1 - int(j == k);
				if (opt[i + 1][k] > opt[i][j] + add) opt[i + 1][k] = opt[i][j] + add;
			}
		}
		int ans = 1000000000;
		for (int i = 0; i <= s; i++)
			if (opt[q][i] < ans) ans = opt[q][i];
		if (ans) ans--;
		printf("Case #%d: %d\n", it + 1, ans);
	}
	return 0;
}
