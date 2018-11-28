#include <cstdio>
using namespace std;

char st[4][5];

int run()
{
	int cx, cy;
	for(int i=0; i<4; i++)
	{
		cx = cy = 0;
		for(int j=0; j<4; j++)
		{
			switch(st[i][j])
			{
				case 'X': cx++; break;
				case 'O': cy++; break;
				case 'T': cx++; cy++; break;
			}
		}
		//printf("cx=%d, cy=%d\n", cx, cy);
		if(cx==4) return 0;
		if(cy==4) return 1;
	}
	for(int i=0; i<4; i++)
	{
		cx = cy = 0;
		for(int j=0; j<4; j++)
		{
			switch(st[j][i])
			{
				case 'X': cx++; break;
				case 'O': cy++; break;
				case 'T': cx++; cy++; break;
			}
		}
		//printf("cx=%d, cy=%d\n", cx, cy);
		if(cx==4) return 0;
		if(cy==4) return 1;
	}
	cx = cy = 0;
	for(int i=0; i<4; i++)
	{
		switch(st[i][i])
		{
			case 'X': cx++; break;
			case 'O': cy++; break;
			case 'T': cx++; cy++; break;
		}
	}
	//printf("cx=%d, cy=%d\n", cx, cy);
	if(cx==4) return 0;
	if(cy==4) return 1;
	cx = cy = 0;
	for(int i=0; i<4; i++)
	{
		switch(st[i][3-i])
		{
			case 'X': cx++; break;
			case 'O': cy++; break;
			case 'T': cx++; cy++; break;
		}
	}
	//printf("cx=%d, cy=%d\n", cx, cy);
	if(cx==4) return 0;
	if(cy==4) return 1;
	for(int i=0; i<4; i++) for(int j=0; j<4; j++)
		if(st[i][j]=='.') return 2;
	return 3;
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int t=1; t<=T; t++)
	{
		gets(st[0]);
		for(int i=0; i<4; i++) gets(st[i]);
		int ans = run();
		printf("Case #%d: ", t);
		switch(ans)
		{
			case 0: printf("X won\n"); break;
			case 1: printf("O won\n"); break;
			case 2: printf("Game has not completed\n"); break;
			case 3: printf("Draw\n"); break;
		}
	}
	return 0;
}
