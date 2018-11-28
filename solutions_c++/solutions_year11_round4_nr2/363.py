#include "stdio.h"
#include "stdlib.h"
#include "memory.h"
#include "string.h"

FILE *fin, *fout;

#define INPUT_FILE_NAME "B-large"
#define INPUT_FILE INPUT_FILE_NAME##".in"
#define OUTPUT_FILE INPUT_FILE_NAME##".out"

#define print(format,...) {fprintf(fout, format, __VA_ARGS__); printf(format, __VA_ARGS__);}

#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))

void problem(int nCase);

void main(int argc, char **argv)
{
	int N,k;
	printf("%s\n", INPUT_FILE);
	fopen_s(&fin, INPUT_FILE, "rt");
	fopen_s(&fout, OUTPUT_FILE, "wt");
	fscanf_s(fin, "%d", &N);
	k=0;
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

void problem(int nCase)
{
	int r,c,d;
	fscanf_s(fin, "%d %d %d", &r, &c, &d);
	int i,j,k,x,y;
	int weightH, weightV;
	int maxBlade = 0;
	int grid[500][500];
	char line[600];
	for (i=0;i<r;++i)
	{
		fscanf_s(fin, "%s", line, 600);
		for (j=0;j<c;++j)
		{
			grid[i][j] = line[j]-'0';
		}
	}
	if (nCase!=16)
		return;
	for (k=20;k>=3 && maxBlade==0;--k)
	{
		for (x=0;x<=r-k && maxBlade==0;++x)
		{
			for (y=0;y<=c-k && maxBlade==0;++y)
			{
				weightH = weightV = 0;
				for (i=0;i<k;++i)
				{
					for (j=0;j<k;++j)
					{
						if ((i>0 && i<k-1) || (j>0 && j<k-1))
						{
							weightH += (i*2-(k-1))*grid[x+i][y+j];
							weightV += (j*2-(k-1))*grid[x+i][y+j];
						}
					}
				}
				if (weightH == 0 && weightV == 0)
				{
					maxBlade = k;
				}
			}
		}
	}
	if (maxBlade)
	{
		print("%d",maxBlade)
	}
	else
	{
		print("IMPOSSIBLE");
	}
}