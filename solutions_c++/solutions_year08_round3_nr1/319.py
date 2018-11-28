#include<stdio.h>

__int64 a[1111], P, K, L, i, j, d, res, tmp, n, t, test;

int main()
{
	freopen("A-large.in.txt", "r", stdin);
	freopen("aL.ans", "w", stdout);
	scanf("%I64d", &test);
	for(t=0; t<test; t++)
	{
		scanf("%I64d %I64d %I64d", &P, &K, &L);
		n=L;
		for(i=0; i<L; i++)
			scanf("%I64d", &a[i]);
		for(i=0; i<n; i++)
			for(j=i+1; j<n; j++)
				if(a[i]<a[j])
				{
					tmp=a[i];
					a[i]=a[j];
					a[j]=tmp;
				}
		for(i=0; i<n; i++)
		{
			d=i/K;
			a[i]=a[i]*(d+1);
		}
		res=0;
		for(i=0; i<n; i++)
			res+=a[i];
		printf("Case #%I64d: %I64d\n", t+1, res);
	}
	return 0;
}


