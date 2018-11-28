#include <iostream>
#include <stdio.h>
#include <set>
#include <map>
#include <list>
#include <algorithm>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <vector>

using namespace std;

int main()
{
	int nTestCases;
	int i, j, k, l, m;
	int R, C, r, c, flag=true;;
	char arr[80][80];


	scanf ("%d", &nTestCases);
	for (i=1; i<=nTestCases; ++i)
	{
		scanf("%d%d", &R, &C);

		memset(arr, 0, sizeof(arr));
		for (j=0; j<R; ++j)
			scanf("%s", arr[j]);

		flag=true;
		//for (j=0; j<R; ++j)
		//{
		//	c=0;
		//	for (k=0; k<C; ++k)
		//	{
		//		if (arr[j][k] == '#')
		//			++c;
		//	}

		//	if (c % 2 != 0)
		//		break;
		//}
		//if (j != R)
		//{
		//	flag=false;
		//}
		//for (j=0; j<R; ++j)
		//{
		//	c=0;
		//	for (k=0; k<C; ++k)
		//	{
		//		if (arr[k][j] == '#')
		//			++c;
		//	}

		//	if (c % 2 != 0)
		//		break;
		//}
		//if (j != R)
		//{
		//	flag=false;
		//}

		if (flag)
		{
			for (j=0; j<R; ++j)
			{
				for (k=0; k<C; ++k)
				{
					if (arr[j][k] == '#')
					{
						if (arr[j][k+1] != '#' || arr[j+1][k] != '#' || arr[j+1][k+1] != '#')
							flag = false;

						if (!flag)
							break;
						
						arr[j][k] = '/';
						arr[j][k+1] = '\\';
						arr[j+1][k] = '\\';
						arr[j+1][k+1] = '/';
					}
				}

				if (!flag)
					break;
			}
		}

		printf ("Case #%d:\n", i); 
		if (!flag)
			printf("Impossible\n");
		else
		{
			for (j=0; j<R; ++j)
				printf("%s\n",arr[j]);
		}

	}

	return 0;
}