#include<cstdio>
#include<algorithm>

using namespace std;

int t;
char board[5][5];
int score_row[3] = {0};
int score_col[3] = {0};
int score_lcross[3] = {0};
int score_rcross[3] = {0};

int main()
{
	int round,i,j,k;
	bool found = false;
	bool dot  =false;
	bool xwin = false;
	bool ywin = false;
	
	freopen("A-large.in","r",stdin);
	freopen("2.txt","w",stdout);
	scanf("%d",&t);
	
	for(round = 0 ; round < t ;round++)
	{
		found =false;
		for(i = 0 ; i < 4 ; i++)
		{
				scanf("%s",board[i]);	
		}	
				
		xwin = false;
	    ywin = false;
	    dot =false;
	    score_lcross[0] = 0;
	    score_lcross[1] = 0;
	    score_lcross[2] = 0;
	    
	    score_rcross[0] = 0;
	    score_rcross[1] = 0;
	    score_rcross[2] = 0;
	    
		for(i = 0 ; i < 4 ; i++)
		{
			score_row[0] = 0;
			score_row[1] = 0;
			score_row[2] = 0;
			
			score_col[0] = 0;
			score_col[1] = 0;
			score_col[2] = 0;
			
			for(j = 0 ; j < 4 ; j++)
			{
				if(board[i][j] == 'X')
					score_row[0]++;
				else if(board[i][j] == 'O')
					score_row[1]++;
				else if(board[i][j] =='T')
					score_row[2]++;
				else
					dot = true;
					
				if(board[j][i] == 'X')
					score_col[0]++;
				else if(board[j][i] == 'O')
					score_col[1]++;
				else if(board[j][i] =='T')
					score_col[2]++;
				else	
					dot = true;
			}
			
			if(board[i][i] == 'X')
					score_rcross[0]++;
			else if(board[i][i] == 'O')
					score_rcross[1]++;
			else if(board[i][i] =='T')
					score_rcross[2]++;
					
			if(board[i][3-i] == 'X')
					score_lcross[0]++;
			else if(board[i][3-i] == 'O')
					score_lcross[1]++;
			else if(board[i][3-i] =='T')
					score_lcross[2]++;
			
			// checking
					
			if(score_row[0] == 4 || score_row[0] + score_row[2] == 4)
					xwin =true;
			else if(score_row[1] == 4 || score_row[1] + score_row[2] == 4)
					ywin = true;
					
			if(score_col[0] == 4 || score_col[0] + score_col[2] == 4)
					xwin =true;
			else if(score_col[1] == 4 || score_col[1] + score_col[2] == 4)
					ywin = true;
								
			if(xwin)
			{
				printf("Case #%d: X won\n",round+1);
				break;
			}
			else if(ywin)
			{
				printf("Case #%d: O won\n",round+1);
				break;
			}
			
		}
		
		if(xwin == false && ywin == false)
		{
			if(score_lcross[0] == 4 || score_lcross[0] + score_lcross[2] == 4)
					xwin =true;
			else if(score_lcross[1] == 4 || score_lcross[1] + score_lcross[2] == 4)
					ywin = true;
					
			if(score_rcross[0] == 4 || score_rcross[0] + score_rcross[2] == 4)
					xwin =true;
			else if(score_rcross[1] == 4 || score_rcross[1] + score_rcross[2] == 4)
					ywin = true;
			
				if(xwin)
				{
					printf("Case #%d: X won\n",round+1);
				}
				else if(ywin)
				{
					printf("Case #%d: O won\n",round+1);
				}
				else
				{
					if(!dot)
						printf("Case #%d: Draw\n",round+1);
					else
						printf("Case #%d: Game has not completed\n",round+1);
				}
		}
		
		
		
		
	}
	return 0;
}
