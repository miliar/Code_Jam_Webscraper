#include <stdio.h>

using namespace std;

char a[21][21];
int WhoWinHorizontal(int x)//0: O wins, 1: X wins, -1 continue
{
	int xcount = 0,ocount = 0;
	for(int i = 0;i < 4;i++)
	{
		if(a[i][x] == 'X' || a[i][x] == 'T')xcount++;
		if(a[i][x] == 'O' || a[i][x] == 'T')ocount++;
	}
	if(xcount == 4)return 1;
	else if(ocount == 4)return 0;
	return -1;
}

int WhoWinVertically(int x)//0: O wins, 1: X wins, -1 continue
{
	int xcount = 0,ocount = 0;
	for(int i = 0;i < 4;i++)
	{
		if(a[x][i] == 'X' || a[x][i] == 'T')xcount++;
		if(a[x][i] == 'O' || a[x][i] == 'T')ocount++;
	}
	if(xcount == 4)return 1;
	else if(ocount == 4)return 0;
	return -1;
}

int WhoWinLRDiagonally()//0: O wins, 1: X wins, -1 continue
{
	int xcount = 0,ocount = 0;
	for(int i = 0;i < 4;i++)
	{
		if(a[i][i] == 'X' || a[i][i] == 'T')xcount++;
		if(a[i][i] == 'O' || a[i][i] == 'T')ocount++;
	}
	if(xcount == 4)return 1;
	else if(ocount == 4)return 0;
	return -1;
}

int WhoWinRLDiagonally()//0: O wins, 1: X wins, -1 continue
{
	int xcount = 0,ocount = 0;
	for(int i = 0;i < 4;i++)
	{
		if(a[i][3 - i] == 'X' || a[i][3 - i] == 'T')xcount++;
		if(a[i][3 - i] == 'O' || a[i][3 - i] == 'T')ocount++;
	}
	if(xcount == 4)return 1;
	else if(ocount == 4)return 0;
	return -1;
}

bool GameEnded()
{
	for(int i = 0;i < 4;i++)
	for(int j = 0;j < 4;j++)
	if(a[i][j] == '.')return false;
	return true;
}

int main()
{
	
	freopen("tic.in","r",stdin);//REmove me
	freopen("tic.out","w",stdout);
	int t,res,pos;
	char e;
	scanf("%d%c",&t,&e);
	for(int q = 0;q < t;q++)
	{
		res = -1;
		for(int i = 0;i < 4;i++)
		{
			for(int j = 0;j < 4;j++)
			scanf("%c",&a[i][j]);
			scanf("%c",&e);
		}
		
		pos = 0;
		while(res == -1 && pos < 4)res = WhoWinHorizontal(pos++);
		pos = 0;
		while(res == -1 && pos < 4)res = WhoWinVertically(pos++);
		
		if(res == -1)res = WhoWinLRDiagonally();
		if(res == -1)res = WhoWinRLDiagonally();
		
		if(res == 0)printf("Case #%d: O won\n",q+1);
		else if(res == 1)printf("Case #%d: X won\n",q+1);
		else if(!GameEnded())printf("Case #%d: Game has not completed\n",q+1);
		else if(GameEnded())printf("Case #%d: Draw\n",q+1);
		
		if(q < t - 1)scanf("%c",&e);
		
	}
	
}
