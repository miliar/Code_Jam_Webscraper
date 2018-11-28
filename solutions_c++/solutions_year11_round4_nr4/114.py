#include "stdio.h"
#include "stdlib.h"
#include "memory.h"
#include "string.h"

FILE *fin, *fout;

#define INPUT_FILE_NAME "D-small-attempt0"
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

typedef struct 
{
	int x,y;
}SWormhole;

int planets[400];
SWormhole worms[2000];
int p,w;

int nThreaten[400];
int nThreatened=0;
int nMaxThreat=0;

void maxThreaten(int planetP)
{
	int i;
	int maxthreat=0;
	if (planetP!=1)
	{
		for (i=0;i<w;++i)
		{
			if (worms[i].x==planetP)
			{
				if (nThreaten[worms[i].y]==0)
					++nThreatened;
				++nThreaten[worms[i].y];
			}
			if (worms[i].y==planetP)
			{
				if (nThreaten[worms[i].x]==0)
					++nThreatened;
				++nThreaten[worms[i].x];
			}
		}
	}
	if (planetP==0)
	{
		nMaxThreat = max(nMaxThreat, nThreatened);
	}
	for (i=0;i<w;++i)
	{
		if (worms[i].x == planetP && planets[worms[i].y]+1 == planets[planetP])
		{
			maxThreaten(worms[i].y);
		}
		if (worms[i].y == planetP && planets[worms[i].x]+1 == planets[planetP])
		{
			maxThreaten(worms[i].x);
		}
	}
	if (planetP!=1)
	{
		for (i=0;i<w;++i)
		{
			if (worms[i].x==planetP)
			{
				--nThreaten[worms[i].y];
				if (nThreaten[worms[i].y]==0)
					--nThreatened;
			}
			if (worms[i].y==planetP)
			{
				--nThreaten[worms[i].x];
				if (nThreaten[worms[i].x]==0)
					--nThreatened;
			}
		}
	}
}

void problem(int nCase)
{
	int i;
	nMaxThreat=0;
	fscanf_s(fin, "%d %d", &p, &w);
	for (i=0;i<w;++i)
	{
		fscanf_s(fin, "%d,%d", &worms[i].x, &worms[i].y);
	}
	memset(planets, 0 ,sizeof(planets));
	memset(nThreaten, 0 ,sizeof(nThreaten));
	planets[0] = 1;
	bool bDone = false;
	while (!bDone)
	{
		bDone = true;
		for (i=0;i<w;++i)
		{
			if (planets[worms[i].x]>0)
			{
				if (planets[worms[i].y]==0 || planets[worms[i].y]>planets[worms[i].x]+1)
				{
					planets[worms[i].y] = planets[worms[i].x]+1;
					bDone = false;
				}
			}
			if (planets[worms[i].y]>0)
			{
				if (planets[worms[i].x]==0 || planets[worms[i].x]>planets[worms[i].y]+1)
				{
					planets[worms[i].x] = planets[worms[i].y]+1;
					bDone = false;
				}
			}
		}
	}
	maxThreaten(1);
	int own = planets[1]-2;
	if (own>0)
		nMaxThreat -= own+1;
	print("%d %d",own, nMaxThreat);
}