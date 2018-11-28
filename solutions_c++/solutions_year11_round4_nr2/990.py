#include<cstdio>
#include<vector>
#include<cstdlib>
#include<climits>
#include<iostream>
#include<memory.h>
#include<algorithm>
#define LL long long
#define _min(a, b) ((a) < (b) ? (a) : (b))
#define _max(a, b) ((a) > (b) ? (a) : (b))
using namespace std;

int n, m, d, T;
char a[555][555];
int main()
{
//*
	freopen(".in", "r", stdin);
	freopen(".out", "w", stdout);
//*/
	cin>> T;
	for (int tt = 1; tt <= T; tt++)
	{
		int ans = 0;
		cin>> n>> m>> d;
		gets(a[0]);
		for (int i = 1; i <= n; i++) gets(a[i] + 1);
		for (int i = 1; i <= n; i++) for (int j = 1; j <= m; j++)
		{
			for (int k = 3; k <= _min(n - i + 1, m - j + 1); k++)// if (i == 2 && j == 2 && k == 5)
			{
				
				if (k < ans) continue;
				double x = 0, y = 0;
				double x1 = i + (double) (k - 1) / 2., y1 = j + (double) (k - 1) / 2.;
				for (int ii = i; ii < i + k; ii++) for (int jj = j; jj < j + k; jj++)
				{
					if (ii == i && (jj == j || jj == j + k - 1)) continue;
					if (ii == i + k - 1 && (jj == j || jj == j + k - 1)) continue;
					x += (a[ii][jj] - 48 + d) * (ii - x1), y += (a[ii][jj] - 48 + d) * (jj - y1);
				}
				if (x == 0 && y == 0) ans = k;
//				cout<< x<< " "<< y<< endl;
			}
		}
		printf("Case #%d: ", tt);
		if (!ans) puts("IMPOSSIBLE");else cout<< ans<< endl;
	}
	return 0;
}
