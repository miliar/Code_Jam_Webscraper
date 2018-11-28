#include <iostream>
#include <fstream>
#include <cstdio>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <string>
#include <sstream>
#define MAX 128
using namespace std;
int min(int a,int b,int c)
{
	if (a < b)
	{
		if (c < a) return c;
		else return a;
	}
	else
	{
		if (b < c) return b;
		else return c;
	}
}
char map[MAX][MAX];
char Rmap[MAX][MAX];
int n,K;
void Rotate()
{
	int i,j;
	for (i=0;i<n; ++i)
	{
		for (j=0; j<n; ++j)
		{
			Rmap[j][n-1-i] = map[i][j];
		}
	}
}
void Gravity()
{
	int i,j,k;
	for (j=0; j<n; ++j)
	{
		for (i=n-1; i>=0; --i)
		{
			if (Rmap[i][j] == '.')
			{
				for (k=i-1; k>=0; --k)
				{
					if (Rmap[k][j] != '.')
					{
						swap(Rmap[i][j],Rmap[k][j]);
						break;
					}
				}
			}
		}
	}
}
bool check(char color)
{
	int i,j;
	int c,r,xie;
	for (i=0; i<n; ++i)
	{
		for (j=0; j<n; ++j)
		{
			bool flag = true;
			for (c=0;c<K; ++c)
			{
				if (j+c >= n||Rmap[i][j+c] != color  )
				{
					flag = false;
					break;
				}
			}
			if (flag) return true;

			flag = true;
			for (r=0; r<K ; ++r)
			{
				if (i+r >= n||Rmap[i+r][j] != color)
				{
					flag = false;
					break;
				}
			}
			if (flag) return true;

			flag = true;
			for (xie=0; xie<K; ++xie)
			{
				if (i+xie>=n || j+xie>=n || Rmap[i+xie][j+xie] != color)
				{
					flag = false;
					break;
				}
			}
			if (flag) return true;

			flag = true;
			for (xie=0; xie<K; ++xie)
			{
				if (i+xie>=n || j-xie<0 || Rmap[i+xie][j-xie] != color)
				{
					flag = false;
					break;
				}
			}
			if (flag) return true;
		}
	}
	return false;

}
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("large.txt", "w", stdout);
	int nt, it;
	int i,j;

	scanf("%d", &nt);
	for (it = 1; it <= nt; it++)
	{
		memset(map,0,sizeof(map));
		memset(Rmap,0,sizeof(Rmap));
		
		scanf("%d%d\n",&n,&K);
		for (i=0; i<n; ++i)
		{
			gets(map[i]);
		}
		
		Rotate();
		Gravity();
		bool Blue,Red;
		Blue = check('B');
		Red = check('R');
		if (Blue && Red)
		{
			printf("Case #%d: Both\n",it);
		}
		else
		{
			if (Blue)
			{
				printf("Case #%d: Blue\n",it);
			}
			else
			{
				if (Red)
					printf("Case #%d: Red\n",it);
				else
					printf("Case #%d: Neither\n",it);
			}
		}
	}
	return 0;
}