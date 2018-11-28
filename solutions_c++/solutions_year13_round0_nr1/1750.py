#include<iostream>
#include<stdio.h>

using namespace std;

int main()
{
	int T;
	bool Ow,Xw,eC,fin;
	int i,j;
	scanf("%d",&T);
	char grid[4][4];
	for(int c=0;c<T;c++)
	{
		eC=false;
		fin=false;
		for(i=0;i<4;i++)
		{
				for(j=0;j<4;j++)
				{
					cin>>grid[i][j];
					if(grid[i][j]=='.') eC=true;
				}
		}
		for(i=0;i<4;i++)
		{
			Ow=true;
			Xw=true;
			for(j=0;j<4;j++)
			{
				if(grid[i][j]!='X'&&grid[i][j]!='T') Xw=false;
				if(grid[i][j]!='O'&&grid[i][j]!='T') Ow=false;
			}
			if(Ow||Xw)
			{
				fin=true;
				break;
			}
		}
		if(!fin) for(j=0;j<4;j++)
		{
			Ow=true;
			Xw=true;
			for(i=0;i<4;i++)
			{
				if(grid[i][j]!='X'&&grid[i][j]!='T') Xw=false;
				if(grid[i][j]!='O'&&grid[i][j]!='T') Ow=false;
			}
			if(Ow||Xw)
			{
				fin=true;
				break;
			}
		}
		if(!fin)
		{
			Ow=true;
			Xw=true;
			 for(j=0;j<4;j++)
			{
				if(grid[j][j]!='X'&&grid[j][j]!='T') Xw=false;
				if(grid[j][j]!='O'&&grid[j][j]!='T') Ow=false;
			}
			if(Ow||Xw)
				fin=true;
		}
		if(!fin)
		{
			Ow=true;
			Xw=true;
			if(!fin) for(j=0;j<4;j++)
			{
				if(grid[j][3-j]!='X'&&grid[j][3-j]!='T') Xw=false;
				if(grid[j][3-j]!='O'&&grid[j][3-j]!='T') Ow=false;
			}
			if(Ow||Xw)
				fin=true;
		}
		if(Ow)
			printf("Case #%d: O won\n",c+1);
		else if(Xw)
			printf("Case #%d: X won\n",c+1);
		else if(eC)
			printf("Case #%d: Game has not completed\n",c+1);
		else
			printf("Case #%d: Draw\n",c+1);

	}
	return 0;
}
