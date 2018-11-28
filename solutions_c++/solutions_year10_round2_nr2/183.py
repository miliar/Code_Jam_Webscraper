#include <stdio.h>
#include <memory.h>
#define eps 1e-8

typedef long long I;

int N,K,B,T,X[60],V[60];
double t[60];

int main()
{
	int TT,C=0,N,K,B,T;
	int i,c,k,s;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&TT);
	while(TT--)
	{
		printf("Case #%d: ",++C);
		scanf("%d %d %d %d",&N,&K,&B,&T);
		c=k=s=0;
		for(i=1;i<=N;i++)scanf("%d",&X[i]);
		for(i=1;i<=N;i++)scanf("%d",&V[i]);
		for(i=1;i<=N;i++)t[i]=(double)(B-X[i])/V[i];
		for(i=N;i>=1;i--)
		{
			if(t[i]<T+eps)
			{
				k++;
				s+=c;
				if(k==K)break;
			}
			else
			{
				c++;
			}
		}
		if(k==K)printf("%d\n",s);
		else puts("IMPOSSIBLE");
	}
	return 0;
}