#include <cstdio>
#include <cstring>

#define Nmax 1000015
#define Amax 4194304

int n, k;
int d[Nmax];
int AI[Amax];
int sir[Nmax];

void citire()
{
	int i;

	scanf("%d\n", &n);
	scanf("%d", &k);
	for (i = 1; i <= k; ++i)
		scanf("%d", &d[i]);
}

void init(int nod, int st, int dr)
{
	if (st == dr) AI[nod] = 1;
	else
	{
		int mij = (st + dr) / 2, fs = nod * 2, fd = nod * 2 + 1;

		init(fs, st, mij);
		init(fd, mij + 1, dr);
		AI[nod] = AI[fs] + AI[fd];
	}
}

void update(int nod, int st, int dr, int a)
{
	if (st == dr)
		AI[nod] = 0;
	else
	{
		int mij = (st + dr) / 2, fs = nod * 2, fd = nod * 2 + 1;

		if (a <= mij) update(fs, st, mij, a);
		else update(fd, mij + 1, dr, a);

		AI[nod] = AI[fs] + AI[fd];
	}
}

int query(int nod, int st, int dr, int a)
{
	if (st == dr)
		return st;
	else
	{
		int mij = (st + dr) / 2, fs = nod * 2, fd = nod * 2 + 1;

		if (AI[fs] >= a) return query(fs, st, mij, a);
		else
		{
			a -= AI[fs];
            return query(fd, mij + 1, dr, a);
		}
	}
}

void solve()
{
	int i, ct = 1, nod;

	init(1, 1, n);
	for (i = 1; i <= n; ++i)
	{
		ct += i - 1;
		ct %= n - i + 1;
		if (!ct) ct = n - i + 1;

		nod = query(1, 1, n, ct);
        update(1, 1, n, nod);
		
		sir[nod] = i;
	}
	
	for (i = 1; i <= k; ++i)
		printf("%d ", sir[d[i]]);
	printf("\n");
}

int main()
{
	freopen("date.in", "r", stdin);
	freopen("date.out", "w", stdout);

	int t;

	scanf("%d\n", &t);
	for (int i = 1;i <= t; ++i)
	{
		citire();
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}
