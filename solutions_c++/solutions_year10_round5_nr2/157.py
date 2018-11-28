#include<stdio.h>

const int SAFE = 10000000;
#define Swap(aa,bb) {cc=aa;aa=bb;bb=cc;}
int cc;

int D[SAFE + 1];
long long X;
int n;
int a[100];

int main(void)
{
	int T;
	int l1, l2, l0;
	
	long long ret;

	freopen("B1.in","r",stdin);
	freopen("B1.out","w",stdout);

	scanf("%d",&T);

	for(l0=1;l0<=T;l0++)
	{
		fprintf(stderr,"%d %d\n",l0,T);
		scanf("%I64d %d",&X,&n);
		ret = X+1;
		for(l1=0;l1<n;l1++) scanf("%d",&a[l1]);

		for(l1=0;l1<n;l1++) for(l2=l1+1;l2<n;l2++) if(a[l1] > a[l2]) Swap(a[l1], a[l2]);

		for(l1=1;l1<=SAFE;l1++)
		{
			D[l1] = -1;
			for(l2=0;l2<n;l2++)
			{
				if(a[l2] > l1) break;
				if(D[l1 - a[l2]] != -1)
				{
					if(D[l1] == -1 || D[l1] > D[l1-a[l2]]+1)
					{
						D[l1] = D[l1-a[l2]]+1;
					}
				}
			}

			if(D[l1] == -1) continue;
			if((X - (long long)l1) % (long long)a[n-1] == 0)
			{
				long long curr = (X - l1) / a[n-1] + D[l1];
				if(curr < ret) ret = curr;
			}
		}

		if(ret == X + 1)
		{
			printf("Case #%d: IMPOSSIBLE\n",l0);
		}
		else
		{
			printf("Case #%d: %I64d\n",l0,ret);
		}
	}

	return 0;
}