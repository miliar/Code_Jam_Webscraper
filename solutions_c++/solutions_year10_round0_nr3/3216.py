#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
using namespace std;

#define sz(v) int((v).size())
#define len(s) int(strlen(s))
#define inf 0x3f3f3f3f;
#define fori(i,c,f) for(int i = c; i < f; i++)
#define for0(i,f) fori(i,0,f)

#define maxn 1000

//long long?
long long m[maxn][maxn];
int n, t[maxn];

long long mem(int c, int f)
{
	if (c == f)
		return t[c];

	if (m[c][f] == -1)
	{
		if (c > f)
			m[c][f] = mem(c, n - 1) + mem(0, f);
		else
			m[c][f] = mem(c, f - 1) + t[f];
	}

	return m[c][f];
}

int main(void)
{
	int tc;
	scanf("%d", &tc);

	for (int tcc = 1; tcc <= tc; tcc++)
	{
		memset(m, -1, sizeof(m));

		int r, k;
		scanf("%d%d%d", &r, &k, &n);
		for (int i = 0; i < n; i++)
			scanf("%d", &t[i]);

		//s é long long?
		int c = 0;
		long long s = 0;
		while (r--)
		{
			long long g = 0;
			int f = c;
			while (1)
			{
				long long x = mem(c, f);
				if (x > k)
					break;
				else
					g = x;

				f = (f + 1) % n;
				if (f == c)
					break;
			}
			c = f;
			s += g;
		}
	
		printf("Case #%d: %I64d\n", tcc, s);
	}

	return 0;
}
