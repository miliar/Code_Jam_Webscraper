#include<stdio.h>

int D, n, T;
int lim[5]={1,10,100,1000,10000};
int a[111];
int P[10000];
int pn;
int MOD;
int A, B;

int main(void)
{
	int l0, l1, l2, l3;

	freopen("A1.in","r",stdin);
	freopen("A1.out","w",stdout);

	P[0] = 2;
	pn = 1;
	for(l1=3;l1<=10000;l1+=2)
	{
		for(l2=0;l2<pn&&P[l2]*P[l2]<=l1;l2++)
		{
			if(l1 % P[l2] == 0) goto maki;
		}
		P[pn] = l1;
		pn++;
maki: ;
	}

	scanf("%d",&T);
	for(l0=1;l0<=T;l0++)
	{
		scanf("%d %d",&D,&n);
		for(l1=0;l1<n;l1++) scanf("%d",&a[l1]);

		if(n == 1)
		{
			printf("Case #%d: I don\'t know.\n",l0);
			continue;
		}

		int ret = -1;
		for(l1=0;l1<pn;l1++)
		{
			MOD = P[l1];
			if(MOD > lim[D]) break;
			for(l2=0;l2<n;l2++) if(a[l2] >= MOD) break;
			if(l2 < n) continue;

			for(A=0;A<MOD;A++)
			{
				B = (a[1] - ((a[0] * A) % MOD) + MOD) % MOD;
				
				for(l2=1;l2<n;l2++)
				{
					if(a[l2] != (a[l2-1] * A + B) % MOD) break;
				}
				if(l2 == n)
				{
					if(ret == -1)
					{
						ret = (a[n-1] * A + B) % MOD;
					}
					else if(ret != (a[n-1] * A + B) % MOD)
					{
						ret = -1;
						break;
					}
				}
			}
			if(A < MOD) break;
		}
		if(ret == -1)
		{
			printf("Case #%d: I don\'t know.\n",l0);
			continue;
		}
		else
		{
			printf("Case #%d: %d\n",l0,ret);
		}
	}
}