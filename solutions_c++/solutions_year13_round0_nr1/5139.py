#include <iostream>
#include <vector>
#include <algorithm>

std::string determine_winner(char board[4][4])
{
	bool X = false;
	bool O = false;
	bool completed = true;

	//check X axis
	for(int y = 0;y<4;y++)
	{
		bool x_temp = true;
		bool o_temp = true;
		for(int x = 0;x<4;x++)
		{
			if(board[y][x] == 'O')
				x_temp = false;
			if(board[y][x] == 'X')
				o_temp = false;
			if(board[y][x] == '.')
			{
				x_temp = false; o_temp = false; completed = false;
			}
		}
		X = X||x_temp;
		O = O||o_temp;
	}
	//check Y axis
	for(int x = 0;x<4;x++)
	{
		bool x_temp = true;
		bool o_temp = true;
		for(int y = 0;y<4;y++)
		{
			if(board[y][x] == 'O')
				x_temp = false;
			if(board[y][x] == 'X')
				o_temp = false;
			if(board[y][x] == '.')
			{
				x_temp = false; o_temp = false; completed = false;
			}
		}
		X = X||x_temp;
		O = O||o_temp;
	}
	//check diagonals
	{//top left to btm right
		bool x_temp = true;
		bool o_temp = true;
		for(int d = 0;d<4;d++)
		{
			if(board[d][d] == 'O')
				x_temp = false;
			if(board[d][d] == 'X')
				o_temp = false;
			if(board[d][d] == '.')
			{
				x_temp = false; o_temp = false; completed = false;
			}
		}
		X = X||x_temp;
		O = O||o_temp;
	}
	{//top left to btm right
		bool x_temp = true;
		bool o_temp = true;
		for(int d = 0;d<4;d++)
		{
			if(board[3-d][d] == 'O')
				x_temp = false;
			if(board[3-d][d] == 'X')
				o_temp = false;
			if(board[3-d][d] == '.')
			{
				x_temp = false; o_temp = false; completed = false;
			}
		}
		X = X||x_temp;
		O = O||o_temp;
	}



	if(X&&O)
		return "Draw";
	if(X)
		return "X won";
	if(O)
		return "O won";
	if(completed)
		return "Draw";
	return "Game has not completed";
}

int main()
{
	using namespace std;
	char board[4][4];
	int problems;
	cin>> problems;

	for(int i = 0;i<problems;i++)
	{
		//read 1 board, solve board, repeat
		for(int y = 0;y<4;y++)
			for(int x=0;x<4;x++)
				cin>>board[y][x];
		cout<<"Case #"<<i+1<<": "<<determine_winner(board).c_str()<<endl;
	}
	return 0;
}
