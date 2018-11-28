#include <cstdio>
#include <cstring>

using namespace std;

#define MAXSIZE 50000
#define MAXK 16

char S[MAXSIZE+1];
int perm[MAXK+2];

bool verify(int p,int k)
{
	for (int i=1;i<p;i++)
	{
		if (perm[i] == perm[p]) return false;
	}
	return true;
}

int min = MAXSIZE + 1;

void execute(int k)
{
	char SAUX[MAXSIZE+1];
	SAUX[strlen(S)]=0;
	for (int i=0;i<strlen(S);i++)
	{
		SAUX[i] = S[i/k * k + perm[i%k+1]-1];
	}
	char c = SAUX[0];
	int count = 1;
	for (int i=1;i<strlen(SAUX);i++)
	{
		if (SAUX[i] != c)
		{
			++count;
			c = SAUX[i];
		}
	}
	if (count < min) min = count;
}


void genperm(int p, int k)
{
	if (p == k+1) {execute(k);return;}
	if (p<1) return;
	do
	{
		bool ver = false;
		do
		{
			perm[p]+=1;
			ver = verify(p,k);
		}while (perm[p]<=k && !ver);
		if (perm[p] <= k) {perm[p+1]=0; genperm(p+1,k);}
		else break;
	}while (true);
}



int main()
{
	
	int N;
	scanf("%d",&N);
	for (int i=1;i<=N;i++)
	{
		int k;
		scanf("%d",&k);
		scanf("%s",S);
		min = MAXSIZE + 1;
		perm[1]=0;
		genperm(1,k);
		printf("Case #%d: %d\n",i,min);
	}
	return 0;
	

}