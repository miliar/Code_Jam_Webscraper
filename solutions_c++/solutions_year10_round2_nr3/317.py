#define _CRT_SECURE_NO_DEPRECATE
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <cstdio>
#include <set>
#include <cmath>
#include <queue>
#include <sstream>
#include <iostream>
using namespace std;

//////////////////// Defines ////////////////////

#pragma comment(linker, "/STACK:67108864")

#define inf      2147483647
#define inf64    9223372036854775807
#define eps      1e-6
#define pi      3.14159265358
#define sqr(a) (a)*(a)
#define rall(a) a.rbegin(),a.rend()
#define all(a) a.begin(),a.end()
#define sz(a) (a).size()
#define mset(a,v) memset(a, v, sizeof(a))
#define pb push_back 
typedef long long ll;
typedef vector<int> VI;
typedef vector<double> VD;
typedef vector<string> VS;

#define ContinueIf(x) if ((x)) continue
#define ContinueUnless(x) if(!(x)) continue

#define BreakIf(x) if ((x)) break
#define BreakUnless(x) if(!(x)) break

#define ReturnUnless(x) if (!(x)) return
#define ReturnIf(x) if ((x)) return

#define ReturnUnless2(x, ret) if (!(x)) return ret
#define ReturnIf2(x, ret) if ((x)) return ret

//////////////////// Problem Code ////////////////////

int N;
const int mod = 100003;

ll powerMod(ll x, int y)
{
	if (!y)
	{
		return 1;
	}
	if (y % 2)
	{
		return (powerMod(x, y-1) * x) % mod;
	}
	return powerMod((x*x) % mod, y / 2);
}

ll combo[512][512];

ll getComb(int n, int k)
{
	if (n < k)
	{
		return 0;
	}
	if (n == k || !k)
	{
		return 1;
	}
	if (combo[n][k] != -1)
	{
		return combo[n][k];
	}
	return combo[n][k] = getComb(n-1, k-1) + getComb(n-1, k);
}

ll memo[512][512];
ll solve(int curr, int rank)
{
	if (curr <= rank)
	{
		return 0;
	}
	if (curr == rank + 1 || rank == 1)
	{
		return 1;
	}
	ll& ans = memo[curr][rank];
	if (ans != -1)
	{
		return ans;
	}
	ans = 0;
	for (int i = 1 ; i < rank ; ++i)
	{
		ll t = solve(rank, i) * getComb(curr - rank - 1, rank - i - 1);

		ans += t;
		ans %= mod;
	}

	return ans;
}

int solve2(int n)
{
	int prev = 1, next = 1;
	for (int i = 1 ; i < n ; ++i)
	{
		int temp = next;
		next += prev;
		next %= mod;
		prev = temp;
	}
	return prev;
}

int main()
{
	int k, T;
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	scanf("%d", &T);
	mset(combo, -1);
	for(k = 1 ; k <= T ; ++k)
	{
		scanf("%d", &N);
		mset(memo, -1);
		int ans = 0;
		for (int i = 1 ; i < N ; ++i)
		{
			ans += solve(N, i);
			ans %= mod;
		}
		printf("Case #%d: %d\n", k, ans);
	}
	return 0;
}

