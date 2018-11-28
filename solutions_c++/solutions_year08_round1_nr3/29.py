#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <cassert>
#include <cmath>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define forv(i, v) forn(i, v.size())
#define for1(i, n) for (int i = 1; i <= int(n); i++)

#define all(x) x.begin(), x.end()
#define pb push_back
#define mp make_pair

typedef pair<int, int> pii;
typedef vector<int> VI;

#define NMAX 1000005
#define C 1000

int f[NMAX];
int s[NMAX];
int first[C][C];

int cyc, prev;

void out(int c)
{
	if (c < 100) printf("0");
	if (c < 10) printf("0");
	printf("%d\n", c);	
}

void solve2(int n)
{
	n %= cyc;
	if (n == 0) n = cyc;
	out((f[n] + 999) % 1000);
}
void solve1(int n)
{
	double A = 3.0 + sqrt(5.0);
	double ans = 1.0;

	forn(i, n)
	{
		ans *= A;
	}

//	printf("%.3lf ", ans);
	int c = ((long long)(ans)) % 1000;
	c %= 1000;
	out(c);
}
void solve(int test)
{
	int n;
	scanf("%d", &n);

	printf("Case #%d: ", test);
	if (n <= 10)
	{
		solve1(n);
//		solve2(n);
	}
	else
	{
		solve2(n);
	}
}
int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	f[1] = 5;
	f[2] = 27;
	f[3] = 144;
	s[2] = f[1] + f[2];

	for (int i = 4; i < NMAX; i++)
	{
		f[i] = (f[i - 1] * 5 + s[i - 2]) % 1000;
		s[i - 1] = (s[i - 2] + f[i - 1]) % 1000;
	}
	
	for (int i = 1; i < NMAX; i++)
	{
		if (first[f[i]][s[i]] != 0)
		{
			prev = first[f[i]][s[i]];
			cyc = i - prev;			
			break;
		}
		first[f[i]][s[i]] = i;
	}

	int tc; scanf("%d\n", &tc);
	forn(it, tc)
	{
		solve(it + 1);
	}


	return 0;
}
