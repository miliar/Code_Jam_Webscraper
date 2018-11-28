#include<stdio.h>

FILE *f = fopen("dancing.in","r");
FILE *g = fopen("dancing.out","w");

#define MaxN 130

int T,N,S,P,A[MaxN];

void citire(void)
{
	fscanf(f,"%d %d %d",&N,&S,&P);
	for(int i=1;i<=N;i++)
		fscanf(f,"%d ",&A[i]);
}

inline int min(int a,int b)
{
	return a < b ? a : b;
}

inline int Rezolvare(void)
{
	int Sol = 0,SolP = 0;
	for(int i=1;i<=N;i++)
		if(A[i]%3 == 0)
		{
			if(A[i]/3 >= P)
				Sol ++;
			else if(A[i]/3+1 >= P && A[i])
				SolP ++;
		}
		else if(A[i]%3 == 1)
		{
			if(A[i]/3+1 >= P)
				Sol ++;
		}
		else
		{
			if(A[i]/3+1 >= P)
				Sol ++;
			else if(A[i]/3+2 >= P)
				SolP ++;
		}
		
	return Sol + min(SolP,S);
}

int main()
{
	fscanf(f,"%d\n",&T);
	for(int i=1;i<=T;i++)
	{
		citire();
		fprintf(g,"Case #%d: %d\n",i,Rezolvare());
	}
}