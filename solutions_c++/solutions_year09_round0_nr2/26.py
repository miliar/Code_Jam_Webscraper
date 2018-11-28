#include <vector>
#include <cstdio>
#include <iostream>

using namespace std;

int n, m, board[100][100];
char number[100][100], sinkN;
int mov[4][2]={{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

char doDFS(int, int);

int main(void)
{
	int t;
	cin>>t;
	for(int caseN=1;caseN<=t;caseN++)
	{
		cin>>n>>m;
		for(int i=0;i<n;i++) for(int j=0;j<m;j++) cin>>board[i][j];

		memset(number, -1, sizeof(number));
		sinkN='a';

		for(int i=0;i<n;i++) for(int j=0;j<m;j++) if(number[i][j]==-1) doDFS(i, j);

		printf("Case #%d:\n", caseN);
		for(int i=0;i<n;i++) 
		{
			for(int j=0;j<m;j++) printf("%c ", number[i][j]);
			printf("\n");
		}
	}

	return 0;
}

char doDFS(int r, int c)
{
	if(number[r][c]!=-1) return number[r][c];

	int y=r, x=c, minVal=board[r][c];
	for(int i=0;i<4;i++)
	{
		int ny=r+mov[i][0], nx=c+mov[i][1];
		if(ny>=0 &&  ny<n && nx>=0 && nx<m && board[ny][nx]<minVal) { minVal=board[ny][nx]; y=ny, x=nx; }
	}

	if(r==y && c==x) { number[r][c]=sinkN; sinkN++; return number[r][c]; }
	else return number[r][c]=doDFS(y, x);
}
