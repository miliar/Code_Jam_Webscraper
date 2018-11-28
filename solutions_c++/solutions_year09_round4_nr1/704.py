#include <windows.h>
#include <stdio.h>
#include <stdlib.h>

#pragma warning(disable:4101)

#define OUTPUT_TO_FILE 1
#define INPUT_FILE 2

#if (INPUT_FILE==0)
#define FILENAME "sample"
#elif (INPUT_FILE==1)
#define FILENAME "A-small-attempt0"
#else
#define FILENAME "A-large"
#endif

#define FULLNAME(x) FILENAME##x

#define INFILE FULLNAME(".in")
#define OUTFILE FULLNAME(".out")

#define FIN(arg,...) fscanf_s(fin, arg##"\n", __VA_ARGS__)

#define CASE printf("Case #%d: \n", i+1); fprintf(fout, "Case #%d: ", i+1)

#if (OUTPUT_TO_FILE==1)
#define FOUT(arg,...) fprintf(fout, arg##"\n", __VA_ARGS__)
#else
#define FOUT(arg,...) printf(arg##"\n", __VA_ARGS__)
#endif

template<class T>
void mov(T &a, void *b)
{
	a = (T)b;
}

#define ALLOC_ZERO(name,size) mov(name,malloc(size)); ZeroMemory(name,size);
#define CREATE_ZERO(type, name, size) type *name = new type[size]; ZeroMemory(name, sizeof(type)*size);
#define ZERO(name) ZeroMemory(name, sizeof(name));
#define FOR_0_N(var, N) for (var = 0;var<N;++var)

FILE *fin,*fout;

int data[100];
bool cool[100];

void swap(int &a, int &b)
{
	int c;
	c=a;
	a=b;
	b=c;
}

int check(int n)
{
	int res=0;
	for (int i=0;i<n;++i)
	{
		cool[i] = (data[i]<=i);
		if (!cool[i])
			++res;
	}
	return res;
}

int solve(int n)
{
	int i,j,x,r=0;
	x = check(n);
	while (x>0)
	{
		for (i=0;i<n;++i)
		{
			if (!cool[i])
				break;
		}
		for (j=i+1;j<n;++j)
		{
			if (data[j]<=i)
				break;
		}
		swap(data[j-1], data[j]);
		++r;
		x= check(n);
	}
	return r;
}

void main()
{
	int N=0;
	int i=0,j=0,k=0;
	fopen_s(&fin,INFILE, "rt");
	fopen_s(&fout,OUTFILE, "wt");
	FIN("%d", &N);
	FOR_0_N(i,N)
	{
		CASE;
		int n;
		char line[100];
		FIN("%d", &n);
		FOR_0_N(j,n)
		{
			FIN("%s",line,100);
			int x=0;
			FOR_0_N(k,n)
			{
				if (line[k]=='1')
					x=k;
			}
			data[j]=x;
		}
		FOUT("%d", solve(n));
	}
	fclose(fout);
	fclose(fin);
}