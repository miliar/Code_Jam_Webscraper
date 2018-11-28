#include <stdio.h>
#include <algorithm>

using namespace std;

int main()
{
	int t,n,s,p;
	int a[102];
	int i,j,k;
	int ans,tmp;

	scanf("%d", &t);
	for(k = 1; k <= t; k++)
	{
		scanf("%d %d %d", &n, &s, &p);
		j = 0;
		ans = 0;
		for(i = 0; i < n; i++)
		{
			scanf("%d", &tmp);
			if(tmp >= 3 * p - 2)
			{
				ans++;
				continue;
			}
			a[j++] = tmp;
		}
		
		for(i = 0; i < j && s > 0; i++)
		{
			if(a[i] >= 3 * p - 4 && a[i] > p)
			{
				ans++;
				s--;
			}
		}

		printf("Case #%d: %d\n", k, ans);
	}
	return 0;
}
