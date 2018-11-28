#include <cstdio>

int N;
char m[4][5];

int main()
{
	scanf("%d",&N);
	for (int k = 1; k <= N; k++)
	{
		for (int i = 0; i < 4; i++) scanf("%s",m[i]);
		int c = 0; char ac = ' ';
		int x=0,t=0,o=0;
		bool ff = false;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (m[i][j]=='.') ff = true;
			}
		}
		if (!ff)c = 2;
		for (int i = 0; i < 4; i++)
		{
			x=0,t=0,o=0;
			for (int j = 0; j < 4; j++)
			{
				if (m[i][j]=='X') x++;
				if (m[i][j]=='O') o++;
				if (m[i][j]=='T') t++;
			}
			if (x+t==4) c=1,ac='X';
			if (o+t==4) c=1,ac='O';
			
			x=0,t=0,o=0;
			for (int j = 0; j < 4; j++)
			{
				if (m[j][i]=='X') x++;
				if (m[j][i]=='O') o++;
				if (m[j][i]=='T') t++;
			}
			if (x+t==4) c=1,ac='X';
			if (o+t==4) c=1,ac='O';
		}
		x=0,o=0,t=0;
		for (int i = 0; i < 4; i++)
		{
			if (m[i][i]=='X') x++;
			if (m[i][i]=='O') o++;
			if (m[i][i]=='T') t++;
		}
		if (x+t==4) c=1,ac='X';
		if (o+t==4) c=1,ac='O';
		
		x=0,o=0,t=0;
		for (int i = 0; i < 4; i++)
		{
			if (m[i][3-i]=='X') x++;
			if (m[i][3-i]=='O') o++;
			if (m[i][3-i]=='T') t++;
		}
		if (x+t==4) c=1,ac='X';
		if (o+t==4) c=1,ac='O';
		
		if (c==0) printf("Case #%d: Game has not completed\n",k);
		if (c==1) printf("Case #%d: %c won\n",k,ac);
		if (c==2) printf("Case #%d: Draw\n",k);
	}
}