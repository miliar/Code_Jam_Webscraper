#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <assert.h>
#include <time.h>
#include <math.h>

#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <functional>
#include <string>
#include <set>
#include <map>
#include <iostream>


using namespace std;
typedef double tip;
const int inf = 0x7fffffff;
const tip eps = 1e-10;

int s[200];
int n;
int x;

int is_eliminated(int c, tip mid)
{
	int i, j, k;
	tip cs = s[c] + mid*x;
	
	for (i = 0; i < n; i++)
	{
		if (i == c) { continue; }
		mid += max((tip)0, (cs-s[i])/x);
	}
	
	return mid <= 1;
}

tip solve(int c)
{
	tip lo = 0, hi = 1, mid;
	
	while (hi - lo > eps)
	{
		mid = (hi + lo) / 2;
		if (is_eliminated(c, mid))
			lo = mid;
		else
			hi = mid;
	}

	return hi;
}

int main()
{
	int t;
	int i, j, k;
	scanf("%d", &t);
	for (int tt = 0; tt < t; tt++)
	{
		printf("Case #%d:", tt+1);
		x = 0;
		scanf("%d", &n);
		for (i = 0; i < n; i++)
		{
			scanf("%d", s+i);
			x += s[i];
		}
		for (i = 0; i < n; i++)
		{
			printf(" %f", solve(i)*100.0);
		}
		printf("\n");
	}
	
	return 0;
}

