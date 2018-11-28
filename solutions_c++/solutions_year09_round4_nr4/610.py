#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#pragma warning(disable:4101)

#define OUTPUT_TO_FILE 1
#define INPUT_FILE 1

#if (INPUT_FILE==0)
#define FILENAME "sample"
#elif (INPUT_FILE==1)
#define FILENAME "D-small-attempt2"
#else
#define FILENAME "sample"
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

FILE*fin,*fout;

typedef struct 
{
	int x,y,r;
}SPlant;

#define SQR(a) ((a)*(a))

double vzd(SPlant *a, SPlant *b)
{
	return (sqrt((double)(SQR(a->x-b->x)+SQR(a->y-b->y)))+(double)a->r+(double)b->r)/2;
}

#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))

void main()
{
	int N=0;
	int i=0,j=0,k=0;
	fopen_s(&fin,INFILE, "rt");
	fopen_s(&fout,OUTFILE, "wt");
	FIN("%d", &N);
	SPlant p[3];
	FOR_0_N(i,N)
	{
		CASE;
		int n;
		FIN("%d", &n);
		for (j=0;j<n;++j)
		{
			FIN("%d %d %d", &p[j].x, &p[j].y, &p[j].r);
		}
		double res = 0;
		if (n==1)
		{
			res = p[0].r;
		}
		if (n==2)
		{
			res = max(p[0].r, p[1].r);
		}
		if (n==3)
		{
			double v01 = max(vzd(&p[0], &p[1]),(double)p[2].r);
			double v02 = max(vzd(&p[0], &p[2]),(double)p[1].r);
			double v12 = max(vzd(&p[1], &p[2]),(double)p[0].r);
			res = min(v01,min(v02,v12));
		}
		FOUT("%.8f",res);
	}
	fclose(fout);
	fclose(fin);
}