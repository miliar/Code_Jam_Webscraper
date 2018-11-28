#include "stdio.h"
#include "stdlib.h"
#include "memory.h"
#include "string.h"
#include "math.h"

FILE *fin, *fout;

#define INPUT_FILE_NAME "C-large"
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
	int N,D;
	int high[2000];
	__int64 l[2000];
	__int64 i,j;
	__int64 s;
	fscanf_s(fin, "%d", &N);
	for (i=0;i<N-1;++i)
	{
		fscanf_s(fin, "%d", &high[i]);
		--high[i];
	}
	for (i=0;i<N-1;++i)
	{
		for (j=i+1;j<high[i];++j)
		{
			if (high[j]>high[i])
			{
				print("Impossible");
				return;
			}
		}
	}
	for (i=0;i<N;++i)
	{
		l[i] = 1000000000;
	}
	bool bChange = true;
	while (bChange)
	{
		bChange = false;
		for (i=0;i<N;++i)
		{
			if (i<N-1)
			{
				for (j=high[i]+1;j<N;++j)
				{
					s = l[j]+(double)(l[high[i]]-l[j])*(double)(j-i)/(double)(j-high[i]);
					if (l[i]>=s)
					{
						l[i] = s-1;
						bChange = true;
					}
				}
			}
			for (j=i+1;j<high[i];++j)
			{
				s = l[i]+(double)(l[high[i]]-l[i])*(double)(j-i)/(double)(high[i]-i);
				if (l[j]>=s)
				{
					l[j] = s-1;
					bChange = true;
				}
			}
		}
	}
	for (i=0;i<N;++i)
		print("%lld ", l[i]);
}