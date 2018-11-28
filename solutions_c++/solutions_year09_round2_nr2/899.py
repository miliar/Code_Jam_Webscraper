#include <stdio.h>
#include <string.h>
#include <cstdlib>
#include <memory.h>

using namespace std;

#define max(x,a) ((x)>(a)?(x):(a))
#define min(x,a) ((x)<(a)?(x):(a))

void exch(int &a,int &b)
{
	int t=b;
	b=a;a=t;
}


int N[30],NL;

void Min(int a,int b)
{
	int i,j;
		for(i=a;i<=b;i++)
		{
			for(j=a+1;j<=b;j++)
			{
				if(N[j-1]<N[j]) exch(N[j-1],N[j]);
			}
		}
}

void Next()
{
	int i,j;
	int D[11];
	int I[11];
	memset(D,0,sizeof(D));

	for(i=0;i<NL;i++)
	{
		j=1;
		while(D[N[i]+j]==0 && (N[i]+j)<10 ) j++;
		if(D[N[i]+j])
		{
			exch(N[i],N[I[N[i]+j]]);
			Min(0,i-1);
			return;
		}
		else
		{
			D[N[i]]++;
			I[N[i]]=i;
		}
	}
	/////// biggest, NL -> NL+1

	Min(0,NL-1);
	N[NL]=0;
	i=NL-1;
	while(N[i]==0) i--;
	exch(N[i],N[NL]);
	NL++;
}


int main()
{
	long i,j,T;

	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	char S[10000];
	scanf("%ld",&T);
	
	for(i=0;i<T;i++)
	{
		scanf("%s",S);
		NL=strlen(S);
		for(j=0;j<NL;j++)
			N[j]=S[NL-j-1]-'0';

		Next();
		for(j=0;j<NL;j++)
			S[NL-j-1]=N[j]+'0';
		S[NL]=0;
		printf("Case #%d: %s\n",i+1,S);
	}
	return 0;
}
