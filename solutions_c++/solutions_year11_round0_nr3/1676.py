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
	int N, min=99999999, res, sum=0;

	scanf ("%d", &nTestCases);
	for (i=1; i<=nTestCases; ++i)
	{
		scanf ("%d", &N);

		min = 99999999;
		sum=0;
		res = 0;
		for (j=0; j<N; ++j)
		{
			scanf ("%d", &k);

			if (k < min)
				min = k;

			res ^= k;
			sum += k;
		}

		printf ("Case #%d: ", i); 
		if (res != 0)
			printf ("NO\n");
		else
			printf ("%d\n", (sum - min));
	}

	return 0;
}