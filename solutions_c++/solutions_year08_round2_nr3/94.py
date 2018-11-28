#include <stdio.h>
#include <stdlib.h>

int xx[1000000];

struct x
{
	struct x * p;
	struct x * n;
	int c;
};

int main()
{
	int ii,n,nn,k,j,i;
	struct x * a;
	struct x * b;
	scanf("%d",&n);
	for (ii=0;ii<n;++ii)
	{
		scanf("%d",&k);
		a=(struct x*)malloc(sizeof(struct x));
		a->p=a;
		a->n=a;
		a->c=k;
		nn=1;
		j=k;
		while (j>1)
		{
			for (i=0;i<((j-1)%nn);++i)
			{
				a=a->p;
			}
			b=(struct x*)malloc(sizeof(struct x));
			--j;
			b->n=a;
			b->c=j;
			b->p=a->p;
			a->p=b;
			b->p->n=b;
			a=b;
			++nn;
		}
		for (i=0;i<k;++i)
		{
			xx[i]=a->c;
			b=a;
			a=a->n;
			free(b);
		}
		scanf("%d",&nn);
		printf("Case #%d: ",ii+1);
		for (i=0;i<nn;++i)
		{
			scanf("%d",&j);
			printf("%d ",xx[j-1]);
		}
		printf("\n");
	}
	return 0;
}
