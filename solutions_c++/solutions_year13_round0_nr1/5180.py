#include <stdio.h>
FILE *in = fopen("input.txt","r");
FILE *out = fopen("output.txt","w");
int ts;
char board[10][10];
int main()
{
	int i,j,k;
	fscanf(in,"%d",&ts);
	k=ts;
	while(ts--)
	{
		for(i=0;i<4;i++)
		{
			fscanf(in,"%s",board[i]);
		}
		int winner=0;
		int check=0;
		for(i=0;i<4;i++)
		{
			int cnt1=0,cnt2=0;
			for(j=0;j<4;j++)
			{
				if(board[i][j]=='O')
				{
					cnt1++;
				}
				if(board[i][j]=='X')
				{
					cnt2++;
				}
				if(board[i][j]=='T')
				{
					cnt1++;
					cnt2++;
				}
				if(board[i][j]=='.')
				{
					check=1;
				}
			}
			if(cnt1==4)
			{
				winner=1;
			}
			if(cnt2==4)
			{
				winner=2;
			}
			cnt1=0;
			cnt2=0;
			for(j=0;j<4;j++)
			{
				if(board[j][i]=='O')
				{
					cnt1++;
				}
				if(board[j][i]=='X')
				{
					cnt2++;
				}
				if(board[j][i]=='T')
				{
					cnt1++;
					cnt2++;
				}
			}
			if(cnt1==4)
			{
				winner=1;
			}
			if(cnt2==4)
			{
				winner=2;
			}
			cnt1=0;
			cnt2=0;
		}
			int cnt11=0,cnt22=0;
		for(i=0;i<4;i++)
		{
			if(board[i][i]=='O')
			{
				cnt11++;
			}
			if(board[i][i]=='X')
			{
				cnt22++;
			}
			if(board[i][i]=='T')
			{
				cnt11++;
				cnt22++;
			}	
			if(cnt11==4)
			{
				winner=1;
				break;
			}
			if(cnt22==4)
			{
				winner=2;
				break;
			}
		}
		cnt11=0,cnt22=0;
		for(i=0;i<4;i++)
		{
			if(board[3-i][i]=='O')
			{
				cnt11++;
			}
			if(board[3-i][i]=='X')
			{
				cnt22++;
			}
			if(board[3-i][i]=='T')
			{
				cnt11++;
				cnt22++;
			}	
			if(cnt11==4)
			{
				winner=1;
				break;
			}
			if(cnt22==4)
			{
				winner=2;
				break;
			}
		}
		if(winner==1)
		{
			fprintf(out,"Case #%d: O won\n",k-ts);
		}
		if(winner==2)
		{
			fprintf(out,"Case #%d: X won\n",k-ts);
		}
		if(winner==0)
		{
			if(check==1)
			{
				fprintf(out,"Case #%d: Game has not completed\n",k-ts);
			}
			else
			{
				fprintf(out,"Case #%d: Draw\n",k-ts);
			}
		}
	}
	return 0;
}