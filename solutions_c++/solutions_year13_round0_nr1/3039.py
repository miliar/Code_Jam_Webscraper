#include <iostream>
#include <fstream>
#include <string>

bool HasSideWon(char board[4][4], char side)
{
	if((board[0][0] == side || board[0][0] == 'T') &&
		(board[1][1] == side || board[1][1] == 'T') &&
		(board[2][2] == side || board[2][2] == 'T') &&
		(board[3][3] == side || board[3][3] == 'T'))
		return true;
	if((board[3][0] == side || board[3][0] == 'T') &&
		(board[2][1] == side || board[2][1] == 'T') &&
		(board[1][2] == side || board[1][2] == 'T') &&
		(board[0][3] == side || board[0][3] == 'T'))
		return true;

	for(int i = 0; i < 4; i++)
	{
		bool won = true;
		for(int j = 0; j < 4; j++)
			won &= (board[i][j] == side || board[i][j] == 'T');
		
		if(won) return true;

		won = true;
		for(int j = 0; j < 4; j++)
			won &= (board[j][i] == side || board[j][i] == 'T');
		if(won) return true;
	}

	return false;
}

int HasEmpty(char board[4][4])
{
	int count = 0;
	for(int i = 0; i < 4; i++)
		for(int j = 0; j < 4; j++)
			count += board[i][j] == '.' ? 1 : 0;

	return count > 0 ? true : false;
}

int main()
{
	std::ifstream in("A-large.in");
	std::ofstream out("out.txt");
	int n = 0;
	in >> n;
	
	char board[4][4] = {0};

	for(int i = 0; i < n; i++)
	{
		for(int j = 0; j < 4; j++)
			for(int k = 0; k < 4; k++)
				in >> board[j][k];

		out << "Case #" << i + 1 << ": ";

		if(HasSideWon(board, 'X'))
			out << "X won";
		else if(HasSideWon(board, 'O'))
			out << "O won";
		else if(!HasEmpty(board))
			out << "Draw";
		else
			out << "Game has not completed";

		out << std::endl;
	}	

	in.close();
	out.close();
	return 0;
}