#include <stdio.h>

#define REP(i, n) for(i=0; i < n ; i++)

using namespace std;

int main()
{
	int T, N, i, j;
	FILE *iFile, *oFile;
	iFile = fopen("C-large.in", "r+");
	oFile = fopen("output.out", "w+");
	fscanf(iFile, "%d", &T);
	REP(i, T)
	{
		fscanf(iFile, "%d", &N);
		long a[N];
		REP(j, N)
		{
			int temp;
			fscanf(iFile, "%d", &temp);
			a[j] = temp;
		}
		for(int x=0; x < N; x++)
		{
			for(int y=x+1; y < N; y++)
			{
				if(a[x] < a[y])
				{
					int temp = a[x];
					a[x] = a[y];
					a[y] = temp;
				}
			}
		}
		int max = -1;
		for(j = 0; j < N-1; j++)
		{
			long xsum1=0, xsum2=0, sum1=0, sum2=0;
			int k;
			for(k=0; k <= j; k++)
			{
				xsum1 = xsum1^a[k];
				sum1 += a[k];
			}
			for(k = j+1; k < N; k++)
			{
				xsum2 = xsum2^a[k];
				sum2 += a[k];
			}
			if(xsum1 != xsum2)
				continue;
			if(sum1 > max)
				max = sum1;
			if(sum2 > max)
				max = sum2;
		}
		fprintf(oFile, "Case #%d: ", i+1);
		if(max != -1)
			fprintf(oFile, "%d\n", max);
		else
			fprintf(oFile, "NO\n"); 
	}
	return 0;  
}