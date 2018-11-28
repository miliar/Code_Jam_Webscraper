#include <stdio.h>
#include <string.h>

int N,M;
char s[10000];
char s2[10000];

int u[100];
int p[100];

int go(int h,int n)
{
	int i,j;
	if (h==n)
	{
		for (i=0;i<N/n;++i)
			for (j=0;j<n;++j)
		{
			s2[i*n+j]=s[i*n+p[j]];
		}
		s2[N]=0;
		j=0;
		for (i=0;i<N-1;++i) if (s2[i]!=s2[i+1]) ++j;
		if (j+1<M) M=j+1;
		return 0;
	}
	for (i=0;i<n;++i)
	{
		if (u[i]==0)
		{
			p[h]=i;
			u[i]=1;
			go(h+1,n);
			u[i]=0;
		}
	}
	return 0;
}

int main()
{
	int nn,ii,k;
	scanf("%d\n",&nn);
	for (ii=0;ii<nn;++ii)
	{
		scanf("%d %s",&k,s);
		N=strlen(s);
		M=N;
		go(0,k);
		printf("Case #%d: %d\n",ii+1,M);
	}
	return 0;
}
