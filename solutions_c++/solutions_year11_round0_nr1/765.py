//#pragma comment(linker,"/STACK:256000000")

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <ctime>
#include <cassert>
#include <stdio.h>
#include <string>
#include <memory.h>

using namespace std;

#define ldb long double
#define LL long long
#define nextline() {int c; while ((c = getchar()) != 10 && c != EOF);}

#define PI 3.1415926535897932384626433832795
#define EPS 1e-9

#define sqr(x) ((x) * (x))
#define ABS(a) ((a)<0?-(a):(a))
#define EQ(a,b) (ABS((a)-(b))<EPS)

#define all(a) a.begin(), a.end()
#define two(i) (1 << (i))
#define has(mask, i) ((((mask) & two(i)) == 0) ? false : true)

const int INF = 1000 * 1000 * 1000;
const LL INF64 = 1000LL * 1000LL * 1000LL * 1000LL * 1000LL * 1000LL;


#define MAXN 1000

int n;
int a[200];
int b[200];
int dp[105][105][105];
int mem[105][105][105];

void Load()
{
	scanf ("%d", &n);
	string s;
	for (int i = 0; i < n; i++)
	{
		cin >> s >> a[i];
		if (s[0] == 'O')	
			b[i] = 1;
		else
			b[i] = 0;
	}
}

int rec (int pos, int bl, int org)
{
	//cerr << pos << " " << bl << " " << org << "\n";
	if (pos == n)
		return 0;

	if (dp[pos][bl][org] != -1)
		return dp[pos][bl][org];

	int mn = INF;
	if (b[pos] == 0)
	{
		if (bl == a[pos])
		{
			mn = min (mn, 1 + rec (pos + 1, bl, org));
			if (org > 1)
				mn = min (mn, 1 + rec (pos + 1, bl, org - 1));
			if (org < 100)
				mn = min (mn, 1 + rec (pos + 1, bl, org + 1));
		}
		if (bl < a[pos])
		{
			mn = min (mn, 1 + rec (pos, bl + 1, org));
			if (org > 1)
				mn = min (mn, 1 + rec (pos, bl + 1, org - 1));
			if (org < 100)
				mn = min (mn, 1 + rec (pos, bl + 1, org + 1));	
		}
		if (bl > a[pos])
		{
			mn = min (mn, 1 + rec (pos, bl - 1, org));
			if (org > 1)
				mn = min (mn, 1 + rec (pos, bl - 1, org - 1));
			if (org < 100)
				mn = min (mn, 1 + rec (pos, bl - 1, org + 1));	
		}
	}
	if (b[pos] == 1)
	{
		if (org == a[pos])
		{
			mn = min (mn, 1 + rec (pos + 1, bl, org));
			if (bl > 1)
				mn = min (mn, 1 + rec (pos + 1, bl - 1, org));
			if (bl < 100)
				mn = min (mn, 1 + rec (pos + 1, bl + 1, org));
		}
		if (org < a[pos])
		{
			mn = min (mn, 1 + rec (pos, bl, org + 1));
			if (bl > 1)
				mn = min (mn, 1 + rec (pos, bl - 1, org + 1));
			if (bl < 100)
				mn = min (mn, 1 + rec (pos, bl + 1, org + 1));	
		}
		if (org > a[pos])
		{
			mn = min (mn, 1 + rec (pos, bl, org - 1));
			if (bl > 1)
				mn = min (mn, 1 + rec (pos, bl - 1, org - 1));
			if (bl < 100)
				mn = min (mn, 1 + rec (pos, bl + 1, org - 1));	
		}
	}
	dp[pos][bl][org] = mn;
	return mn;
}


void Solve()
{
	memmove (dp, mem, sizeof (mem));

	cout << rec (0, 1, 1) << "\n";
}
                
int main()
{
	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);
	int t, T;
	cin >> T;
	memset (mem, 0xFF, sizeof (mem));

	for (t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ": ";
		Load();
		Solve();
	}
	return 0;
}
