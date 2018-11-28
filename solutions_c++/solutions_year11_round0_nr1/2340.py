#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#define Max 105

using namespace std;

char str[Max];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int z, zi, n, a, b, wa, wb, ans, i, t, tt;

	scanf("%d", &z);

	for(zi=1;zi<=z;zi++)
	{
		scanf("%d", &n);

		a = 1, b = 1;
		wa = 0, wb = 0;

		ans = 0;
		for(i=0;i<n;i++)
		{
			scanf("%s %d", str, &t);

			if(str[0] == 'B')
			{
				tt = max(abs(a-t) - wa, 0) + 1;
				ans += tt;

				wa = 0;
				wb += tt;

				a = t;
			}
			else
			{	
				tt = max(abs(b-t) - wb, 0) + 1;
				ans += tt;

				wa += tt;
				wb = 0;

				b = t;
			}
		}
		printf("Case #%d: %d\n", zi, ans);
	}
}


