#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

#define MAXN 1001

int a[MAXN];
int a2[MAXN];
int b[MAXN];
int b2[MAXN];

int main()
{
//	freopen("input","r",stdin);
//	freopen("output","w",stdout);
	int tt;
	scanf("%d\n", &tt);
	for (int t = 0; t < tt; ++t)
	{
		int n;
		scanf("%d", &n);
		int n1 = 0, n2 = 0;
		for (int i = 0; i < n; ++i)
		{
			char c;
			int k;
			scanf(" %c %d", &c, &k);
			if (c == 'O')
				a[n1] = k, a2[n1++] = i;
			else
				b[n2] = k, b2[n2++] = i;
		}
		scanf("\n");
		int ans = 0;
		for (int i1 = 0, i2 = 0, c1 = 1, c2 = 1; i1 < n1 || i2 < n2; )
		{
			if (i1 < n1 && i2 < n2)
			{
				if (a2[i1] < b2[i2])
				{
					if (c1 < a[i1])
						++c1;
					else if (c1 > a[i1])
						--c1;
					else
						++i1;
						
					if (c2 < b[i2])
						++c2;
					else if (c2 > b[i2])
						--c2;
				}
				else
				{
					if (c1 < a[i1])
						++c1;
					else if (c1 > a[i1])
						--c1;
						
					if (c2 < b[i2])
						++c2;
					else if (c2 > b[i2])
						--c2;
					else
						++i2;
				}
			}
			else if (i1 < n1)
			{
				if (c1 < a[i1])
					++c1;
				else if (c1 > a[i1])
					--c1;
				else
					++i1;			
			}
			else
			{
				if (c2 < b[i2])
					++c2;
				else if (c2 > b[i2])
					--c2;
				else
					++i2;
			}
			++ans;
		}
		printf("Case #%d: %d\n", t + 1, ans);		
	}
	return 0;
}
