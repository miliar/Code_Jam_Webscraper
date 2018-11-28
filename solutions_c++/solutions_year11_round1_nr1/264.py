#include "stdio.h"
#include "stdlib.h"
#include "memory.h"

#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define abs(x) ((x)>(0)?(x):-(x))


bool possible(__int64 N, __int64 Pd, __int64 Pg)
{
	if (Pg == 100 && Pd<100)
		return false;
	if (Pg == 0 && Pd>0)
		return false;
	int i;
	for (i=1;i<=N && i<=100;++i)
	{
		if (((Pd*i)%100)==0)
		{
			return true;
		}
	}
	return false;
}

void main(int argc, char **argv)
{
	FILE *f;
	int n,k;
	__int64 N,Pd,Pg;
	fopen_s(&f, argv[1], "rb");
	fscanf_s(f, "%d", &n);
	for (k=1;k<=n;++k)
	{
		printf("Case #%d: ",k);
		fscanf_s(f, "%lld %lld %lld", &N, &Pd, &Pg);
		if (possible(N, Pd, Pg))
		{
			printf("Possible");
		}
		else
		{
			printf("Broken");
		}
		printf("\n");
	}
	fclose(f);
}