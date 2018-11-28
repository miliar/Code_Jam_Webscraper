#include<iostream>
#include<cstdio>
using namespace std;

char g[10][10];

bool isx(char ch)
{
	return ch=='X' || ch=='T';
}
bool iso(char ch)
{
	return ch=='O' || ch=='T';
}

char chk()
{
	for(int i = 1; i <= 4; i ++)
	{
		if(isx(g[i][1]) && isx(g[i][2]) && isx(g[i][3]) && isx(g[i][4]) ) return 'X';
		if(iso(g[i][1]) && iso(g[i][2]) && iso(g[i][3]) && iso(g[i][4]) ) return 'O';
		
		if(isx(g[1][i]) && isx(g[2][i]) && isx(g[3][i]) && isx(g[4][i]) ) return 'X';
		if(iso(g[1][i]) && iso(g[2][i]) && iso(g[3][i]) && iso(g[4][i]) ) return 'O';
	}
	
	if( isx(g[1][1]) && isx(g[2][2]) && isx(g[3][3]) && isx(g[4][4]) ) return 'X';
	if( iso(g[1][1]) && iso(g[2][2]) && iso(g[3][3]) && iso(g[4][4]) ) return 'O';
	if( isx(g[1][4]) && isx(g[2][3]) && isx(g[3][2]) && isx(g[4][1]) ) return 'X';
	if( iso(g[1][4]) && iso(g[2][3]) && iso(g[3][2]) && iso(g[4][1]) ) return 'O';
	
	return '.';
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	int cas;
	scanf("%d",&cas);
	for(int t = 1; t <= cas; t ++)
	{
		int cnt = 0;
		for(int i = 1; i <= 4; i ++)
			scanf("%s", g[i]+1);
			
		for(int i = 1; i <= 4; i ++)
			for(int j = 1; j <= 4; j ++)
				if(g[i][j] == '.')
					cnt ++;
		
		printf("Case #%d: ", t);
		
		char ans = chk();
		if(ans == '.')
		{
			if(cnt == 0) printf("Draw\n");
			else printf("Game has not completed\n");
		}
		else printf("%c won\n", ans);
	}
}
