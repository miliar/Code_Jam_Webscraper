#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>

using namespace std;

int a[1010], b[1010];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int ntests;
	scanf("%d", &ntests);
	for (int itest = 1; itest <= ntests; itest++)
	{
		int n, res = 0;
		scanf("%d", &n);
		for (int i = 0; i < n; i++) 
		{
			scanf("%d %d", &a[i], &b[i]);
			for (int j = 0; j < i; j++)
			{
				if (a[i] > a[j] && b[i] < b[j] || a[i] < a[j] && b[i] > b[j]) 
				{
					res++;
				}
			}
		}

		printf("Case #%d: %d\n", itest, res);
	}
	return 0;
}