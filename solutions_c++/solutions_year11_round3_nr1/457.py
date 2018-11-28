#include <stdio.h>
#include <cmath>
#include <string>
#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int t, T;
int i,j,k;
int r,c;
char a[100][100];

int main()
{
	bool imp;
	freopen("D:\\A-large.in", "r", stdin);
	freopen("D:\\A-large.out", "w", stdout);
	scanf("%d", &T);
	for (t=1; t<=T; t++)
	{
		scanf("%d%d", &r,&c);
		for(i=0; i<r; i++)
		{
			scanf("%s", a[i]);
		}
		for(i=0; i<r-1; i++)
		{
			for(j=0; j<c-1; j++)
			{
				if (a[i][j]=='#' && a[i+1][j]=='#' && a[i][j+1]=='#' && a[i+1][j+1]=='#')
				{
					a[i][j]='/';
					a[i+1][j]='\\';
					a[i][j+1]='\\';
					a[i+1][j+1]='/';
				}
			}
		}
		printf("Case #%d:\n", t);
		imp = false;
		for(i=0; i<r; i++)
		{
			for(j=0; j<c; j++)
			{
				if (!imp && a[i][j]=='#')
				{
					printf("Impossible\n");
					imp = true;
				}
			}
		}
		if (!imp)
		{
			for(i=0; i<r; i++)
			{
				printf("%s\n", a[i]);
			}
		}
	}



	return 0;
}