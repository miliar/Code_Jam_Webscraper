//////////
//
//	Auther: hazy
//	Pro ID:	
//	Pro Profile:  
//	Attention!!: 	
//	Created @ 2008_8
//
//////////
#include <stdio.h>
#include <string.h>

#include <vector>

#include <iostream>
#include <utility>
#include <algorithm>

typedef 	long long 	i64;
using namespace std;
const int MAXN = 100;

int 	cas, T = 0;

int 	n, m;
int 	A;

int 	Area(int a, int b, int c, int d)
{
	return abs( a*d - b*c );
}

int main()
{
	int 	i, j,k;
	
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("b_small.out", "w", stdout);
	
	for (scanf("%d", &cas); cas; cas--)
	{
		scanf("%d %d %d", &n, &m, &A);
		
		int a, b, c, d;

		int 	flag = 0;
		
		printf("Case #%d: ", ++T);
		for (a=0; a<=n; a++)
		for (b=0; b<=m; b++)
			for (c=0; c<=n; c++)
			for (d=0; d<=m; d++)
			{
			//	printf("0 0 %d %d %d %d\n", a, b, c, d);
				if (Area(a, b, c, d) == A)
				{
					flag = 1;
					printf("0 0 %d %d %d %d\n", a, b, c, d);
					goto 	lag;
				}
			}
		lag :  
		
		if (flag == 0)
			printf("IMPOSSIBLE\n");
	}
	return 0;
}
