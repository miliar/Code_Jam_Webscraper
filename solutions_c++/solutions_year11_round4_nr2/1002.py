#pragma warning (disable : 4786)
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <algorithm>
#include <map>
#include <iostream>
#include <sstream>
#include <queue>
#include <cstring>
#include <ctime>
#include <cfloat>

using namespace std;

#define EPS 1e-9

#define SZ 1005

int maze[SZ][SZ];

double getmassx(int x, int y, int k)
{
	int i, j;
	double sumx = 0;
	double summ = 0;
	for(i = x; i < x + k; i++)
	{
		int xx = i - x;
		for(j = y; j < y + k; j++)
		{
			
			int yy = j - y;
			if(xx == 0 && yy == 0)
				continue;
			if(xx == 0 && yy == k - 1)
				continue;
			if(xx == k - 1 && yy == 0)
				continue;
			if(xx == k - 1 && yy == k - 1)
				continue;
				
			sumx += ((yy + 0.5) * maze[i][j]);
			summ += maze[i][j];
		}
	}
	double ret = (double)sumx / summ; 
	return(ret);
}

double getmassy(int x, int y, int k)
{
	int i, j;
	double sumx = 0;
	double summ = 0;
	for(i = x; i < x + k; i++)
	{
		int xx = i - x;
		for(j = y; j < y + k; j++)
		{
			int yy = j - y;
			if(xx == 0 && yy == 0)
				continue;
			if(xx == 0 && yy == k - 1)
				continue;
			if(xx == k - 1 && yy == 0)
				continue;
			if(xx == k - 1 && yy == k - 1)
				continue;
				
			sumx += (xx + 0.5) * maze[i][j];
			summ += maze[i][j];
		}
	}
	double ret = (double)sumx / summ; 
	return(ret);
}

int main()
{
	freopen("B-small-attempt0.in", "rt", stdin);
	freopen("B-small.out", "wt", stdout);

	//freopen("B-large.in", "rt", stdin);
	//freopen("B-large.out", "wt", stdout);
	int inp, r, kase, n, m, c, d, k, i, j, l, t;
	string s1, s2;
	char str[SZ];
	scanf("%d", &inp);
	
	for(kase = 1; kase <= inp; kase++)
	{
	
		scanf("%d %d %d", &r, &c, &d);
		gets(str);

		for(i = 0; i < r; i++)
		{	
			gets(str);
			for(j = 0; j < c; j++)
			{
				//scanf("%d", &maze[i][j]);
				maze[i][j] = d + str[j] - '0';
			}
		}

		int mn = (r > c)?c: r;

		bool flag = false;
		for(k = mn; k >= 3; k--)
		{
			for(i = 0; i <= r - k; i++)
			{
				for(j = 0; j <= c - k; j++)
				{
					double xm = getmassx(i, j, k);
					double ym = getmassy(i, j, k);
					if(fabs(xm - (double)(k) / 2.0) < EPS && fabs(ym - (double)(k) / 2.0) < EPS)
					{
						flag = true;
						break;
					}
				}
				if(flag)
					break;
			}
			if(flag)
				break;
		}

		printf("Case #%d: ", kase);
		if(flag)
			printf("%d\n", k);
		else
			printf("IMPOSSIBLE\n");
		
	
	}
	return 0;
}

