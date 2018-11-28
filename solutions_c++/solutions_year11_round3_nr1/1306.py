#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <cstdio>
#include <vector>
#include <map>
using namespace std;

char a[51][51];
int main()
{//
//	freopen("A-small-attempt0.in", "r", stdin);
//	freopen("A-small.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);


	int T, R, C;
	scanf("%d", &T);
	for(int t=1; t<=T; t++)
	{
		bool flag = true;
		scanf("%d%d", &R, &C);
		printf("Case #%d:\n", t);
		for(int i=0; i<R; i++)
			scanf("%s", a[i]);
		for(int i=0; i<R; i++)
			for(int j=0; j<C; j++)
			{
				if(a[i][j] == '#')
				{
					if(i+1<R && j+1<C)
					{
						if(a[i+1][j+1] == '#' && a[i+1][j] == '#' && a[i][j+1] == '#')
						{
							a[i][j] = '/';
							a[i][j+1] = '\\';
							a[i+1][j] = '\\';
							a[i+1][j+1] = '/';
						}
					}
				}
			}
		for(int i=0; i<R; i++)
			for(int j=0; j<C; j++)
			{
				if(a[i][j] == '#')
				{
					flag = false;
					break;
				}
			}
		if(!flag)
			puts("Impossible");
		else 
		{
			for(int i=0; i<R; i++)
				printf("%s\n", a[i]);
		}
	}
//	while(1);
	return 0;
}