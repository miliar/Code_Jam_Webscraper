#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>
#include <set>
#include <algorithm>
#include <iostream>
using namespace std;

typedef __int64 LL;
typedef unsigned __int64 uLL;

int max(int a, int b)
{
	if (a>b) return a;
	return b;
}

int min(int a, int b)
{
	if (a>b) return b;
	return a;
}

struct point
{
	int start, end;
	point (){}
};

int main()
{
	freopen("a.in.txt","r",stdin);
	freopen("a.out.txt","w",stdout);

	int kase, tCase = 0;
	scanf ("%d",&kase);

	while (kase--)
	{
		int i, j, k, l, m, n, p, N, count = 0;
		scanf ("%d",&N);
		point hold[1500];
		for (i=0; i<N; i++) scanf ("%d%d", &hold[i].start, &hold[i].end);
		for (j=0; j<N; j++)
		{
			for (k=0; k<N; k++)
			{
				if (k==j) continue;
				if (hold[j].start < hold[k].start && hold[j].end > hold[k].end)
					count++;
			}
		}
		printf ("Case #%d: %d\n", ++tCase, count);
	}

	return 0;
}
