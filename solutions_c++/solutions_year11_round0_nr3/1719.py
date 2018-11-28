#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

const int maxX = 1048576;
const int maxN = 1010;

int t, n;
int dp[2][maxX];
int ar[maxN];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for (int q = 0; q < t; q++)
	{
		scanf("%d", &n);
		int minn = 0, sumx = 0, sum = 0;
		for (int i = 0; i < n; i++)
		{
			scanf("%d", &ar[i]);
			if (i == 0 || ar[i] < minn)
			{
				minn = ar[i];
			}
			sum += ar[i];
			sumx ^= ar[i];
		}
		printf("Case #%d: ", q + 1);
		if (sumx)
		{
			printf("NO\n");
		}
		else
		{
			printf("%d\n", sum - minn);
		}
	}
	return 0;
}