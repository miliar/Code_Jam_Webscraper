#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <math.h>
#include <string>
#include <string.h>
using namespace std;

char o_r[64][64];
char r[64][64];
int di[4] = {1, 0, 1, 1};
int dj[4] = {0, 1, 1,-1};

bool Check(int i, int j, int d, int k, int n)
{
	char T = r[i][j];
	int pi = i;
	int pj = j;
	for(int rr = 1; rr < k; rr++)
	{
		pi += di[d];
		pj += dj[d];
		if(pi < 0 || pi >= n || pj < 0 || pj >= n)
			return 0;
		if(r[pi][pj] != T)
			return 0;
	}
	return 1;
}

void Solve()
{
	memset(o_r, 0, sizeof(o_r));
	int n, k;
	cin >> n >> k;
	for(int i = 0; i < n; i++)
		scanf("%s", o_r[i]);
	for(int j = 0; j < n; j++)
	{
		int p = n - 1;
		for(int i = n - 1; i >= 0; i--)
		{
			while(p >= 0 && o_r[j][p] == '.')
				p--;
			r[i][n - j - 1] = (p >= 0) ? o_r[j][p] : '.';
			p--;
		}
	}
	bool blue = 0;
	bool red = 0;
	for(int i = 0; i < n; i++)
	{
		for(int j = 0; j < n; j++)
		{
			for(int d = 0; d < 4; d++)
			{
				if(r[i][j] != '.' && Check(i, j, d, k, n))
				{
					if(r[i][j] == 'R')
						red = 1;
					else
						blue = 1;
					break;
				}
			}
		}
	}
	if(blue && red)
		cout << "Both" << endl;
	else if(red)
		cout << "Red" << endl;
	else if(blue)
		cout << "Blue" << endl;
	else
		cout << "Neither" << endl;
}

int main()
{
	freopen("d:\\input.in", "r", stdin);
	freopen("d:\\output.out", "w", stdout);
	int C;
	cin >> C;
	for(int r = 1; r <= C; r++)
	{
		cout << "Case #" << r << ": ";
		Solve();
	}
	return 0;
}
