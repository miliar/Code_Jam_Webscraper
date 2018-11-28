#include <cstdio>
#include <assert.h>
using namespace std;

FILE* fin;
FILE* fout;

int R,C,G[100][100];
char result[100][100];
int dr[] = {-1, 0, 0, 1};
int dc[] = {0, -1, 1, 0};

void handleInput()
{
	fscanf(fin, "%d %d", &R, &C);
	for(int i = 0; i < R; i++)
		for(int j = 0; j < C; j++)
		{
			fscanf(fin, "%d", &G[i][j]);
			result[i][j] = '*';
		}
}

char floodFill(int r, int c, char next)
{
	if(result[r][c] != '*')
		return result[r][c];
	int best = G[r][c];
	int bestDir = -1;
	for(int i = 0; i < 4; i++)
	{
		if(r+dr[i] < 0 || r+dr[i] == R || c+dc[i] < 0 || c+dc[i] == C)
			continue;
		if(G[r+dr[i]][c+dc[i]] < best)
		{
			best = G[r+dr[i]][c+dc[i]];
			bestDir = i;
		}
	}
	if(bestDir == -1)
		result[r][c] = next;
	else
		result[r][c] = floodFill(r+dr[bestDir], c+dc[bestDir], next);
	return result[r][c];
}

void getResult()
{	
	int i,j,r,c,f;
	char next = 'a';
	for(i = 0; i < R; i++)
	{
		for(j = 0; j < C; j++)
		{
			fprintf(fout, "%c ", floodFill(i,j,next));
			if(result[i][j] == next)
				next++;
		}
		fprintf(fout, "\n");
	}
}

int main()
{
	fin = fopen ("b.in","r");
	fout = fopen ("b.out","w");
	
	int T;
	fscanf(fin, "%d", &T);
	for(int t = 1; t <= T; t++)
	{
		handleInput();
		fprintf(fout, "Case #%d:\n", t);
		getResult();
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
