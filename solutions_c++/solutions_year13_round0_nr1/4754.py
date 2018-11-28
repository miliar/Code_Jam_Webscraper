#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>


void main()
{
int cases,index_cases,i,j;
char board[4][4];
char line[5];
char col,row, colcount, rowcount, emptycell, option, possrow, posscol;

freopen("A-large.in" , "rt" , stdin ) ;
freopen("A-large.out" , "wt" , stdout ) ;

cases = 0;
//read the number of test cases 
scanf("%d",&cases);
//printf("Cases = %d\n",cases);

//Loop through all the cases
for (index_cases=0 ; index_cases<cases; index_cases++)
{
	emptycell=0;
	for (i=0;i<4;i++)
	{
		scanf("%s",&line);
//		printf("%s\n",line);
		for (j=0;j<4;j++)
		{
			board[i][j] = line[j];
			if (board[i][j]=='.') 
			{	
				emptycell++;
//				printf("emptycell <%c>  %d, %d\n",board[i][j], i,j);
			}
//			printf("Board[%d][%d] = %c\n",i,j,board[i][j]);
	
		}
	}

	for (option=0; option<4; option++)
	{
			row=0;
			col=0;
			rowcount = 0;
			colcount = 0;
			possrow = 1;
			posscol = 1;
//		printf("emptycell %d\n",emptycell);
		for (j=0 ; (j<4) && ((possrow) || (posscol)) ; j++)
		{
			if (possrow)
			{
				if (row == 0)
				{
					if (board[option][j] != '.') rowcount++;
					else possrow = 0;
					if((board[option][j] == 'X')||(board[option][j] == 'O')) row = board[option][j];
				}
				else
				{
					if((board[option][j]==row)||(board[option][j]=='T')) rowcount++;
					else possrow = 0;
				}
			}

			if (posscol)
			{
				if (col == 0)
				{
					if(board[j][option] != '.') colcount++;
					else posscol = 0;
					if((board[j][option] == 'X')||(board[j][option] == 'O')) col = board[j][option];
				}
				else
				{
					if((board[j][option]==col)||(board[j][option]=='T')) colcount++;
					else posscol = 0;
				}
			}

		}
		if ((colcount==4)||(rowcount==4))break;
	}
//	printf("colc %d, rowc %d\n",colcount, rowcount);
	if ((colcount<4)&&(rowcount<4))
	{
		row=0;
		col=0;
		rowcount = 0;
		colcount = 0;
		possrow = 1;
		posscol = 1;
		
		for (j=0 ; (j<4) && ((possrow) || (posscol)) ; j++)
		{
			if (possrow)
			{
				if (row == 0)
				{
					if (board[j][j] != '.') rowcount++;
					else possrow = 0;
					if((board[j][j] == 'X')||(board[j][j] == 'O')) row = board[j][j];
				}
				else
				{
					if((board[j][j]==row)||(board[j][j]=='T')) rowcount++;
					else possrow = 0;
				}
			}

			if (posscol)
			{
				if (col == 0)
				{
					if (board[j][3-j] != '.') colcount++;
					else posscol = 0;
					if((board[j][3-j] == 'X')||(board[j][3-j] == 'O')) col = board[j][3-j];
				}
				else
				{
					if((board[j][3-j]==col)||(board[j][3-j]=='T')) colcount++;
					else posscol = 0;
				}
			}

		}	
//	printf("colc %d, rowc %d\n",colcount, rowcount);
	}


	printf("Case #%d: ",index_cases+1);
	if ((colcount==4)||(rowcount==4))
	{
		if (colcount==4)
			printf("%C won\n",col);
		else
			printf("%C won\n",row);
	}
	else 
		if (emptycell) printf("Game has not completed\n");
		else printf("Draw\n");


	
	
	//	for (i=0;i<4;i++)
//	{
//		for (j=0;j<4;j++)
//		{
//			printf("%c ",board[i][j]);
//		}
//	printf("\n");
//	}
}
fclose(stdin) ;
fclose(stdout) ;

}