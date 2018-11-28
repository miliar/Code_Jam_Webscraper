#include<stdio.h>
#include<math.h>

int a[111], b[111], c[111], d[111], n, m;
long double A[1111], B[1111], C[1111];
long double ret;

void Go(long double ox, long double oy, long double oz)
{
	int l1;

	long double mp = -1e100;
	for(l1=0;l1<n;l1++)
	{
		long double curr = (abs(ox - a[l1]) + abs(oy - b[l1]) + abs(oz - c[l1])) / d[l1];
		if(curr > mp) mp = curr;
	}
	if(mp < ret) ret = mp;
}

int main(void)
{
	int T, l0;
	int l1, l2, l3;

	freopen("small.in","r",stdin);
	freopen("small.out","w",stdout);
	//freopen("input.txt","r",stdin);

	scanf("%d",&T);
	for(l0=1;l0<=T;l0++)
	{
		m = 0;
		scanf("%d",&n);
		for(l1=0;l1<n;l1++)
		{
			scanf("%d %d %d %d",&a[l1],&b[l1],&c[l1],&d[l1]);
		}

		for(l1=0;l1<n;l1++)
		{
			A[m] = a[l1];
			B[m] = b[l1];
			C[m] = c[l1];
			m++;
			for(l2=l1+1;l2<n;l2++)
			{
				A[m] = ((long double)a[l1] + a[l2]) / 2.0;
				B[m] = ((long double)b[l1] + b[l2]) / 2.0;
				C[m] = ((long double)c[l1] + c[l2]) / 2.0;
				m++;

				A[m] = ((long double)a[l1] * d[l2] + (long double)a[l2] * d[l1]) / ((long double)d[l1] + (long double)d[l2]);
				B[m] = ((long double)b[l1] * d[l2] + (long double)b[l2] * d[l1]) / ((long double)d[l1] + (long double)d[l2]);
				C[m] = ((long double)c[l1] * d[l2] + (long double)c[l2] * d[l1]) / ((long double)d[l1] + (long double)d[l2]);
				m++;

				A[m] = ((long double)a[l1] * d[l1] + (long double)a[l2] * d[l1]) / ((long double)d[l1] + (long double)d[l2]);
				B[m] = ((long double)b[l1] * d[l1] + (long double)b[l2] * d[l2]) / ((long double)d[l1] + (long double)d[l2]);
				C[m] = ((long double)c[l1] * d[l1] + (long double)c[l2] * d[l2]) / ((long double)d[l1] + (long double)d[l2]);
				m++;
			}
		}

		ret = 1e100;
		for(l1=0;l1<m;l1++) for(l2=0;l2<m;l2++) for(l3=0;l3<m;l3++) Go(A[l1],B[l2],C[l3]);

		printf("Case #%d: %.7Lf\n",l0,ret);
	}
}