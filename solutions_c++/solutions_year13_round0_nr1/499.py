#include <cstdio>

const int MAXN = 4;
char str[MAXN][MAXN+1];

int main()
{
	int T;
	scanf("%d", &T);
	
	for(int t = 1; t <= T; t++)
	{
		int p = 0;
		bool win[2] = {false, false};
		char play[2] = {'O', 'X'}, wild = 'T';
		
		for(int i = 0; i < MAXN; i++)
		{
			scanf("%s", str[i]);
			for(int j = 0; j < MAXN; j++)
				if(str[i][j] != '.')
					++p;
		}
		
		for(int pp = 0; pp < 2; pp++)
		{
			//row column
			for(int i = 0; i < MAXN; i++)
			{
				int V = 0, T = 0;
				for(int j = 0; j < MAXN; j++)
					if(str[i][j] == play[ pp ])
						++V;
					else if(str[i][j] == wild)
						++T;
				
				if( (V==3 && T==1) || V==4 )
				{
					win[pp] = true;
					break;
				}
				
				V = 0, T = 0;
				for(int j = 0; j < MAXN; j++)
					if(str[j][i] == play[ pp ])
						++V;
					else if(str[j][i] == wild)
						++T;
				
				if( (V==3 && T==1) || V==4 )
				{
					win[pp] = true;
					break;
				}
			}
			
			if(win[pp]) break;
			//two diagonals
			int V = 0, T = 0;
			for(int i = 0; i < MAXN; i++)
				if(str[i][i] == play[ pp ])
					++V;
				else if(str[i][i] == wild)
					++T;
					
			if( (V==3 && T==1) || V==4 )
			{
				win[pp] = true;
				break;
			}

			V = 0, T = 0;
			for(int i = 0; i < MAXN; i++)
				if(str[i][MAXN-1-i] == play[ pp ])
					++V;
				else if(str[i][MAXN-1-i] == wild)
					++T;
					
			if( (V==3 && T==1) || V==4 )
			{
				win[pp] = true;
				break;
			}				
		}
		
		printf("Case #%d: ", t);
		if(win[0]) printf("O won\n");
		else if(win[1]) printf("X won\n");
		else if(p == MAXN*MAXN) printf("Draw\n");
		else printf("Game has not completed\n");
	}
	
	
	return 0;
}