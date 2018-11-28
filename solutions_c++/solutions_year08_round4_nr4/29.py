#include <cstdio>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <cstring>

using namespace std;

#define pb push_back
#define sz(a) (int)((a).size())
#define ll long long
#define sqr(a) ((a) * (a))

#define Nmax 50015
#define Kmax 32

int n, k;
char sir[Nmax];
char comp[Nmax];
int p[Kmax];

void citire()
{
	scanf("%d\n", &k);
	scanf("%s\n", sir + 1);
	n = strlen(sir + 1);
}

void solve()
{
	int i, j, sol = n, cnt;

	for (i = 1; i <= k; ++i)
		p[i] = i;

	do
	{
		for (i = 0; i < n; i += k)
			for (j = 1; j <= k; ++j)
				comp[i + j] = sir[i + p[j]];

		cnt = 1;
		for (i = 2; i <= n; ++i)
			if (comp[i] != comp[i - 1]) ++cnt;
		sol = min(sol, cnt);
	}
	while (next_permutation(p+1, p+k+1));

	printf("%d\n", sol);
}

int main()
{
	freopen("date.in", "r", stdin);
	freopen("date.out", "w", stdout);

	int t;

	scanf("%d\n", &t);
	for (int i = 1; i <= t; ++i)
	{
		citire();
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}
