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
#define MAX 1024
using namespace std;
int line[MAX][2];
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int nt, it;
	int i,j;
	unsigned int sum;
	scanf("%d", &nt);
	for (it = 1; it <= nt; it++)
	{
		int n;
		sum = 0;
		memset(line,0,sizeof(line));
		scanf("%d",&n);
		for (i=0; i<n; ++i)
		{
			scanf("%d%d",&line[i][0],&line[i][1]);
		}

		for (i=0; i<n; ++i)
		{
			for (j=0; j<i; ++j)
			{
				if (line[i][0] < line[j][0] && line[i][1] > line[j][1])
				{
					sum++;
				}
				if (line[i][0] > line[j][0] && line[i][1] < line[j][1])
				{
					sum++;
				}
			}
		}
		printf("Case #%d: %d\n",it,sum);
	}
	return 0;
}