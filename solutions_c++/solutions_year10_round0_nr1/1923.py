#include <iostream>
#include <vector>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#define file "a"
#define ldb long double
#define LL long long
const ldb eps = 1e-9;
const int INF = 1 << 30;
const LL LINF = 1ll << 60;
const ldb LDINF = 1e+70;
using namespace std;

int n, k;

void Load()
{
	cin >>n >> k;
}

void Solve(int Test)
{
	int res = 0;
	while (k > 0)
	{
		if ((k & 1) == 1)
		{
			res++;
		}
		else break;
		k >>= 1;
	}
	if (res >= n)
	{
		cout << "Case #" << Test << ": ON\n";
	}
	else 
	{
		cout << "Case #" << Test << ": OFF\n";
	}
}

int main()
{
	freopen(file".in", "rt", stdin);
	freopen(file".out", "wt", stdout);
	int T;
	cin >> T;
	int i;
	for (i = 1; i <= T; i++)
	{
		Load();
		Solve(i);
	}
	return 0;
}