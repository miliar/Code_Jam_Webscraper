#include<iostream>
#include<cmath>
#include<stdio.h>
#include<string.h>
using namespace std;
char board[4][4];
const string state[4] = {"X won","O won","Draw","Game has not completed"};
int caseNum = 1;
int main()
{
	int T;
	FILE *input, *output;
	if ((input = fopen("test", "r")) == NULL )
	{
		printf("cannot open this file\n");
		exit(0);
	}
	output = fopen("A-small-attempt0.out","w");
	fscanf(input,"%d",&T);
	char temp;
	while(T--)
	{
		bool flag = false;					//true when find someone has won
		char win;
		bool ifDraw = false;
		temp = fgetc(input);				//assimilate the empty line (char 10 '')
		for(int i = 0;i < 4;i++)
		{
			int j = 0;
			while(j<4)
			{
				temp = fgetc(input);
				board[i][j] = temp;
				if(board[i][j] == '.'){ifDraw = true;}
				j++;
			}
			temp = fgetc(input);
		}
		
		for(int i = 0;i<4;i++)				//judging line
		{
			char start = board[i][0];
			if(start == '.'){continue;}
			int j;
			if(start == 'T'){start = board[i][1];j=2;}
			else{j = 1;}
			while(j<4)
			{
				if(board[i][j] == '.'){ifDraw = true;}
				if(board[i][j] == start || board[i][j] == 'T')
				{
					j++;
				}
				else
				{
					break;;
				}
			}
			if(j==4)
			{
				flag=true;
				win = start;
				break;
			}
		}
		if(!flag)
		{
			for(int col=0;col<4;col++)
			{
				char start = board[0][col];
				if(start == '.'){continue;}
				int row;
				if(start == 'T'){start = board[1][col];row=2;}
				else{row = 1;}
				while(row<4)
				{
					if(board[row][col] == '.'){ifDraw = true;}
					if(board[row][col] == start || board[row][col] == 'T')
					{
						row++;
					}
					else
					{
						break;
					}
				}
				if(row==4)
				{
					flag=true;
					win = start;
					break;
				}
			}
		}
		if(!flag)
		{
			char start = board[0][0];
			int j;
			if(start == 'T'){start = board[1][1];j=2;}
			else{j = 1;}
			while(j<4&&start!='.')
			{
				if(board[j][j]==start||board[j][j] == 'T')
				{
					j++;
				}
				else
				{
					break;
				}
			}
			if(j==4)
			{
				flag = true;
				win = start;
			}
			start = board[0][3];
			if(start == 'T'){start = board[1][2];j=2;}
			else{j = 1;}
			while(j<4&&start!='.')
			{
				if(board[j][3-j]==start||board[j][3-j]=='T')
				{
					j++;
				}
				else
				{
					break;
				}
			}
			if(j==4)
			{
				flag=true;
				win =start;
			}
		}
		if(flag)
		{
			if(win=='X')
			{
				fprintf(output,"Case #%d: %s\n",caseNum++,state[0].c_str());
			}
			else
			{
				fprintf(output,"Case #%d: %s\n",caseNum++,state[1].c_str());
			}
		}
		else
		{
			if(ifDraw)
			{
				fprintf(output,"Case #%d: %s\n",caseNum++,state[3].c_str());
			}
			else
			{
				fprintf(output,"Case #%d: %s\n",caseNum++,state[2].c_str());
			}
		}
	}
	fclose(output);
	system("pause");
	return 0;
}