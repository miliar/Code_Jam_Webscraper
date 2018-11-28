#include <cstdio>
#include <vector>
#include <set>
#include <algorithm>
#include <iostream>

using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define pb push_back

const int N = 60;

char a[N][N];
char b[N][N];
int z[4][N][N];

bool count(int n, int k, char c)
{
	memset(z, 0, sizeof z);
	forn(i, n)
	{
		forn(j, n)
		{
			if(b[i][j] == c)
			{
				if(k == 1)
					return true;
				forn(t, 4)
					z[t][i][j] = 1;
				if(i > 0)
				{
					z[0][i][j] += z[0][i - 1][j];
					if(j + 1 < n)
						z[1][i][j] += z[1][i - 1][j + 1];
				}
				if(j > 0)
				{
					if(i > 0)
						z[2][i][j] += z[2][i - 1][j - 1];
					z[3][i][j] += z[3][i][j - 1];
				}
				forn(t, 4)
					if(z[t][i][j] >= k)
						return true;
			}
		}
	}
	return false;
}

void rotate(int n)
{
	memset(b, '.', sizeof b);
	for(int i = n - 1; i >= 0; --i)
	{
		int top = n - 1;
		for(int j = n - 1; j >= 0; --j)
		{
			if(a[i][j] != '.')
			{
				b[top--][n - i - 1] = a[i][j];
			}
		}
	}
	/*forn(i, n)
	{
		forn(j, n)
			printf("%c", b[i][j]);
		printf("\n");
	}*/
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("oup.txt", "w", stdout);

	int test;
	scanf("%d\n", &test);

	for1(itm, test)
	{
		int n, k;
		scanf("%d %d\n", &n, &k);
		forn(i, n)
		{
			forn(j, n)
				scanf("%c", &a[i][j]);
			scanf("\n");
		}
		rotate(n);
		
		bool f1 = count(n, k, 'B');
		bool f2 = count(n, k, 'R');
		if(f1 && f2)
			printf("Case #%d: Both\n", itm);
		else if(!f1 && !f2)
			printf("Case #%d: Neither\n", itm);
		else if(f1 && !f2)
			printf("Case #%d: Blue\n", itm);
		else if(!f1 && f2)
			printf("Case #%d: Red\n", itm);
	}

	return 0;
}
