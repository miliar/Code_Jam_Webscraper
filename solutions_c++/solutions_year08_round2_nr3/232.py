#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

#define MAX 1000010L

struct nodo
{
	int s;
};

int main()
{
	int q,Q;
	int sol,a,b,n,m,p,c,c1;
	int *mapa;
	struct nodo *cad;

	mapa=(int *)malloc(sizeof(int)*MAX);
	cad=(struct nodo *)malloc(sizeof(struct nodo)*MAX);

	scanf(" %d",&Q);
	for(q=1;q<=Q;q++)
	{
		scanf(" %d %d",&n,&m);


		for(a=1;a<=n;a++)
			cad[a].s=a+1;
		cad[n].s=1;

		for(c=n,c1=n-1,a=1;a<=n;a++)
		{
			for(b=0;b<a;b++)
			{
				c1=c;
				c=cad[c].s;
			}
			mapa[c]=a;
			cad[c1].s=cad[c].s;
			c=c1;
		}

		printf("Case #%d:",q);
		for(a=0;a<m;a++)
		{
			scanf(" %d",&p);
			printf(" %d",mapa[p]);
		}
		printf("\n");
	}

	return(0);
}

