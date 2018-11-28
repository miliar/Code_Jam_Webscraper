#include <stdio.h>
#include<stdlib.h>
#include<time.h>

int T,C,D;

int loc[500];
int count[500];
int sumcount[500];

int mdist(int low, int high)
{
	int phobia = loc[high] - loc[low];
	int tot = sumcount[high] - sumcount[low] + count[low];

	return (tot - 1) * D - phobia;
}

int main()
{
	FILE *fin=fopen("input.txt","r");
	FILE *fout = fopen("output.txt","w");

	fscanf(fin, "%d", &T);
	for(int aaa=1; aaa<=T; aaa++)
	{
		fscanf(fin, "%d%d", &C, &D);

		for(int i = 0; i < C; i++)
		{
			fscanf(fin, "%d%d", loc + i, count + i);
			if(i>0) sumcount[i] = sumcount[i-1] + count[i];
			else sumcount[i] = count[i];
		}

		int result=0;
		for(int i = 0; i < C; i++)
		{
			for(int j = i; j < C; j++)
			{
				int c = mdist(i,j);
				if(result < c) result = c;
			}
		}

		fprintf(fout,"Case #%d: %f\n", aaa, result / 2.0);
	}

	return 0;
}
