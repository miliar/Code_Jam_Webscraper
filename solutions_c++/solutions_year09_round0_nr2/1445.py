#include <cstdio>
#include <cstring>
#include <algorithm>
#define MAX 105

using namespace std;

int nmaps, grid[MAX][MAX], nrows, ncols, dirr[]={-1,0,0,1}, dirc[]={0,-1,1,0};
char answer[MAX][MAX], curchar;

char go(int r, int c)
{
	if(answer[r][c])
		return answer[r][c];
	
	int best=-1, bestr, bestc;
	for(int i=0; i<4; i++)
		if(r+dirr[i]>=0 && r+dirr[i]<nrows && c+dirc[i]>=0 && c+dirc[i]<ncols && 
			grid[r+dirr[i]][c+dirc[i]]<grid[r][c] && (best==-1 || grid[r+dirr[i]][c+dirc[i]]<best))
		{
			best=grid[r+dirr[i]][c+dirc[i]];
			bestr=r+dirr[i];
			bestc=c+dirc[i];
		}
	
	if(best==-1)
		answer[r][c]=curchar++;
	else
		answer[r][c]=go(bestr, bestc);
	
	return answer[r][c];
}

int main()
{
	scanf("%d", &nmaps);
	for(int i=0; i<nmaps; i++)
	{
		curchar='a';
		memset(grid, 0, sizeof(grid));
		memset(answer, 0, sizeof(answer));
		scanf("%d %d", &nrows, &ncols);
		for(int j=0; j<nrows; j++)
			for(int k=0; k<ncols; k++)
				scanf("%d", &grid[j][k]);
		
		for(int j=0; j<nrows; j++)
			for(int k=0; k<ncols; k++)
				answer[j][k]=go(j, k);
		
		printf("Case #%d:\n", i+1);
		for(int j=0; j<nrows; j++)
		{
			for(int k=0; k<ncols; k++)
				printf("%c ", answer[j][k]);
			putchar('\n');
		}
	}
}
