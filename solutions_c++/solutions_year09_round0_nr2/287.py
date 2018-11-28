#include <algorithm>
#include <iostream>

#define MAX 100

using namespace std;

int nRow,nCol,map[MAX][MAX];
char marked[MAX][MAX],nextLab;
const int dir[5][2]={{0,0},{-1,0},{0,-1},{0,1},{1,0}};
int nTest;

char DFS(int row,int col)
{
	if(marked[row][col])return marked[row][col];
	int minInd=0;
	for(int q=1;q<5;q++)
		if(0<=row+dir[q][0]&&row+dir[q][0]<nRow&&0<=col+dir[q][1]&&col+dir[q][1]<nCol&&
			map[row+dir[q][0]][col+dir[q][1]]<map[row+dir[minInd][0]][col+dir[minInd][1]])
			minInd=q;
	if(minInd==0)return marked[row][col]=nextLab++;
	return marked[row][col]=DFS(row+dir[minInd][0],col+dir[minInd][1]);
}

int main()
{
	/*
	freopen("input.txt","wt",stdout);
	printf("2\n100 100\n");
	for(int q=0;q<100;q++)
	{
		for(int w=0;w<100;w++)
			printf("%d ",q*100+w+1);
		printf("\n");
	}
	printf("100 100\n");
	for(int q=0;q<100;q++)
	{
		for(int w=0;w<100;w++)
			printf("%d ",10000-q*100+w);
		printf("\n");
	}
	return 0;
	*/
	
	freopen("in.txt","rt",stdin);
	freopen("out.txt","wt",stdout);
	scanf("%d ",&nTest);
	for(int test=1;test<=nTest;test++)
	{
		nextLab=1;
		fill(&marked[0][0],&marked[MAX-1][MAX],'\0');
		scanf("%d %d",&nRow,&nCol);
		for(int q=0;q<nRow;q++)
			for(int w=0;w<nCol;w++)
				scanf("%d",&map[q][w]);
		for(int q=0;q<nRow;q++)
			for(int w=0;w<nCol;w++)
				DFS(q,w);
		printf("Case #%d:\n",test);
		for(int q=0;q<nRow;q++)
		{
			for(int w=0;w<nCol;w++)
				printf("%c ",marked[q][w]+'a'-1);
			printf("\n");
		}
	}
	
	return 0;
}
