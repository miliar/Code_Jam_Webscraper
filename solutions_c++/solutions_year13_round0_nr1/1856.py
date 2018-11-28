#include <iostream>
#include <cstdio>

using namespace std;

char G[4][10];

const char *solve()
{
	int i,j;
	for(i=0; i<4; i++)
	{
		for(j=0; j<4; j++)
			if(G[i][j] != 'T' && G[i][j] != 'O')
				break;
		if(j >= 4)
			return "O won";
		for(j=0; j<4; j++)
			if(G[j][i] != 'T' && G[j][i] != 'O')
				break;
		if(j >= 4)
			return "O won";
		for(j=0; j<4; j++)
			if(G[i][j] != 'T' && G[i][j] != 'X')
				break;
		if(j >= 4)
			return "X won";
		for(j=0; j<4; j++)
			if(G[j][i] != 'T' && G[j][i] != 'X')
				break;
		if(j >= 4)
			return "X won";
	}
	for(j=0; j<4; j++)
		if(G[j][j] != 'T' && G[j][j] != 'O')
			break;
	if(j >= 4)
		return "O won";
	for(j=0; j<4; j++)
		if(G[j][3-j] != 'T' && G[j][3-j] != 'O')
			break;
	if(j >= 4)
		return "O won";
	for(j=0; j<4; j++)
		if(G[j][j] != 'T' && G[j][j] != 'X')
			break;
	if(j >= 4)
		return "X won";
	for(j=0; j<4; j++)
		if(G[j][3-j] != 'T' && G[j][3-j] != 'X')
			break;
	if(j >= 4)
		return "X won";

	for(i=0; i<4; i++)
		for(j=0; j<4; j++)
			if(G[i][j] == '.')
				return "Game has not completed";
	return "Draw";
}

int main()
{
	FILE *in,*out;
	char line[1000];
	int T, t;
	int i, j;
	in = fopen("A.in","r");
	out = fopen("A.out","w+");
	fgets(line,999,in);
	sscanf(line,"%d",&T);
	for(t = 1; t <= T; t++)
	{
		for(i = 0; i < 4; i++)
			fgets(G[i],9,in);
		fgets(line,999,in);//empty line
		fprintf(out, "Case #%d: %s\n",t,solve());
	}
	fclose(in);
	fclose(out);
}
