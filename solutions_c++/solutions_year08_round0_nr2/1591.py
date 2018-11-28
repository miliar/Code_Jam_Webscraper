#include<stdio.h>

#define NMAX 100
#define MMAX 5001

int T,N[NMAX];
__int64 Data[NMAX][MMAX];

__int64 Sum[NMAX];

void Input()
{
	int i,j;
	FILE *in=fopen("a2.in","r");
	fscanf(in,"%d\n\n",&T);
	for(i=0;i<T;i++)
	{
		fscanf(in,"%d\n",&N[i]);
		for(j=0;j<N[i];j++)
		{
			fscanf(in,"%I64d\n",&Data[i][j]);
			Data[i][j]%=N[i];
		}
		fscanf(in,"\n");
	}
	fclose(in);
}

void Process()
{
	int i,j;
	for(i=0;i<T;i++)
	{
		for(j=0;j<N[i];j++)
			Sum[i]+=Data[i][j];
	}
}

void Output()
{
	int i;
	int Temp;
	FILE *out=fopen("a2.out","w");
	for(i=0;i<T;i++)
	{
		Temp=Sum[i]%(__int64)N[i];
		if(Temp==0)
			fprintf(out,"YES\n");
		else
			fprintf(out,"NO\n");
	}
	fclose(out);
}

int main()
{
	Input();
	Process();
	Output();
	return 0;
}
