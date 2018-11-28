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

typedef struct  
{
	__int64 d,l;
	__int64 maxd;
}SVine;

void problem(int nCase)
{
	int N,D;
	SVine vine[10000];
	int i,j;
	__int64 dist;
	fscanf_s(fin, "%d", &N);
	memset(vine,0, sizeof(vine));
	for (i=0;i<N;++i)
	{
		fscanf_s(fin, "%d %d", &vine[i].d, &vine[i].l);
	}
	fscanf_s(fin, "%d", &D);
	bool bChange=true;
	vine[0].maxd = vine[0].d;
	if (vine[0].maxd+vine[0].d>=D)
	{
		print("YES");
		return;
	}
	while (bChange)
	{
		bChange = false;
		for (i=0;i<N;++i)
		{
			if (vine[i].maxd>0)
			{
				for (j=0;j<N;++j)
				{
					dist = abs(vine[j].d-vine[i].d);
					if (dist <= vine[i].maxd && vine[j].l>vine[j].maxd)
					{
						if (vine[j].maxd<dist)
						{
							vine[j].maxd = min(dist, vine[j].l);
							bChange = true;
							if (vine[j].maxd+vine[j].d>=D)
							{
								print("YES");
								return;
							}
						}
					}
				}
			}
		}
	}
	print("NO");
}