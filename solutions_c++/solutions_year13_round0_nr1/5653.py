// Tic-Tac-Toe-Tomek.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include <fstream>
using namespace std;

char check(char p1,char p2,char p3,char p4)
{
	char p[4]={p1,p2,p3,p4};
	char s=0;
	for (int i=0;i<4;i++)
	{
		if(p[i]=='T')
		{
			continue;
		}

		if (p[i]=='.')
		{
			return 0;
		}

		if (s==0)
		{
			s=p[i];
		}
		else if (s!=p[i])
		{
			return 0;
		}
	}
	return s;
}


int _tmain(int argc, _TCHAR* argv[])
{
	fstream infile;
	fstream outfile;
	infile.open("c:\\A-small-attempt0.in",ios::in);
	outfile.open("c:\\A-small-out.txt",ios::out|ios::trunc );

	int T;
	infile>>T;
	char tmp;
	for(int t=0;t<T;t++)
	{
		
		char board[4][4]={0};
		int full=1;
		for (int i=0;i<4;i++)
		{
			for (int j=0;j<4;j++)
			{
				infile>>board[i][j];
				if (board[i][j]=='.')
				{
					full=0;
				}
			}
		}
		//std::cin>>tmp;

		int r=0;

		for (int i=0;i<4;i++)
		{
			r=check(board[i][0],board[i][1],board[i][2],board[i][3]);
			if (r!=0)
			{
				break;
			}
			r=check(board[0][i],board[1][i],board[2][i],board[3][i]);
			if (r!=0)
			{
				break;
			}
		}

		if (r==0)
		{
			
			r=check(board[0][0],board[1][1],board[2][2],board[3][3]);
			if (r==0)
			{
				r=check(board[0][3],board[1][2],board[2][1],board[3][0]);
			}
		}
		outfile<<"Case #"<<t+1<<": ";

		if(r!=0)
		{
			char str[2]={r,0};
			outfile<<str<<" won";
		}
		else if (full==1)
		{
			outfile<<"Draw";
		}
		else
		{
			outfile<<"Game has not completed";
		}
		outfile<<std::endl;

	}
	
	return 0;
}

