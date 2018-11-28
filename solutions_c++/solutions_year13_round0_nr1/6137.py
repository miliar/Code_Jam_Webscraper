#include<stdio.h>
#include<conio.h>
#define MAX 4
char board[MAX][MAX];
int tic_tac_toe()
{
	int i,j;
	for(i=0;i<4;i++)
	{
		if(board[i][1]==board[i][2] && board[i][2]==board[i][3])
		{
			if(board[i][0]==board[i][1])
			{
				if(board[i][1]=='X')
					return 1;
				else if(board[i][1]=='O') return 2;
			}
			else if(board[i][0]=='T')
			{
				if(board[i][1]=='X')
					return 1;
				else if(board[i][1]=='O') return 2;
			}
		}
		if(board[i][0]==board[i][2] && board[i][2]==board[i][3])
		{
			if(board[i][0]==board[i][1])
			{
				if(board[i][0]=='X')
					return 1;
				else if(board[i][0]=='O') return 2;
			}
			else if(board[i][1]=='T')
			{
				if(board[i][0]=='X')
					return 1;
				else if(board[i][0]=='O')return 2;
			}
		}
		if(board[i][0]==board[i][1] && board[i][1]==board[i][3])
		{
			if(board[i][0]==board[i][2])
			{
				if(board[i][0]=='X')
					return 1;
				else if(board[i][0]=='O') return 2;
			}
			else if(board[i][2]=='T')
			{
				if(board[i][0]=='X')
					return 1;
				else if(board[i][0]=='O') return 2;
			}
		}
		if(board[i][0]==board[i][1] && board[i][1]==board[i][2])
		{
			if(board[i][0]==board[i][3])
			{
				if(board[i][0]=='X')
					return 1;
				else if(board[i][0]=='O') return 2;
			}
			else if(board[i][3]=='T')
			{
				if(board[i][0]=='X')
					return 1;
				else if(board[i][0]=='O') return 2;
			}
		}//end for zeroth row
	}//end for row-wise checking
	
	
	for(j=0;j<4;j++)
	{
		if(board[1][j]==board[2][j] && board[2][j]==board[3][j])
		{
			if(board[0][j]==board[1][j])
			{
				if(board[1][j]=='X')
					return 1;
				else if(board[1][j]=='O') return 2;
			}
			else if(board[0][j]=='T')
			{
				if(board[1][j]=='X')
					return 1;
				else if(board[1][j]=='O') return 2;
			}
		}
		if(board[0][j]==board[2][j] && board[2][j]==board[3][j])
		{
			if(board[0][j]==board[1][j])
			{
				if(board[0][j]=='X')
					return 1;
				else if(board[0][j]=='O') return 2;
			}
			else if(board[1][j]=='T')
			{
				if(board[0][j]=='X')
					return 1;
				else if(board[0][j]=='O') return 2;
			}
		}
		if(board[0][j]==board[1][j] && board[1][j]==board[3][j])
		{
			if(board[0][j]==board[2][j])
			{
				if(board[0][j]=='X')
					return 1;
				else if(board[0][j]=='O') return 2;
			}
			else if(board[2][j]=='T')
			{
				if(board[0][j]=='X')
					return 1;
				else if(board[0][j]=='O') return 2;
			}
		}
		if(board[0][j]==board[1][j] && board[1][j]==board[2][j])
		{
			if(board[0][j]==board[3][j])
			{
				if(board[0][j]=='X')
					return 1;
				else if(board[0][j]=='O') return 2;
			}
			else if(board[3][j]=='T')
			{
				if(board[0][j]=='X')
					return 1;
				else if(board[0][j]=='O') return 2;
			}
		}//end for zeroth column
	}//end for column-wise checking
	
	if(board[0][0]==board[1][1] && board[1][1]==board[2][2] && board[2][2]==board[3][3])
	{
		if(board[0][0]=='X')
			return 1;
		else if(board[0][0]=='O') return 2;
	}
	if(board[0][0]=='T')
		if(board[1][1]==board[2][2] && board[2][2]==board[3][3])
		{
			if(board[1][1]=='X')
				return 1;
			else if(board[1][1]=='O') return 2;
		}
	if(board[1][1]=='T')
		if(board[0][0]==board[2][2] && board[2][2]==board[3][3])
		{
			if(board[0][0]=='X')
				return 1;
			else if(board[0][0]=='O') return 2;
		}
	if(board[2][2]=='T')
		if(board[0][0]==board[1][1] && board[1][1]==board[3][3])
		{
			if(board[0][0]=='X')
				return 1;
			else if(board[0][0]=='O') return 2;
		}
	if(board[3][3]=='T')
		if(board[0][0]==board[1][1] && board[1][1]==board[2][2])
		{
			if(board[0][0]=='X')
				return 1;
			else if(board[0][0]=='O') return 2;
		}
	//1st diagonal checked
	
	
	if(board[0][3]==board[1][2] && board[1][2]==board[2][1] && board[2][1]==board[3][0])
	{
		if(board[0][3]=='X')
			return 1;
		else if(board[0][3]=='O') return 2;
	}
	if(board[0][3]=='T')
		if(board[1][2]==board[2][1] && board[2][1]==board[3][0])
		{
			if(board[1][2]=='X')
				return 1;
			else if(board[1][2]=='O') return 2;
		}
	if(board[1][2]=='T')
		if(board[0][3]==board[2][1] && board[2][1]==board[3][0])
		{
			if(board[0][3]=='X')
				return 1;
			else if(board[0][3]=='O') return 2;
		}
	if(board[2][1]=='T')
		if(board[0][3]==board[1][2] && board[1][2]==board[3][0])
		{
			if(board[0][3]=='X')
				return 1;
			else if(board[0][3]=='O') return 2;
		}
	if(board[3][0]=='T')
		if(board[0][3]==board[1][2] && board[1][2]==board[2][1])
		{
			if(board[0][3]=='X')
				return 1;
			else if(board[0][3]=='O') return 2;
		}
	//2nd diagonal checked
	
	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			if(board[i][j]=='.')
				return 4;//game not completed checked
	return 3;//else its a draw		
}

int main()
{
	int T;
	int i,j,t=1;
	int status;
	FILE *fin=fopen("A-large.in","r");
	FILE *fout=fopen("A-large.out","w");
	if(!fin)
		printf("Input file not found!");
	if(!fout)
		printf("Output file not found!");
	fscanf(fin,"%d",&T);
	for(t=1;t<=T;t++)
	{
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				fscanf(fin," %c",&board[i][j]);
		status=tic_tac_toe();
		switch(status)
		{
			case 1:fprintf(fout,"Case #%d: X won\n",t);
				   break;
			case 2:fprintf(fout,"Case #%d: O won\n",t);
				   break;
			case 3:fprintf(fout,"Case #%d: Draw\n",t);
				   break;
			case 4:fprintf(fout,"Case #%d: Game has not completed\n",t);
				   break;
		}
	}
	return 0;
}
