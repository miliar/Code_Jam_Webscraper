#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main(void)
{
	int cas;
	freopen("C-large.in", "r", stdin);
	freopen("my.out", "w", stdout);
	scanf("%d", &cas);
	int t;
	for(t = 1; t <= cas; t++)
	{
		int n;
		scanf("%d", &n);
		int cmin = 100000000;
		int sum = 0;
		int result = 0;
		int i, j;
		for(i = 1; i <= n; i++)
		{
			int tmp;
			scanf("%d", &tmp);
			if(tmp < cmin)
				cmin = tmp;
			sum += tmp;
			result = result ^ tmp;
		}
		if(result == 0)
		{
			printf("Case #%d: %d\n", t, sum - cmin); 
		}
		else 
		{
			printf("Case #%d: NO\n", t);
		}

	}
	return 0;
}