#include <iostream>
#include <fstream>
using namespace std;
ifstream in ("tttt.in"); ofstream out ("tttt.out");

char board[4][4];

int main()
{
	int t;
	in >> t;
	for(int cs = 1; cs <=t; cs++)
	{
		bool xWon=false,oWon=false;
		bool hasSpaces = false;
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				in >> board[i][j];
				if(board[i][j]=='.')hasSpaces=true;
			}
			in.ignore();
		}
		in.ignore();
		//Main Diag
		int who = 0;
		int winLn = 0;
		for(int i = 0; i < 4; i++)
		{
			if(board[i][i]=='.')
			{
			    who==0;
			    break;
			}
			if(board[i][i]=='T')
			{
				winLn++;
				continue;
			}
			if(board[i][i]=='O')
			{
				if(who==2)
				{
					who=0;
					break;
				}
				winLn++;
				who=1;
			}
			if(board[i][i]=='X')
			{
				if(who==1)
				{
					who=0;
					break;
				}
				winLn++;
				who=2;
			}
		}
		if(who==1&&winLn==4)oWon=true;
		if(who==2&&winLn==4)xWon=true;
		//Sec Diag
		who=0,winLn=0;
		for(int i = 0; i < 4; i++)
		{
		    if(board[i][3-i]=='.')
			{
			    who==0;
			    break;
			}
			if(board[i][3-i]=='T')
			{
				winLn++;
				continue;
			}
			if(board[i][3-i]=='O')
			{
				if(who==2)
				{
					who=0;
					break;
				}
				winLn++;
				who=1;
			}
			if(board[i][3-i]=='X')
			{
				if(who==1)
				{
					who=0;
					break;
				}
				winLn++;
				who=2;
			}
		}
		if(who==1&&winLn==4)oWon=true;
		if(who==2&&winLn==4)xWon=true;
	//Lines
	for(int i = 0; i < 4; i++)
	{
		who=0,winLn=0;
		for(int j = 0; j < 4; j++)
		{
		    if(board[i][j]=='.')
			{
			    who==0;
			    break;
			}
			if(board[i][j]=='T')
			{
				winLn++;
				continue;
			}
			if(board[i][j]=='O')
			{
				if(who==2)
				{
					who=0;
					break;
				}
				winLn++;
				who=1;
			}
			if(board[i][j]=='X')
			{
				if(who==1)
				{
					who=0;
					break;
				}
				winLn++;
				who=2;
			}
		}
		if(who==1&&winLn==4)oWon=true;
		if(who==2&&winLn==4)xWon=true;
	}
	//Cols
	for(int i = 0; i < 4; i++)
	{
		who=0,winLn=0;
		for(int j = 0; j < 4; j++)
		{
		    if(board[j][i]=='.')
			{
			    who==0;
			    break;
			}
			if(board[j][i]=='T')
			{
				winLn++;
				continue;
			}
			if(board[j][i]=='O')
			{
				if(who==2)
				{
					who=0;
					break;
				}
				winLn++;
				who=1;
			}
			if(board[j][i]=='X')
			{
				if(who==1)
				{
					who=0;
					break;
				}
				winLn++;
				who=2;
			}
		}
		if(who==1&&winLn==4)oWon=true;
		if(who==2&&winLn==4)xWon=true;
	}
	if(hasSpaces==false&&!oWon&&!xWon)
	{
		out << "Case #" << cs << ": Draw\n";
		continue;
	}
	if(oWon&&xWon)
	{
		out << "Case #" << cs << ": Draw\n";
		continue;
	}
	if(oWon)
	{
		out << "Case #" << cs << ": O won\n";
		continue;
	}
	if(xWon)
	{
		out << "Case #" << cs << ": X won\n";
		continue;
	}
	out << "Case #" << cs << ": Game has not completed\n";
}
}
