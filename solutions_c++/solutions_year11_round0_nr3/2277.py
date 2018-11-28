#include <stdio.h>
#include <string.h>
#include <math.h>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#define mp(a, b) make_pair(a, b)
#define pair_mst pair <int, pair <int, int> >

using namespace std;

int main()
{
	int t, p = 0, n;
	
//	freopen("C-large.in", "r", stdin);
//	freopen("C-large.out", "w", stdout);
	
	scanf("%d", &t);
	while (t--)
	{
		long long arr[1005], sum_b = 0, sum = 0;
		
		p++;
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
		{
			scanf("%lld", &arr[i]);
			sum_b ^= arr[i];
			sum += arr[i];
		}
		
		if (sum_b == 0)
		{
			sort(arr, arr + n);
			printf("Case #%d: %lld\n", p, sum - arr[0]);
		}
		else
			printf("Case #%d: NO\n", p);
	}

   return 0;
}
