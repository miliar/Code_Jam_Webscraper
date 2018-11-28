#include <cstdio>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

#define pb push_back
#define sz(a) (int)((a).size())
#define ll long long
#define sqr(a) ((a) * (a))

#define Nmax 10015
#define INF 0x3f3f3f3f

int n, v;
int tip[Nmax], change[Nmax];
int D[Nmax][2];

void citire()
{
	int i;

	scanf("%d %d\n", &n, &v);
	for (i = 1; i <= (n - 1) / 2; ++i)
		scanf("%d %d\n", &tip[i], &change[i]);
	for (i = (n - 1) / 2 + 1; i <= n; ++i)
		scanf("%d\n", &tip[i]);
}

void DF(int nod)
{
	int fs = nod * 2, fd = nod * 2 + 1;

	if (fd <= n)
	{
		DF(fs), DF(fd);
	}
	else
	{
		if (tip[nod] == 1) D[nod][1] = 0;
		else D[nod][0] = 0;
		return;
	}

	if (tip[nod] == 1)
	{
		D[nod][1] = min(D[nod][1], D[fs][1] + D[fd][1]);
		D[nod][0] = min(D[nod][0], min(D[fs][0] + min(D[fd][0], D[fd][1]), D[fd][0] + min(D[fs][0], D[fs][1])));
		if (change[nod] == 1)
		{
 			D[nod][1] = min(D[nod][1], min(D[fs][1] + min(D[fd][0], D[fd][1]), D[fd][1] + min(D[fs][0], D[fs][1])) + 1);
			D[nod][0] = min(D[nod][0], D[fs][0] + D[fd][0] + 1);
		}
	}
	else
	{
		D[nod][1] = min(D[nod][1], min(D[fs][1] + min(D[fd][0], D[fd][1]), D[fd][1] + min(D[fs][0], D[fs][1])));
		D[nod][0] = min(D[nod][0], D[fs][0] + D[fd][0]);
		if (change[nod] == 1)
		{
 			D[nod][1] = min(D[nod][1], D[fs][1] + D[fd][1] + 1);
			D[nod][0] = min(D[nod][0], min(D[fs][0] + min(D[fd][0], D[fd][1]), D[fd][0] + min(D[fs][0], D[fs][1])) + 1);
    	}
	}
}

void solve()
{
	memset(D, 0x3f, sizeof(D));

	DF(1);
	
	if (D[1][v] == INF)
		printf("IMPOSSIBLE\n");
	else
		printf("%d\n", D[1][v]);
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
