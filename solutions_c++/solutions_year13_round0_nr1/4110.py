#include<stdio.h>

char Tic[10][10];

int main()
{
	int T;
	scanf("%d",&T);
	for(int cs=1;cs<=T;cs++)
	{
		for(int i=0;i<4;i++)
		{
			scanf("%s",Tic[i]);
			if(Tic[i][0]=='\0')	i--;
		}

		bool xwin=false;
		bool owin=false;
		bool nocom=false;
		bool tie=true;

		for(int i=0;i<4;i++)
		{
			int os=0;
			int xs=0;
			int ts=0;
			for(int j=0;j<4;j++)
			{
				if(Tic[i][j]=='O')	os++;
				if(Tic[i][j]=='X')	xs++;
				if(Tic[i][j]=='T')	ts++;
				if(Tic[i][j]=='.')	nocom=true;
			}
			if(os==4||(os==3&&ts))
				owin=true,tie=false;
			if(xs==4||(xs==3&&ts))
				xwin=true,tie=false;

		}

		for(int i=0;i<4;i++)
		{
			int os=0;
			int xs=0;
			int ts=0;
			for(int j=0;j<4;j++)
			{
				if(Tic[j][i]=='O')	os++;
				if(Tic[j][i]=='X')	xs++;
				if(Tic[j][i]=='T')	ts++;
				if(Tic[j][i]=='.')	nocom=true;
			}
			if(os==4||(os==3&&ts))
				owin=true,tie=false;
			if(xs==4||(xs==3&&ts))
				xwin=true,tie=false;

		}
		int os=0;
		int xs=0;
		int ts=0;
		for(int i=0;i<4;i++)
		{
			if(Tic[i][i]=='O')	os++;
			if(Tic[i][i]=='X')	xs++;
			if(Tic[i][i]=='T')	ts++;
			if(Tic[i][i]=='.')	nocom=true;
		}
		if(os==4||(os==3&&ts))
			owin=true,tie=false;
		if(xs==4||(xs==3&&ts))
			xwin=true,tie=false;
		os=xs=ts=0;
		for(int i=0;i<4;i++)
		{
			if(Tic[i][3-i]=='O')	os++;
			if(Tic[i][3-i]=='X')	xs++;
			if(Tic[i][3-i]=='T')	ts++;
			if(Tic[i][3-i]=='.')	nocom=true;
		}
		if(os==4||(os==3&&ts))
			owin=true,tie=false;
		if(xs==4||(xs==3&&ts))
			xwin=true,tie=false;
		if(nocom) tie=false;
		printf("Case #%d: ",cs);
		if(owin)	printf("O won\n"),nocom=false;
		if(xwin)	printf("X won\n"),nocom=false;
		if(tie)		printf("Draw\n");
		if(nocom)	printf("Game has not completed\n");
	}
	return 0;
}