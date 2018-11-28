#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <iostream>
using namespace std;

const int N=60;
char s[N][N];
int r, c, t, t1;

int main()
{
	//freopen("A-small-attempt2.in", "r", stdin);
//	freopen("A-small-attempt2.out", "w", stdout);
	int i, j, k, flag, flag1;
	scanf("%d", &t);
	for(t1=1; t1<=t; t1++)
	{
		scanf("%d%d", &r, &c);
		for(i=0; i<r; i++)
			scanf("%s", &s[i]);
		
		flag1=1;
		for(i=0; i<r; i++)
		{
			for(j=0; j<c; j++)
			{
				if(s[i][j]=='#')
				{
					flag = 0;
					if(i<r-1 && j<c-1)
					{
						if(s[i+1][j]=='#' && s[i+1][j]=='#' && s[i+1][j]=='#')
						{
							flag = 1;
							s[i][j] = s[i+1][j+1] = '/';
							s[i][j+1] = s[i+1][j] = '\\';
						}	
					}
					if(flag==0)
					{
						flag1 = 0;
						break;
					}
				}
			}
			if(flag1==0)
				break;
		}
		printf("Case #%d:\n", t1);
		if(flag1==1)
		{
			for(i=0; i<r; i++)
				printf("%s\n", s[i]);
		}
		else
			printf("Impossible\n");
	}

	return 0;
}