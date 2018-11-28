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

#define SZ 1005

char dat[SZ][SZ];

int main()
{
	//freopen("A-small-attempt2.in", "rt", stdin);
	//freopen("A-small.out", "wt", stdout);

	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
	int inp, tmp, r, c, kase, k, i, j, pg, pd;
	char ch;
	scanf("%d", &inp);
	
	for(kase = 1; kase <= inp; kase++)
	{
		scanf("%d %d", &r, &c);
		for(i = 0; i < r; i++)
		{
			scanf(" %s", dat[i]);
		}
		bool flag = true;
		
		for(i = 0; i < r - 1; i++)
		{
			for(j = 0; j < c - 1; j++)
			{
				if(dat[i][j] == '#')
				{
					if(dat[i][j + 1] != '#' || dat[i + 1][j] != '#' || dat[i + 1][j + 1] != '#')
					{
						flag = false;
						break;
					}
					dat[i][j] = '/';
					dat[i][j + 1] = '\\';
					dat[i + 1][j] = '\\';
					dat[i + 1][j + 1] = '/';
				}
			}
			if(dat[i][c - 1] == '#')
				flag = false;
			if(!flag)
				break;
		}
		if(r < 2 || c < 2)
		{
			for(i = 0; i < r; i++)
			{
				for(j = 0; j < c; j++)
				{
					if(dat[i][j] == '#')
						flag = false;
				}
			}
		}
		for(j = 0; j < c; j++)
		{
			if(dat[r - 1][j] == '#')
				flag = false;
		}
		printf("Case #%d:\n", kase);
		if(flag)
		{
			for(i = 0; i < r; i++)
			{
				printf("%s\n", dat[i]);
			}
		}
		else
		{
			printf("Impossible\n");
		}
		
		
		
	}
	return 0;
}

