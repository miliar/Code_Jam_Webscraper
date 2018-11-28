#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <set>

using namespace std;

#define MAX			(100000000 + 1000000)

int comp[MAX];

bool factorizable(int x, int n, int m)
{
//	cout << "factorizable: " << x << " " << n << " " << m << endl;
	if (!n || !m)
		return false;
	if (x <= n || x <= m)
		return true;
	if (!comp[x] || n==1 || m==1)
		return false;
	return factorizable(x / comp[x], n / comp[x], m) || factorizable(x / comp[x], n, m / comp[x]);
}

pair<int,int> factorize(int x, int n, int m)
{
	if (!n || !m)
		return pair<int,int>(0,0);
	if (x <= n)
		return pair<int,int>(x, 1);
	if (x <= m)
		return pair<int,int>(1, x);
	if (!comp[x] || n==1 || m==1)
		return pair<int,int>(0,0);
	pair<int,int> p = factorize(x / comp[x], n / comp[x], m);
	if (p.first)
	{
		p.first *= comp[x];
		return p;
	}
	p = factorize(x / comp[x], n, m / comp[x]);
	p.second *= comp[x];
	return p;
}

int main()
{
	for (int n = 2; n*n < MAX; n++)
		if (!comp[n])
		{
			for (int i = n*n; i < MAX; i += n)
				comp[i] = n;
		}

	int kases, kase = 0;
	for (cin >> kases; kases; kases--)
	{
		int n, m, A;
		cin >> n >> m >> A;
		if (A > n*m)
		{
			printf("Case #%d: IMPOSSIBLE\n", ++kase);
			continue;
		}
		for (int b = 0; b <= n; b++)
			for (int c = 0; c <= n; c++)
				if (A + b*c <= n*m && factorizable(A + b*c, n, m))
				{
					pair<int,int> p = factorize(A + b*c, n, m);
					printf("Case #%d: 0 0 %d %d %d %d\n", ++kase, p.first, b, c, p.second);
					goto next;
				}
next:	;
	}
	return 0;
}
