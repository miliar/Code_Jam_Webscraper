#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <iostream>
using namespace std;

int g[1010];

int main(){

	int T;

	freopen("C-small.in","r",stdin); freopen("C-small.out", "w", stdout);
	//freopen("C-large.in","r",stdin); freopen("C-large.out", "w", stdout);
	
	scanf("%d", &T);

	for (int test = 1; test <= T; test++)
	{
		int R, k, n;
		int res = 0;

		scanf("%d %d %d", &R, &k, &n);
		for (int i = 0; i < n; i++)
			scanf("%d", &g[i]);

		int j = 0;
		for (int i = 0; i < R; i++)
		{
			int sum = 0;
			int cur = j;
			sum += g[j];
			j = (j + 1) % n;

			while (sum <= k)
			{
				if(sum + g[j] <= k && j != cur)
				{
					sum += g[j];
					j = (j + 1) % n;
				}
				else
					break;
			}
			res += sum;

		}

		printf("Case #%d: %d\n", test, res);

	}
	return 0;
}