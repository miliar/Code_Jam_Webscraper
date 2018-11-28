#include <stdio.h>

FILE *fout;

void prn(int f)
{
	static int cnt = 1;

	switch(f)
	{
	case 0:
		fprintf(fout,"Case #%d: X won\n", cnt);
		break;

	case 1:
		fprintf(fout,"Case #%d: O won\n", cnt);
		break;

	case 2:
		fprintf(fout,"Case #%d: Draw\n", cnt);
		break;

	case 3:
		fprintf(fout,"Case #%d: Game has not completed\n", cnt);
		break;
	}

	cnt++;
}

void main(void)
{
	FILE *fin = fopen("A-large.in","r");
	fout = fopen("A-large.out","w");

	int i, j, n, src, t;
	char board[4][5];

	fscanf(fin,"%d",&n);
	printf("%d\n",n);

	while(n--)
	{
		for(i=0; i<4; i++)
			fscanf(fin, "%s",board[i]);
				
		// 가로
		for(i=0; i<4; i++)
		{
			src = 0;
			t = 0;
			for(j=0; j<4; j++)
			{
				if( board[i][j] == 'X' )	 src++;
				else if( board[i][j] == 'O') src--;
				else if( board[i][j] == 'T') t=1;
			}

			if( src == 4 || (src == 3 && t ) )
			{
				prn(0);
				break;
			}
			else if(src == -4 || (src == -3 && t) )
			{
				prn(1);
				break;
			}
		}
		if( i != 4 )
			continue;

		// 세로
		for(j=0; j<4; j++)
		{
			src = 0;
			t = 0;
			for(i=0; i<4; i++)
			{
				if( board[i][j] == 'X' )	 src++;
				else if( board[i][j] == 'O') src--;
				else if( board[i][j] == 'T') t=1;
			}

			if( src == 4 || (src == 3 && t ) )
			{
				prn(0);
				break;
			}
			else if(src == -4 || (src == -3 && t) )
			{
				prn(1);
				break;
			}
		}
		if( j != 4 )
			continue;

		// 대각선
		src = 0;
		t = 0;
		for(i=0,j=0; i<4; i++, j++)
		{

			if( board[i][j] == 'X' )	 src++;
			else if( board[i][j] == 'O') src--;
			else if( board[i][j] == 'T') t=1;
		}		
		if( src == 4 || (src == 3 && t ) )
		{
			prn(0);
			continue;
		}
		else if(src == -4 || (src == -3 && t) )
		{
			prn(1);
			continue;
		}
		
		src = 0;
		t = 0;
		for(i=0,j=3; i<4; i++, j--)
		{
			if( board[i][j] == 'X' )	 src++;
			else if( board[i][j] == 'O') src--;
			else if( board[i][j] == 'T') t=1;
		}		
		if( src == 4 || (src == 3 && t ) )
		{
			prn(0);
			continue;
		}
		else if(src == -4 || (src == -3 && t) )
		{
			prn(1);
			continue;
		}

		//Draw
		src=0;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				if(board[i][j] != '.')
					src++;

		if( src == 16 )
			prn(2);
		else
			prn(3);

	}
}