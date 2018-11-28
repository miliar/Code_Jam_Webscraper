#include "stdio.h"
#include "stdlib.h"
#include "memory.h"
#include "string.h"
#include "math.h"

FILE *fin, *fout;

#define INPUT_FILE_NAME "A-large"
#define INPUT_FILE INPUT_FILE_NAME##".in"
#define OUTPUT_FILE INPUT_FILE_NAME##".out"

#define print(format,...) {fprintf(fout, format, __VA_ARGS__); printf(format, __VA_ARGS__);}

#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define pow2(a) ((a)*(a))

template<class T>
inline void swap(T &a, T &b)
{
	T c;
	c=a;
	a=b;
	b=c;
}

void problem(int nCase);
void init();

void main(int argc, char **argv)
{
	int N,k;
	printf("%s\n", INPUT_FILE);
	fopen_s(&fin, INPUT_FILE, "rt");
	fopen_s(&fout, OUTPUT_FILE, "wt");
	fscanf_s(fin, "%d\n", &N);
	k=0;
	init();
	while(N--)
	{
		++k;
		print("Case #%d: ", k);
		problem(k);
		print("\n");
	}
	fclose(fin);
	fclose(fout);
}

void init()
{
}

void problem(int nCase)
{
	int i,j,k;
	int a,b,c;
	int P[1000];
	int L[1000];
	int index[1000];
	int N;
	fscanf_s(fin, "%d", &N);
	for (i=0;i<N;++i)
	{
		fscanf_s(fin, "%d", &L[i]);
		index[i] = i;
	}
	for (i=0;i<N;++i)
	{
		fscanf_s(fin, "%d", &P[i]);
	}
	for (i=0;i<N;++i)
	{
		for (j=0;j<N-i-1;++j)
		{
			if (L[j]*P[j+1]>L[j+1]*P[j])
			{
				swap(L[j+1], L[j]);
				swap(P[j+1], P[j]);
				swap(index[j+1], index[j]);
			}
		}
	}
	for (i=0;i<N;++i)
	{
		print("%d ", index[i]);
	}
}