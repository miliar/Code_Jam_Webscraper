// google2013_1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


int _tmain(int argc, _TCHAR* argv[])
{
	int cas;
	char game[4][5];
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&cas);
	int t = 0;
	while(cas--)
	{
		t++;
		int i =0;
		gets(game[0]);
		for(i=0; i<4; i++)
			gets(game[i]);
		int j = 0;
		int ix, it, io, ib;
		int win = 2;
		for(i=0; i<4; i++)
		{
			ix = it = io = 0;
			for(j=0; j<4; j++)
			{
				if(game[i][j] == 'X')
					ix++;
				if(game[i][j] == 'T')
					it++;
				if(game[i][j] == 'O')
					io++;
			}
			if( ix + it == 4)
			{
				win = 0;
				goto end;
			}
			if( it + io == 4)
			{
				win = 1;
				goto end;
			}
		}
		
		for(j=0; j<4; j++)
		{
			ix = it = io = 0;
			for(i=0; i<4; i++)
			{
				if(game[i][j] == 'X')
					ix++;
				if(game[i][j] == 'T')
					it++;
				if(game[i][j] == 'O')
					io++;
			}
			if( ix + it == 4)
			{
				win = 0;
				goto end;
			}
			if( it + io == 4)
			{
				win = 1;
				goto end;
			}
		}
		ix = it = io = 0;
		for(i=0; i<4; i++)
		{
			if(game[i][i] == 'X')
				ix++;
			if(game[i][i] == 'T')
				it++;
			if(game[i][i] == 'O')
				io++;
			if( ix + it == 4)
			{
				win = 0;
				goto end;
			}
			if( it + io == 4)
			{
				win = 1;
				goto end;
			}
		}
		ix = it = io = 0;
		for(i=0; i<4; i++)
		{
			if(game[i][3-i] == 'X')
				ix++;
			if(game[i][3-i] == 'T')
				it++;
			if(game[i][3-i] == 'O')
				io++;
			if( ix + it == 4)
			{
				win = 0;
				goto end;
			}
			if( it + io == 4)
			{
				win = 1;
				goto end;
			}
		}

		for(i=0; i<4; i++)
		{
			for(j=0; j<4; j++)
			{
				if(game[i][j] == '.')
				{
					win = 3;
					goto end;
				}
			}
		}
end:
		switch(win)
		{
		case 0: printf("Case #%d: X won\n",t); break;
		case 1: printf("Case #%d: O won\n",t); break;
		case 2: printf("Case #%d: Draw\n",t); break;
		case 3: printf("Case #%d: Game has not completed\n",t); break;
		}
	}
	return 0;
}

