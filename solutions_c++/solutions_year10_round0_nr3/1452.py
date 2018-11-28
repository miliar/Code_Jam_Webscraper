#include <stdio.h>

#define MAX 1100

int tam[MAX];
int prox[MAX];
long long int soma[MAX];

int main()
{
	int i,j;
	int r,k,n;
	int ncases,ccnt;
	long long int resp;
	long long int ac;
	scanf("%d",&ncases);
	for(ccnt=1;ccnt<=ncases;++ccnt)
	{
		scanf("%d %d %d",&r,&k,&n);
		for(i=0;i<n;++i)
			scanf("%d",&tam[i]);
		for(i=0;i<n;++i)
		{
			prox[i]=(i+n-1)%n;
			ac=tam[i];
			for(j=(i+1)%n;j!=i;j=(j+1)%n)
			{
				if(ac+tam[j]>k)
				{
					prox[i]=j;
					soma[i]=ac;
					break;
				}
				ac+=tam[j];
			}
			if(j==i)
			{
				prox[i]=i;
				soma[i]=ac;
			}
		}

		j=0;
		resp=0;
		for(i=0;i<r;++i)
		{
			resp+=soma[j];
			j=prox[j];
		}
		printf("Case #%d: %lld\n",ccnt,resp);
	}
	return 0;
}






