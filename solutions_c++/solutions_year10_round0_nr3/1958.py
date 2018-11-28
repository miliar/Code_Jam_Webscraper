#include <stdio.h>

int main()
{
	int T, test;
	scanf("%d", &T);
	for (test=0;test<T;test++)
	{
		int R, k, n, g[1000], i;
		scanf("%d %d %d", &R, &k, &n);
		for (i=0;i<n;i++)
			scanf("%d", &g[i]);

		int pos = 0, Time[1000], round;
		long long Money[1000], sum, m=0;
		for (i=0;i<n;i++)
			Time[i] = -1, Money[i] = -1;

		Time[0] = 0;
		Money[0] = 0;

		for (round=1;round<=R;round++)
		{
			sum = 0;
			for (i=0;i<n;i++)
			{
				if (sum+g[pos]<=k)
				{
					sum+=g[pos];
					pos = (pos+1)%n;
				}
				else break;
			}
			m+=sum;

			if (Time[pos]==-1)
			{
				Time[pos] = round;
				Money[pos] = m;
			}
			else break;
		}

		long long res=0;

		if (round==R+1) 
			res = m;
		else
		{
			int dR = R-round, dT = round - Time[pos];
			long long dM = m - Money[pos];
			res = m + dM*((long long)(dR/dT));

			R = dR%dT;

			for (round=0;round<R;round++)
			{
				sum = 0;
				for (i=0;i<n;i++)
				{
					if (sum+g[pos]<=k)
					{
						sum+=g[pos];
						pos = (pos+1)%n;
					}
					else break;
				}
				res+=sum;
			}
		}

		printf("Case #%d: %lld\n", test+1, res);
	}
}