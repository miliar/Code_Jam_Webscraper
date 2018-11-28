#include<stdio.h>

#define MOD 1000000007

int n, m, X, Y, Z;

int a[100], b[1111];
long long D[1111];

int main(void)
{
	int T;
	int l0, l1, l2, l3;

	freopen("small.in","r",stdin);
	freopen("small.out","w",stdout);

	scanf("%d",&T);
	for(l0=1;l0<=T;l0++)
	{
		scanf("%d %d %d %d %d",&n,&m,&X,&Y,&Z);
		for(l1=0;l1<m;l1++)
		{
			scanf("%d",&a[l1]);
		}

		for(l1=0;l1<n;l1++)
		{
			b[l1] = a[l1 % m];
			a[l1 % m] = ((long long)X * a[l1 % m] + (long long)Y * (l1 + 1)) % (long long)Z;
		}

		long long ret = 0;
		for(l1=0;l1<n;l1++)
		{
			D[l1] = 1;
			for(l2=0;l2<l1;l2++)
			{
				if(b[l2] < b[l1])
				{
					D[l1] += D[l2];
				}
			}
			ret += D[l1];

			D[l1] %= MOD;
			ret %= MOD;
		}

		printf("Case #%d: %I64d\n",l0,ret);
	}

	return 0;
}