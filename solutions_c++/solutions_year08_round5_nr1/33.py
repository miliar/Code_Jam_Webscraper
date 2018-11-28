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

bool bitmap[7000][7000];
bool inside[7000][7000];
char mask[7000][7000];

void solve(int test_num)
{
	cerr << test_num << "\n";
	int L;
	cin >> L;
	int cx = 0, cy = 0, dx = 0, dy = 1;
	memset(bitmap, 0, sizeof(bitmap));
	forn(i, L)
	{
		string s;
		int t;
		cin >> s >> t;
		forn(j, t) fors(k, s) if (s[k] == 'L')
		{
			int dx1 = -dy;
			int dy1 = dx;
			dx = dx1;
			dy = dy1;
		}
		else if (s[k] == 'R')
		{
			int dx1 = dy;
			int dy1 = -dx;
			dx = dx1;
			dy = dy1;
		}
		else
		{
			if (!dy)
			{
				int u = cx, v = cx + dx;
				if (u > v) swap(u, v);
				bitmap[u + 3500][cy + 3500] = true;
			}
			cx += dx;
			cy += dy;
		}
	}
	memset(inside, 0, sizeof(inside));
	for (int i = -3020; i <= 3020; i++)
	{
		int sum = 0;
		for (int j = -3020; j <= 3020; j++)
		{
			sum += bitmap[i + 3500][j + 3500];
			sum %= 2;
			if (sum) inside[i + 3500][j + 3500] = true;
		}
	}
	memset(mask, 0, sizeof(mask));
	for (int i = -3020; i <= 3020; i++)
	{
		bool was = false;
		for (int j = -3020; j <= 3020; j++)
		{
			was |= inside[i + 3500][j + 3500];
			if (was) mask[i + 3500][j + 3500] ^= 1;
		}
		was = false;
		for (int j = 3020; j >= -3020; j--)
		{
			was |= inside[i + 3500][j + 3500];
			if (was) mask[i + 3500][j + 3500] ^= 2;
		}
		was = false;
		for (int j = -3020; j <= 3020; j++)
		{
			was |= inside[j + 3500][i + 3500];
			if (was) mask[j + 3500][i + 3500] ^= 4;
		}
		was = false;
		for (int j = 3020; j >= -3020; j--)
		{
			was |= inside[j + 3500][i + 3500];
			if (was) mask[j + 3500][i + 3500] ^= 8;
		}
	}
	int ans = 0;
	for (int i = -3020; i <= 3020; i++)
	{
		for (int j = -3020; j <= 3020; j++)
		{
			if (inside[i + 3500][j + 3500]) continue;			
			if ((mask[i + 3500][j + 3500] & 3) == 3) ans++;
			else if ((mask[i + 3500][j + 3500] & 12) == 12) ans++;
		}
	}
	printf("Case #%d: ", test_num);
	printf("%d\n", ans);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int nt;
	cin >> nt;
	for (int it = 1; it <= nt; it++)
		solve(it);
	return 0;
}
