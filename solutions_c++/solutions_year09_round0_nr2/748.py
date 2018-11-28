#include "stdio.h"
#include "stdlib.h"
#include "string.h"

#define min(a,b) ((a)<(b)?(a):(b))

bool isSink(int **grid, int h, int w, int y, int x)
{
	bool bRes = true;
	if (x>0)
		bRes &= grid[y][x] <= grid[y][x-1];
	if (y>0)
		bRes &= grid[y][x] <= grid[y-1][x];
	if (x<w-1)
		bRes &= grid[y][x] <= grid[y][x+1];
	if (y<h-1)
		bRes &= grid[y][x] <= grid[y+1][x];
	return bRes;
}

char findBasin(unsigned char **solution, int **grid, int h, int w, int y, int x)
{
	int nMin = 10001;
	if (x>0)
		nMin = grid[y][x-1];
	if (y>0)
		nMin = min(nMin, grid[y-1][x]);
	if (x<w-1)
		nMin = min(nMin, grid[y][x+1]);
	if (y<h-1)
		nMin = min(nMin, grid[y+1][x]);

	if (y>0 && nMin == grid[y-1][x])
	{
		return solution[y-1][x];
	}
	else
	if (x>0 && nMin == grid[y][x-1])
	{
		return solution[y][x-1];
	}
	else
	if (x<w-1 && nMin == grid[y][x+1])
	{
		return solution[y][x+1];
	}
	else
//	if (y<h-1 && nMin == grid[y+1][x])
	{
		return solution[y+1][x];
	}

}

unsigned char **solve(int **grid, int h, int w)
{
	unsigned char **solution;
	int i,j;
	solution = new unsigned char*[h];
	for (i = 0 ; i < h ; ++i)
	{
		solution[i] = new unsigned char[w];
		for (j=0;j<w;++j)
		{
			solution[i][j] = 0xff;
		}
	}

//	find sink
	char sink = 0;
	for (i=0;i<h;++i)
	{
		for (j=0;j<w;++j)
		{
			if (isSink(grid, h, w, i, j))
				solution[i][j] = sink++;
		}
	}
//	find basins
	bool bChange = true;
	while (bChange)
	{
		bChange = false;
		for (int i=0;i<h;++i)
		{
			for (j=0;j<w;++j)
			{
				if (solution[i][j] == 0xff)
				{
					solution[i][j] = findBasin(solution, grid, h, w, i, j);
					bChange = true;
				}
			}
		}
	}
	return solution;
}

void main()
{
	FILE *fin,*fout;
	int i,j,k;
	int t,h,w;
	fopen_s(&fin, "B-large.in", "rt");
	fopen_s(&fout, "B-large.out", "wb");

	fscanf_s(fin,"%d\n",&t);
	for (i=0;i<t;++i)
	{
		int **grid;
		fscanf_s(fin, "%d %d\n", &h, &w);
		grid = new int*[h];
		for(j=0;j<h;++j)
		{
			grid[j] = new int[w];
			for (k=0;k<w;++k)
			{
				fscanf_s(fin, "%d", &grid[j][k]);
			}
		}
		unsigned char **solution = solve(grid,h,w);
		fprintf(fout, "Case #%d:\n",i+1);
		char charmap[26];
		for (j=0;j<26;++j)
			charmap[j] = 0;
		char basin='a';
		for (j=0;j<h;++j)
		{
			if (charmap[solution[j][0]]==0)
			{
				charmap[solution[j][0]] = basin++;
			}
			fprintf(fout, "%c", charmap[solution[j][0]]);
			for (k=1;k<w;++k)
			{
				if (charmap[solution[j][k]]==0)
				{
					charmap[solution[j][k]] = basin++;
				}
				fprintf(fout, " %c", charmap[solution[j][k]]);
			}
			delete []grid[j];
			delete []solution[j];
			fprintf(fout, "\n");
		}
		delete []grid;
		delete []solution;
	}

	fclose(fin);
	fclose(fout);
}