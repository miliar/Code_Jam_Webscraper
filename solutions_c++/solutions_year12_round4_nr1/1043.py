#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<string>
#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<queue>
#include<math.h>
using namespace std;



int d[10005] = {0};
int l[10005] = {0};

int r[10005] = {0};

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int tt;
	scanf("%d", &tt);

	for(int t = 0; t < tt; t++)
	{
		int n;
		scanf("%d", &n);

		for(int i = 0; i < n; i++)
			scanf("%d%d", &d[i], &l[i]);

		int dst;
		scanf("%d", &dst);


		memset(r, 0, sizeof(int) * 10005);
		bool f = 0;
		r[0] = min(l[0], d[0]);

		for(int i = 0; i < n; i++)
		{
			for(int j = i + 1; j <= n; j++)
			{
				if(n == j && dst - d[i] > r[i])
					break;
				if(n != j && (d[j] - d[i]) > r[i])
					break;
				if(j == n)
				{
					f = 1;
					break;
				}

				r[j] = max(r[j], min(l[j], d[j] - d[i]));
			}
			if(f)
				break;
		}


		printf("Case #%d: ", t+1);
		if(f)
			printf("YES\n");
		else
			printf("NO\n");
	}

	return 0;
}


