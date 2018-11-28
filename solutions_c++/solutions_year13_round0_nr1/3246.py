#include<stdio.h>
#include<stdlib.h>

int cases,board[4][4];
const int X=5,O=100,T=11;

bool testwin(int p)
{
	bool ret = false;
	int WCond1,WCond2;
	int rowsum,columnsum,diag1,diag2;
	WCond1 = 4*p;
	WCond2 = 3*p + T;
	int i,j,k;
	for (i = 0; i<4; i++)
	{
		rowsum = 0;
		columnsum = 0;
		for (j = 0; j<4;j++)
		{
			rowsum+=board[i][j];
			columnsum+=board[j][i];
		}
		if (rowsum == WCond1 || rowsum == WCond2 || columnsum == WCond1 || columnsum == WCond2)
		{
			ret = true;
			return ret;
		}
	}
	diag1 = board[0][0] + board[1][1] + board[2][2] + board[3][3];
	diag2 = board[0][3] + board[1][2] + board[2][1] + board[3][0];
	if (diag1 == WCond1 || diag1 == WCond2 || diag2 == WCond1 || diag2 == WCond2)
	{
		ret = true;
		return ret;
	}
	return ret;
}

int main()
{
	bool full,xwin,owin;
	int i,j,k;
	char temp[4];
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d\n",&cases);
	for (i = 0; i<cases; i++)
	{
		full = true;
		for(j = 0;j<4;j++)
		{
			scanf("%s\n",temp);
			for (k = 0; k<4; k++)
			{
				if (temp[k] == 'X')
					board[j][k] = X;
				if (temp[k] == 'O')
					board[j][k] = O;
				if (temp[k] == 'T')
					board[j][k] = T;
				if (temp[k] == '.')
				{
					board[j][k] = 0;
					full = false;
				}
			}
		}
		scanf("\n");
		xwin = testwin(X);
		owin = testwin(O);
		if (xwin)
			printf("Case #%d: X won\n",i+1);
		if (owin)
			printf("Case #%d: O won\n",i+1);
		if (!xwin && !owin && full)
			printf("Case #%d: Draw\n",i+1);
		if (!xwin && !owin && !full)
			printf("Case #%d: Game has not completed\n",i+1);
	}
}
