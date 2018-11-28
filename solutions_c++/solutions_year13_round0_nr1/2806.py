#include <stdio.h>

char s[5][5];

char check(int x,int y,int dx,int dy)
{
	char t='\0';
	for(int i=0;i<4;i++)
	{
		if(!t && s[x+i*dx][y+i*dy]!='T')
		{
			if(s[x+i*dx][y+i*dy]=='.')return '\0';
			t=s[x+i*dx][y+i*dy];
		}
		if(s[x+i*dx][y+i*dy]!='T' && t!=s[x+i*dx][y+i*dy])return '\0';
	}
	return t;
}

char cc()
{
	bool full=true;
	for(int i=0;i<4;i++)
	{
		char g=check(i,0,0,1);
		if(g)return g;
		g=check(0,i,1,0);
		if(g)return g;
		for(int j=0;j<4;j++)if(s[i][j]=='.')full=false;
	}
	char g=check(0,0,1,1);
	if(g)return g;
	g=check(3,0,-1,1);
	if(g)return g;
	return full?'D':'G';
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,TC=0;
	scanf("%d",&T);
	while(++TC<=T)
	{
		printf("Case #%d: ",TC);
		for(int i=0;i<4;i++)scanf("%s",s[i]);
		char g=cc();
		switch (g)
		{
		case 'X':
		case 'O':
			printf("%c won\n",g);
			break;
		case 'D':
			puts("Draw");
			break;
		case 'G':
			puts("Game has not completed");
			break;
		}
	}
	return 0;
}