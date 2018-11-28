#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <assert.h>
#include <time.h>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <functional>
#include <string>
#include <set>
#include <map>
#include <iostream>


int next(int n)
{
	return 1;
}

int main()
{
	int i, j, k;
	int t, a, b;
	int pot, cnt;
	
	scanf("%d", &t);
	
	for (int tt = 0; tt < t; tt++)
	{
		int pot = 1, cnt = 0;
		scanf("%d%d", &a, &b);
		while (10*pot <= a) pot *= 10;
		
		for (i = a; i <= b; i++)
		{
			j = i;
			while (1)
			{
				j = (j % pot) * 10 + j / pot;
				if (j == i) break;
				if (a <= j && j <= b) cnt++;
			}
		}
		printf("Case #%d: %d\n", tt+1, cnt/2);
	}
	
	return 0;
}

