#include <iostream>
#include <vector>
#include <deque>
#include <map>
#include <string>
#include <utility>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <string.h>
#include <math.h>
using namespace std;

void docount(char c, int &nx, int &no, int &ndot, int &nt)
{
	switch(c)
	{
		case 'X':
                         nx++;
			 break;
		case 'O':
			no++;
			break;
		case '.':
			ndot++;
			break;
		case 'T':
			nt++;
			break;
		default:
			cout<<"wrong char:"<<c<<endl;
			break;
	}
}


string judge(char board[][4])
{
	bool iexistdot=false;
	for(int i=0;i<4;i++)//row
	{
		int nx=0,no=0,ndot=0,nt=0;
		for(int j=0;j<4;j++)
		{
			docount(board[i][j],nx,no,ndot,nt);
		}
		if(ndot>0)
		{
			iexistdot=true;
			continue;
		}
		else
		{
			if(nx==0)
				return "O won";
			else if(no==0)
				return "X won";
		}
	}
	for(int j=0;j<4;j++)//column
	{
		int nx=0,no=0,ndot=0,nt=0;
		for(int i=0;i<4;i++)
		{
			docount(board[i][j],nx,no,ndot,nt);
		}
		if(ndot>0)
		{
			iexistdot=true;
			continue;
		}
		else
		{
			if(nx==0)
				return "O won";
			else if(no==0)
				return "X won";
		}
		
	}
	
	{
		int nx=0,no=0,ndot=0,nt=0;
		for(int i=0;i<4;i++)
		{
			docount(board[i][i],nx,no,ndot,nt);
		}
		if(ndot>0)
		{
			iexistdot=true;
		}
		else
		{
			if(nx==0)
				return "O won";
			else if(no==0)
				return "X won";
		}
		
	}	
	{
		int nx=0,no=0,ndot=0,nt=0;
		for(int i=0;i<4;i++)
		{
			docount(board[i][3-i],nx,no,ndot,nt);
		}
		if(ndot>0)
		{
			iexistdot=true;
		}
		else
		{
			if(nx==0)
				return "O won";
			else if(no==0)
				return "X won";
		}
	}
	if(iexistdot==true)
		return "Game has not completed";
	else
		return "Draw";

}

int main() {
 
        int N;
        cin>>N;
        int count=1;
        char board[4][4];
        while(N--)
        {
                for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>board[i][j];
		

                cout<<"Case #"<<count++<<": "<<judge(board)<<endl;
         }



        return 0;
}
