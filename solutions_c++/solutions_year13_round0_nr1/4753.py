#include <stdio.h>
char D[5][5];
void checkWin(int sy,int sx,int dy,int dx,char& win)
{
	bool check[256]={0,};
	for (int q=0;q<4;++q)
	{
		int y=sy+dy*q;
		int x=sx+dx*q;
		check[ D[y][x] ] = true;
	}
	if (check['.']) return;
	if (check['O'] && check['X']) return;
	win = check['O']?'O':'X';
}
int main()
{
	int T;	scanf("%d",&T);
	for (int kase=1;kase<=T;++kase)
	{
		for (int q=0;q<4;++q) scanf("%s",&D[q][0]);
		char win='.';
		for (int q=0;q<4;++q) 
		{
			checkWin(q,0,0,1,win);
			checkWin(0,q,1,0,win);
		}
		checkWin(0,0,1,1,win);
		checkWin(0,3,1,-1,win);
		if (win=='.') 
		{
			bool anyDot = false;
			for (int q=0;q<4;++q) for (int w=0;w<4;++w) if (D[q][w]=='.') { 
				anyDot = true; break; 
			}
			if (anyDot) printf("Case #%d: Game has not completed\n",kase);
			else		printf("Case #%d: Draw\n",kase);

		}
		else printf("Case #%d: %c won\n",kase,win);
	}
	return 0;
}
