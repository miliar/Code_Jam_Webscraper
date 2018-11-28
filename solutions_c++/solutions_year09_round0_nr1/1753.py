#include <cstdio>
#include <string.h>
#include <stdlib.h>

using namespace std;

#define max(x,a) ((x)>(a)?(x):(a))
#define min(x,a) ((x)<(a)?(x):(a))

int L,D,N;

char Dic[5000][16];
char Ma[5000];

void Nul()
{
	memset(Ma,1,D);
}

char* Lett(int n,char *S)
{
	char *e;
	if(*S=='(')
	{
		S++;
		e=strchr(S,')');
		*e=0;
		for(int i=0;i<D;i++)
		{
			if(!strchr(S,Dic[i][n])) Ma[i]=0;
		}
		S=e;
	}
	else
	{
		for(int i=0;i<D;i++)
		{
			if(*S!=Dic[i][n]) Ma[i]=0;
		}
	}
	S++;
	return S;
}

int Count()
{
	int S=0;
	for(int i=0;i<D;i++)
	{
		if(Ma[i]) S++;
	}
	return S;
}


int main()
{
	long i,j;

	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	char S[10000];
	scanf("%d%d%d",&L,&D,&N);
	
	for(i=0;i<D;i++)
	{
		scanf("%s",Dic[i]);
	}

	char *l;
	for(i=0;i<N;i++)
	{
		scanf("%s",S);
		Nul();
		l=S;
		for(j=0;j<L;j++)
		{
			l=Lett(j,l);
		}
		printf("Case #%d: %d\n",i+1,Count());
	}
	return 0;
}
