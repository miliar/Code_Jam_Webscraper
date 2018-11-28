#include<stdio.h>

__int64 x[111111], y[111111], a[11];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("aL.ans", "w", stdout);

	__int64 t, test, n, A, B, C, D, M, i, xx, yy, res, m, indx, j, k;
	scanf("%I64d", &test);
	for(t=0; t<test; t++)
	{
		scanf("%I64d %I64d %I64d %I64d %I64d %I64d %I64d %I64d", &n, &A, &B, &C, &D, &x[0], &y[0], &M);
		for(i=1; i<n; i++)
		{
			x[i]= (A*x[i-1] + B)%M;
			y[i]= (C*y[i-1] + D)%M;
		//	printf("%d %d\n", x[i], y[i]);
		}
//		res=0;
//		for(i=0; i<n; i++)
//			for(j=i+1; j<n; j++)
//				for(k=j+1; k<n; k++)
//					if((x[i]+x[j]+x[k])%3==0 && (y[i]+y[j]+y[k])%3==0)
//						res++;
//printf("Case #%I64d: %I64d\n", t+1, res);


		for(i=0; i<10; i++)
			a[i]=0;
		for(i=0; i<n; i++)
		{
			xx=x[i]%3;
			yy=y[i]%3;
			indx= xx*3 + yy +1;
			a[indx]++;
		}
		res=0;
		for(i=1; i<=9; i++)
		{
			m=a[i];
			res+=(m*(m-1)*(m-2)/6);
		}
		res+=(a[1]*a[2]*a[3]);
		res+=(a[4]*a[5]*a[6]);
		res+=(a[7]*a[8]*a[9]);
		res+=(a[1]*a[4]*a[7]);
		res+=(a[2]*a[5]*a[8]);
		res+=(a[3]*a[6]*a[9]);
		res+=(a[1]*a[5]*a[9]);
		res+=(a[1]*a[6]*a[8]);
		res+=(a[2]*a[4]*a[9]);
		res+=(a[2]*a[6]*a[7]);
		res+=(a[3]*a[4]*a[8]);
		res+=(a[3]*a[5]*a[7]);
		printf("Case #%I64d: %I64d\n", t+1, res);

	}
	return 0;
}

		
