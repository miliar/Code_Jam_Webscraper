#include<stdio.h>

#define Swap(aa,bb) {cc=aa;aa=bb;bb=cc;}
int cc;

int a[1111], n;
int A, B;
int T;

int main(void)
{
	int l1, l2, l3, l0;

	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	scanf("%d",&T);

	for(l0=1;l0<=T;l0++)
	{
		scanf("%d %d %d",&A,&B,&n);
		for(l1=0;l1<n;l1++) scanf("%d",&a[l1]);
		for(l1=0;l1<n;l1++) for(l2=l1+1;l2<n;l2++) if(a[l1] < a[l2]) Swap(a[l1], a[l2]);

		long long ret = 0;
		for(l1=0;l1<n;l1++)
		{
			ret += (long long)a[l1] * (long long)(l1 / B + 1);
		}

		printf("Case #%d: %I64d\n",l0,ret);
	}

	return 0;
}