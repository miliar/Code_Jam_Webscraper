#include<stdio.h>
#include<conio.h>
void main()
{
	char tictac[5][5];
	int sameX=0,sameO=0,t,done=0;

	scanf("%i\n",&t);
	for(int n=1;n<=t;n++)
	{
		done=0;
		for(int x=0;x<=3;x++)
		{
			gets(tictac[x]);
			//printf("ea%s\n",tictac[x]);
		}
		scanf("\n");
		//printf("\n");
//horizontal
		for(x=0;x<=3 && done==0;x++)
		{
			sameX=0;sameO=0;
			for(int y=0;y<=3;y++)
			{
				if(tictac[x][y]=='X')
				{
					sameX++;
				}
				else if(tictac[x][y]=='O')
				{
					sameO++;
				}
				else if(tictac[x][y]=='T')
				{
					sameX++;
				sameO++;
				}
			}
			//printf("%i.H X=%i O=%i\n",n,sameX,sameO);
			if(sameX==4)
			{
				done=1;
				printf("Case #%i: X won\n",n);
			}
			else if(sameO==4)
			{
				done=1;
				printf("Case #%i: O won\n",n);
			}
		}
//vertical
		for(x=0;x<=3 && done==0;x++)
		{
			sameX=0;sameO=0;
			for(int y=0;y<=3;y++)
			{
				if(tictac[y][x]=='X')
				{
					sameX++;
				}
				else if(tictac[y][x]=='O')
				{
					sameO++;
				}
				else if(tictac[y][x]=='T')
				{
					sameX++;
				sameO++;
				}
			}
			//printf("%i.V X=%i O=%i\n",n,sameX,sameO);
			if(sameX==4)
			{
				done=1;
				printf("Case #%i: X won\n",n);
			}
			else if(sameO==4)
			{
				done=1;
				printf("Case #%i: O won\n",n);
			}
		}

//diagonal \
		sameX=0;sameO=0;
		for(x=0;x<=3 && done==0;x++)
		{
			if(tictac[x][x]=='X')
			{
				sameX++;
			}
			else if(tictac[x][x]=='O')
			{
				sameO++;
			}
			else if(tictac[x][x]=='T')
			{
				sameX++;
				sameO++;
			}
		}
		if(sameX==4 && done==0)
		{
			done=1;
			printf("Case #%i: X won\n",n);
		}
		else if(sameO==4 && done==0)
		{
			done=1;
			printf("Case #%i: O won\n",n);
		}

//diagonal /
		sameX=0;sameO=0;
		int y;
		for(x=3,y=0;x>=0 && done==0;x--,y++)
		{
			if(tictac[y][x]=='X')
			{
				sameX++;
			}
			else if(tictac[y][x]=='O')
			{
				sameO++;
			}
			else if(tictac[y][x]=='T')
			{
				sameX++;
				sameO++;
			}
		}
		if(done==0)
		//printf("ea%i %i %i\n",n,sameX,sameO);
		if(sameX==4 && done==0)
		{
			done=1;
			printf("Case #%i: X won\n",n);
		}
		else if(sameO==4 && done==0)
		{
			done=1;
			printf("Case #%i: O won\n",n);
		}
		int dot=0;
		for(x=0;x<=3 && done==0;x++)
		{
			for(y=0;y<=3;y++)
			{
				if(tictac[x][y]=='.')
				{
					dot++;
				}
			}
			if(dot>0)
			{
				done=1;
				//printf("%i\n",dot);
				printf("Case #%i: Game has not completed\n",n);
			}
		}
		//if(done==0)
		//printf("%i",dot);
		if(done==0 && dot==0)
		{
			printf("Case #%i: Draw\n",n);
		}

	}

}