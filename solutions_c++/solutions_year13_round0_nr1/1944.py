#include <cstdio>
#include <algorithm>
using namespace std;

int T;
char G[5][5];

char check4(char a, char b, char c, char d)
{
	char x[4] = {a,b,c,d};
	sort(x,x+4);
	if(x[0]=='.')
		return '.';
	if(x[0]=='T')
		return 'X';
	if(x[3]=='T')
		return 'O';
	if(x[0]==x[3])
		return x[0];
	return '.';
}

char get_winner()
{
	char r,c;
	for(int i = 0; i < 4; i++)
	{
		r = check4(G[i][0],G[i][1],G[i][2],G[i][3]);
		c = check4(G[0][i],G[1][i],G[2][i],G[3][i]);
		if(r!='.')
			return r;
		if(c!='.')
			return c;
	}
	r = check4(G[0][0],G[1][1],G[2][2],G[3][3]);
	c = check4(G[0][3],G[1][2],G[2][1],G[3][0]);
	if(r!='.')
		return r;
	if(c!='.')
		return c;
	return '.';
}

bool is_over()
{
	for(int r = 0; r < 4; r++)
		for(int c = 0; c < 4; c++)
			if(G[r][c] == '.')
				return false;
	return true;
}

int main()
{
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		for(int r = 0; r < 4; r++)
			scanf("%s", G[r]);
		char winner = get_winner();
		if(winner != '.')
			printf("%c won\n", winner);
		else if(is_over())
			printf("Draw\n");
		else
			printf("Game has not completed\n");
	}
}

