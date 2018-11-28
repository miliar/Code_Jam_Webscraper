#include <iostream>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

int test;
string name = "d";

struct node
{
	long long n;
	int s;
	node(long long _n = 0, int _s = 0) : n(_n), s(_s) {}

	bool operator < (const const node & K) const
	{
		if (n != K.n) return n < K.n;
		return s < K.s;
	}
};

long long MOD = 1000000007;

long long inv(long long x)
{
	long long res = 1;
	int p = MOD - 2;
	while (p)
	{
		if (p & 1) res = res * x % MOD;
		p >>= 1;
		x = x * x % MOD;
	}
	return res;
}

map<node, long long> memo;

long long can[70 * 70][71];
long long C[71][71];
long long F[71];

long long f(long long N, int s, int b)
{
	if (N < 0) return 0;

	if (memo.count(node(N, s))) return memo[node(N, s)];
	long long res = 0;

	int x = N % b;

	for (int t = x; t < b*b / 2 && t <= N; t += b)
	{
		long long M = (N - t) / b;
		if (can[t][s])
		{
			if (M == 0)
				res += F[s] * can[t][s] % MOD;
			else
			{
				for (int s1 = 1; s1 <= s; s1++)
					res += F[s] * can[t][s] % MOD * f(M, s1, b) % MOD * C[s][s1] % MOD;
			}
		}
		
		if (can[t][s-1])
		{
			if (M == 0)
				res += 0 % MOD;
			else
			{
				for (int s1 = 1; s1 <= s; s1++)
					res += F[s] * can[t][s-1] % MOD * f(M, s1, b) % MOD * C[s-1][s1-1] % MOD;
			}
		}
	}

	return memo[node(N, s)] = res % MOD;
}

void solve()
{
	long long ans = 0;
	long long N;
	int b;

	cin >> N >> b;
	memo.clear();

	memset(can, 0, sizeof can);
	memset(C, 0, sizeof C);
	for (int i = 0; i <= b; i++)
	{
		C[i][0] = 1;
		for (int j = 1; j <= i; j++)
			C[i][j] = (C[i-1][j] + C[i-1][j-1]) % MOD;
		F[i] = i == 0 ? 1 : F[i-1] * i % MOD;
	}

	can[0][0] = 1;

	for (int j = 1; j < b; j++) for (int i = b * b - 1; i >= j; i--) for (int u = 0; u < b - 1; u++)
		can[i][u+1] += can[i-j][u];

	for (int i = 1; i <= b; i++)
		ans += f(N, i, b) * inv(F[i]) % MOD;

	ans %= MOD;

	cout << "Case #" << test << ": ";
	cout << ans << endl;

	cerr << "Case #" << test << ": ";
	cerr << ans << endl;
}

int main()
{
	freopen((name + ".in").c_str(), "r", stdin);
	freopen((name + ".out").c_str(), "w", stdout);

	int tests;
	cin >> tests;
	for (test = 1; test <= tests; test++)
		solve();

	return 0;
}