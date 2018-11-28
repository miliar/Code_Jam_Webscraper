#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <map>
#include <set>
#define LL long long
#define ldb long double
#define sqr(a) ((a) * (a))
#define nextLine() {int c = 0; while((c = getchar()) != 10 && c != EOF);}
#define addEdge(a, b) next[edges] = first[a]; first[a] = edges; end[edges] = a;
#define debug(a) cerr << #a << " = " << a << " ";
#define debugl(a) cerr << #a << " = " << a << "\n";
const ldb eps = 1e-9;
const ldb pi = fabsl(atan2(0.0, -1.0));
const LL LINF = 1ll << 60;
const ldb LDINF = 1e42;
const int INF = 0x7f7f7f7f;
using namespace std;
#define problem "c"

LL n;

void Load()
{
	cin >> n;
}

void Solve(int Test)
{
	cout << "Case #" << Test << ": ";
	cerr << Test << "\n";
	if (n == 1) 
	{
		cout << "0\n";
		return;
	}
	LL x;
	LL res = 1;
	for (int i = 2; i <= n && i <= 1000000; i++)
	{
		x = i;
		if (x * x > n) break;
		int j;
		for (j = 2; j * j <= x; j++)
			if (x % j == 0)
				break;
		if (j * j <= x)
			continue;
		for (x = (LL)i * (LL)i; x <= n; x *= (LL)i)
			res++;
	}
	cout << res << "\n";
}

int main()
{
	freopen(problem ".in", "rt", stdin);
	freopen(problem ".out", "wt", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		Load();
		Solve(i + 1);
	}
	return 0;
}

