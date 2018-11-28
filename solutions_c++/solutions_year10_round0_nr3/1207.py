#include <stdio.h>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <map>
using namespace std;


int a[1002];
int h[1002*2];
int b[1002*2][2];

int main()
{

	int ca, c;

	int r, k, n;
	int i, j;

	__int64 ans = 0, sum = 0;


	freopen("c:\\C-large.in", "r", stdin);
	freopen("c:\\C-large.out", "w+", stdout);

	scanf("%d", &ca);
	for(c = 1; c <= ca; c++)
	{
		memset(a, 0, sizeof(a));
		memset(b, 0, sizeof(b));
		memset(h, 0, sizeof(h));
		sum = 0;
		scanf("%d%d%d", &r, &k, &n);
		for(i = 1; i <= n; i++)
		{
			scanf("%d", &a[i]);
			sum += a[i];
			h[i] = h[i-1] + a[i];
		}
		for(i = n+1;i <= 2*n; i++)
		{
			h[i] = h[i-1] + a[i-n];
		}

	//	for(i = 1;i <= 2*n; i++) printf("%d ", h[i]); printf("\n");


		if(sum <= k)
		{
			ans = sum * (__int64)r;
		}
		else
		{
			for(i = 1;i <= n; i++)
			{
				for(j = i;j <= 2*n; j++)
				{
					if(h[j] - h[i-1] > k)
					{
						break;
					}
				}
				b[i][0] = j%n;
				if(j%n==0) b[i][0]=n;
				b[i][1] = h[j-1] - h[i-1];
			//	printf("%d %d\n", b[i][0], b[i][1]);
			}

			ans = 0;
			j = 1;
			for(i = 1;i <= r; i++)
			{
				ans += b[j][1];
			//	printf("%d ** %d\n", j, b[j][1]);
				j = b[j][0];
			}
		}

		printf("Case #%d: %I64d\n", c, ans);

	}
	return 0;
}