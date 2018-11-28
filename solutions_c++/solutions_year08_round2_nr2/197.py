//* Problem  : Number Sets
//* Contest  : Google Code Jam 2008. Online Round 1B
//* Date     : 2008.07.26
//* Author   : alt
//* Language : C++
//* Compiler : Microsoft Visual C++ 8.0

#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <string>

using namespace std;

#define int64 long long
#define MP make_pair
#define PB push_back
#define SZ(a) (int)a.size()
#define FOR(i, n) for (int i = 0; i < (int)n; i++)
#define FORSZ(i, a) FOR(i, SZ(a))
#define INF 1000*1000*1000
#define INFLL ((long long)INF*INF)
#define ALL(a) a.begin(), a.end()
#define RALL(a) a.rbegin(), a.rend()

#define int64 long long

#define PI (2.0 * acos(0.0))

int it, nt;

int is_prime(int n)
{
	for (int i = 2; i * i <= n; i++)
		if (n % i == 0)
			return 0;
	return 1;
}

int pr[1024], A, B, P, res;

int st[1024];

int r[1024];

int ok(int a, int b)
{
	for (int i = P; i <= B; i++)
		if (pr[i] && (a%i == 0) && (b % i == 0)) return 1;
	return 0;
}

void solve()
{
	memset(r, 0, sizeof(r));
	for (int i = A; i <= B; i++)
		st[i] = i;
	while (1)
	{
		int f = 0;
		for (int i = A; i <= B; i++)
			for (int j = i + 1; j <= B; j++)
				if (st[i] != st[j] && ok(i, j))
				{
					int tt = st[i];
					f = 1;
					for (int t = A; t <= B; t++)
						if (st[t] == tt)
							st[t] = st[j];
				}
		if (!f) break;

	}
	res = 0;
	for (int i = A; i <= B; i++)
		r[st[i]]++;
	for (int i = A; i <= B; i++)
		res += !!r[i];
}

void result()
{
	printf("Case #%d: %d\n", it, res);
}


int main()
{
//#ifdef _DEBUG
	freopen("1064", "r", stdin);
	freopen("A-small.out", "w", stdout);	
//#endif
	for (int i = 2; i <= 1000; i++)
		pr[i] = is_prime(i);
	scanf("%d", &nt);
	for (it = 1; it <= nt; it++)
	{
		scanf("%d%d%d", &A, &B, &P);
		solve();
		result();
	}
	return 0;
}

