#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

void solve(void)
{
	char c;
	int i = 0;
	int j = 0;
	int a[100][100];
	int n;
	scanf("%d", &n);
	scanf("%c", &c);
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n; j++)
		{
			scanf("%c", &(a[i][j]));
			a[i][j] -= '0';
		}
		scanf("%c", &c);
	}
// 	for (i = 0; i < n; i++)
// 	{
// 		for (j = 0; j < n; j++)
// 			cerr << a[i][j] << " ";
// 		cerr << endl;
// 	}
	int r[100];
	for (i = 0; i < n; i++)
	{
		j = n - 1;
		while ((j >= 0) && (a[i][j] == 0))
			j--;
		if (j < 0)
			j = 0;
		r[i] = j;
	}
	for (i = 0; i < n; i++)
		cerr << r[i] << " ";
	cerr << endl;
	int res = 0;
	int zap;
	int ii, jj;
	for (i = 0; i < n; i++)
	{
		j = i;
		while (r[j] > i)
			j++;
		res += j - i;
		for (jj = j; jj > i; jj--)
		{
			for (ii = 0; ii < n; ii++)
			{
				zap = a[jj][ii];
				a[jj][ii] = a[jj - 1][ii];
				a[jj - 1][ii] = zap;
			}
			zap = r[jj];
			r[jj] = r[jj - 1];
			r[jj - 1] = zap;
		}
	}
	cout << res;
}

int main (void) 
{
	//freopen("input1.txt", "r", stdin);
	//freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("output1.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}
}