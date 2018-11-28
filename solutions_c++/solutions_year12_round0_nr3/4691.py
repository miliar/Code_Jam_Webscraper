#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>

using namespace std;

int main( )
{
	int t, tt, r = 0;
	int A, B, n, m;
	
	freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);

	scanf("%d\n", &tt);
	for(t = 1; t <= tt; t++)
	{
		scanf("%d %d", &A, &B);
		n = A; r = 0;

		if (B < 10) 
		{
			printf("Case #%d: %d\n", t, r);
			continue;
		}
		
		int j = 1;
		for (int i = A; i <= B; i++)
		{
			if (i < 100) j = 2;
			else if (i < 1000) j = 3;
			else if (i < 10000) j = 4;
			else if (i < 100000) j = 5;
			else if (i < 1000000) j = 6;
			else if (i < 10000000) j = 7;

			for (int k = 1; k < j; k++)
			{
				int tn = n % (int)(pow((double)10, k));
				if (tn == 0) continue;
				m = tn * (int)(pow((double)10, j - k)) + ((n - tn) / (int)(pow((double)10, k)));
				if (n < m && n >= A && m <= B) r++;
				else continue;
			}
			n++;
		}
		printf("Case #%d: %d\n", t, r);
	}

	return 0;
}