#include <stdio.h>
#include <math.h>
#include <string.h>
#include <memory.h>
#include <vector>
#include <string>
#include <iostream>
#include <set>
#include <ctime>
#include <map>
#include <algorithm>
using namespace std;

#define FOR(i, n)		for (int i = 0; i < (int) (n); i++)
#define RFOR(i, n)		for (int i = (int) (n) - 1; i >= 0; i--)
#define CL(x)			memset(x, 0, sizeof(x))
#define CLX(x, v)		memset(x, v, sizeof(x))
#define ALL(x)			(x).begin(), (x).end()
#define PB				push_back
#define MP				make_pair

typedef long long LL;
typedef unsigned long long UL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int, int> PII;

//////////////////////////////////////////////////////////////////////////

LL GCD(LL a, LL b)
{
	while (b)
	{
		LL t = a % b;
		a = b;
		b = t;
	}
	return a;
}

bool Solve(LL n, LL pd, LL pg)
{
	if (pg == 0)
	{
		return pd == 0;
	}
	else if (pg == 100)
	{
		return pd == 100;
	}
	else
	{
		return n >= 100 / GCD(100, pd);
	}
}

int main()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	/*{
		string s = "";
		freopen((s + ".in").c_str(), "r", stdin);
		freopen((s + ".out").c_str(), "w", stdout);
	}*/
#endif

	int tt;
	cin >> tt;
	FOR(i, tt)
	{
		LL n, pd, pg;
		cin >> n >> pd >> pg;
		printf("Case #%d: ", i + 1);
		if (Solve(n, pd, pg))
			printf("Possible\n");
		else
			printf("Broken\n");
	}

	return 0;
}
