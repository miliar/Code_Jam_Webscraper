#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
using namespace std;

const int N = 1000 + 1;
const int M = 10;

int c[N][N];
int m[N];
int s[N ];
int v[N];
int n;
bool found;

void tr(int j, int x)
{
	if (v[j] == x)
	{
		found = true;
		return;
	}
	v[j] = x;
	for (int i = 0; i < s[j]; ++i)
		tr(c[j][i], x);
}

void traversal(int j, int x)
{
	int i;

	for (i = 0; i < s[j]; ++i)
		tr(c[j][i], x);
}

int main()
{
	int i, j, k, t, p;

	scanf("%d", &t);
	for (i = 1; i <= t; ++i)
	{
		scanf("%d", &n);
		memset(s, 0, sizeof(int) * N);
		memset(v, 0, sizeof(int) * N);
		for (j = 1; j <= n; ++j)
		{
			scanf("%d", &m[j]);
			for (k = 0; k < m[j]; ++k)
			{
				scanf("%d", &p);	
				c[p][s[p]++] = j;
			}
		}

		found = false;
		for (j = 1; j <= n; ++j)
		{
			if (s[j] >= 2)
				traversal(j, j);

			if (found)
				break;
		}

		if (found)
			printf("Case #%d: Yes\n", i);
		else
			printf("Case #%d: No\n", i);
	}




	return 0;
}

