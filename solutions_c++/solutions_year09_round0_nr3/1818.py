#include <cstdio>
#include <string.h>
#include <stdlib.h>

using namespace std;

#define max(x,a) ((x)>(a)?(x):(a))
#define min(x,a) ((x)<(a)?(x):(a))

int L;

char Key[20]="welcome to code jam";
long N[19];

void Lett(char S)
{
	for(int i=18;i>=0;i--)
	{
		if(Key[i]==S)
			N[i]+=N[i-1];
		N[i]%=10000;
	}
	if(Key[0]==S)
		N[0]++;
	N[0]%=10000;
}

void Nul()
{
	memset(N,0,19*4);
}

int main()
{
	long i,j,Q;

	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	char S[10000];
	scanf("%d",&Q);
	gets(S);

	char *l;
	for(i=0;i<Q;i++)
	{
		gets(S);
		Nul();
		j=0;
		while(S[j])
		{
			Lett(S[j]);
			j++;
		}
		printf("Case #%d:",i+1);
		sprintf(S,"%ld\n",N[18]+10000);
		S[0]=' ';
		printf("%s",S);
	}
	return 0;
}
