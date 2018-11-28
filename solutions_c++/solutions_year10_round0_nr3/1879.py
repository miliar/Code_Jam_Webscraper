#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <sstream>
#include <set>
#include <math.h>

#define N 1001
using namespace std;
 
int main ()
{
    int T, i = 1, j = 0, l;
    int n, k, r;
	int groups [N], count [N], euro [N];

    scanf ("%d", &T);
 
    while (T) 
	{
		T --;
		
		scanf ("%d %d %d", &r, &k, &n);

		for (j = 0; j < n; j ++)
			scanf ("%d", &groups [j]);

		for (j = 0; j < n; j ++)
		{
			int sum = 0;
			for (l = 0; l < n; l ++)
			{
				if (sum + (groups [(j + l) % n]) > k)
					break;

				sum += (groups [(j + l) % n]);
			}

			euro [j] = sum;
			count [j] = l;
		}
        
		int start = 0;
		long long ans = 0, sum_cycle = 0;
		vector <long long> cycle;
		int flag [N];
		memset (flag, 0, sizeof(flag));

		for (j = 0; j < r; j ++)
		{
			flag [start] ++;

			if (flag [start] == 3)
				break;
			if (flag [start] == 2)
			{
				cycle.push_back (euro [start]);
				sum_cycle += euro [start];
			}

			ans += euro [start];
			start = start + count [start];
			start = start % n;
		}

		int left = r - j;
		int ncycle = cycle.size();

		if (ncycle)
		{
			ans += (left / ncycle) * sum_cycle;
			for (j = 0; j < (left % ncycle); j ++)
				ans += cycle [j];
		}
		printf ("Case #%d: %lld\n", i, ans);

		i ++;
    }
 
    return 0;
}
