#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
using namespace std;

char num[20];
char ans[20];
int a[20];

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	int T;
	int cas = 1;
	scanf("%d", &T);

	while(T--)
	{
		int n;
		scanf("%d", &n);

		for(int i=1; i<=n; i++)
			scanf("%d", &a[i]);

		int len;
		len = 1 << n;
		int max = -1;
		for(int i=1; i<len-1; i++)
		{
			int j = i;
			int rlen = n;
			itoa(j, num, 2);
			int llen = strlen(num);
			for(int k=llen-1; k>=0; k--)
			{
				ans[rlen--] = num[k];
			}
			while (rlen)
			{
				ans[rlen--] = '0';
			}
			
			//puts(num);
			//puts(ans);
			int x = 0, y = 0;
			int total = 0;
			for(int k=1; k<=n; k++)
			{
				if(ans[k] == '0')
				{
					x ^= a[k];
					total += a[k];
				}
				else
					y ^= a[k];
			}
			if(max < total && x == y)
				max = total;
		}

		printf("Case #%d: ", cas ++);
		if(max == -1)
			puts("NO");
		else
			printf("%d\n", max);
	}
}