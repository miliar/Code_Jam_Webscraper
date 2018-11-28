#include <iostream>
#include <cstdio>
using namespace std;
int dir[8][2]={{-1,0},{0,-1},{-1,-1},{-1,1},
               {1,0},{0,1},{1,1},{1,-1}};
char setup[4][5];
bool iscomplete;
bool xwon,owon;
bool check(int x, int y)
{
	return x>=0 && y>=0 && x<4 && y<4;
}
int count(int x, int y)
{
	if(setup[x][y] == '.')
	{
		if(iscomplete) iscomplete = false;
		return 0;
	}
	if(setup[x][y] == 'T')
		return 0;
	int tx,ty,cnt;
	for(int i = 0; i < 4; ++i)
	{
		tx = x + dir[i][0];
		ty = y + dir[i][1];
		cnt = 0;
		while(check(tx,ty) && (setup[tx][ty] == setup[x][y] || setup[tx][ty] == 'T'))
		{
			++cnt;
			tx+=dir[i][0];
			ty+=dir[i][1];
		}
		tx = x + dir[i+4][0];
		ty = y + dir[i+4][1];
		while(check(tx,ty) && (setup[tx][ty] == setup[x][y] || setup[tx][ty] == 'T'))
		{
			++cnt;
			tx+=dir[i+4][0];
			ty+=dir[i+4][1];
		}
		if(cnt == 3 )
		{
			if(setup[x][y] == 'X')
				return 1;
			else return 2;
		}		
	}
	return 0;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int cas = 1; cas <= T; ++cas)
	{
		iscomplete = true;
		xwon = false;
		owon = false;
		for(int i = 0; i < 4; ++i)
		{
			scanf("%s",setup[i]);
		}
		for(int i = 0; i < 4; ++i)
		{
			for(int j = 0; j < 4; ++j)
			{
				int temp = count(i,j);
				if(temp == 1)
				{
					xwon = true;
					break;
				}
				else if(temp == 2)
				{
					owon = true;
					break;
				}
			}
			if(owon || xwon)
				break;
		}
		printf("Case #%d: ",cas);
		if(xwon) printf("X won\n");
		else if(owon) printf("O won\n");
		else if(iscomplete) printf("Draw\n");
		else printf("Game has not completed\n");
	}
	return 0;
}