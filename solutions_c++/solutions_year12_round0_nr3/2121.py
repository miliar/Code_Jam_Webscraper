#include <stdio.h>

int t,T;
int n,a,b,k,m;
int i;
int r;

int main()
{
	freopen("D:\\C-large.in", "r", stdin);
	freopen("D:\\C-large.out", "w", stdout);

	scanf("%d", &T);

	for (t = 1; t<=T; t++)
	{
		scanf("%d%d", &a, &b);
		r = 0;

		for (i=a; i<=b; i++)
		{
			for (k=1; k<=i; k*=10);
			k/=10;
			m = i;
			do
			{
				m = (m%10)*k+m/10;
				if (m<i && m >= a && m <=b && m>=k)
				{
					r++;
				}
			} while (m!=i);
		}
		
		printf("Case #%d: %d\n", t, r);
    }

	return 0;
}