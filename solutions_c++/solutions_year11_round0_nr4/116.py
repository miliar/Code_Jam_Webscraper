#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std; 
int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("GCJ_D1.txt", "w", stdout);
	int T, N, tcnt = 0;
	int candy[1010];
	scanf("%d", &T);
	for (int tcnt = 1; tcnt <= T; tcnt++)
	{
		int n;
		scanf("%d", &n);
		int per[1010], cnt = 0;
		for (int i = 0; i < n; i++)
		{
			scanf("%d", &per[i]);
			if (per[i] != i + 1)
				cnt++;
		}
		
		printf("Case #%d: %.6lf\n", tcnt, (double)cnt);
	}
}
