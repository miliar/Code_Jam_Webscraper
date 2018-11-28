/*
3
2 3
###
###
1 1
.
4 5
.##..
.####
.####
.##..


Case #1:
Impossible
Case #2:
.
Case #3:
./\..
.\//\
./\\/
.\/.. 
*/

#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int R;
int C;
char IN[60*60];

int check()
{
	for(int r=0; r<R; r++)
	{
		for(int c=0; c<C; c++)
		{
			if(IN[r*C+c] == '#' && IN[r*C+c+1] == '#' && IN[(r+1)*C+c] == '#' && IN[(r+1)*C+c+1] == '#')
			{
				IN[r*C+c] = '/';
				IN[r*C+c+1] = '\\';
				IN[(r+1)*C+c] = '\\';
				IN[(r+1)*C+c+1] = '/';
			}
			else
				IN[r*C+c] = IN[r*C+c];
		}
	}

	int found=0;
	for(int r=0; r<R; r++)
	{
		for(int c=0; c<C; c++)
		{
			if(IN[r*C+c] == '#')
			{
				return 0;
			}
		}
	}

	return 1;
}

int main()
{
	freopen("input.txt", "rt", stdin);

	int num;
	scanf("%d", &num);
//printf("num=%d\n", num);

	for (int ii=0; ii<num; ii++)
	{
		scanf("%d %d", &R, &C);
//printf("%d %d\n", R, C);

		for(int r=0; r<R; r++)
		{
			char s[60];
			scanf("%s", s);

			for(int c=0; c<C; c++)
			{
				IN[r*C+c] = s[c];
//printf("%c", IN[r*C+c]);
			}
//printf("\n");
		}

		int result = check();

		printf("Case #%d:\n", ii+1);
		if(result == 0)
		{
			printf("Impossible\n");
		}
		else
		{
			for(int r=0; r<R; r++)
			{
				for(int c=0; c<C; c++)
				{
					printf("%c", IN[r*C+c]);
				}
				printf("\n");
			}
		}
	}

	return 0;
}

