#include <iostream>
#include <fstream>

using namespace std;

// Tic-Tac-Toe-Tomek - small

int main(void)
{
	ifstream input_file;
	input_file.open("round1/A-large.in");

	int games;
	char board[4][4];

	ofstream output_file;
	output_file.open("round1/output.out", std::ios_base::trunc);

	input_file >> games;
	for(int i = 0; i < games; i++)
	{
		bool has_empty = false;
		bool winner = false;
		for(int row = 0; row < 4; row++)
		{
			for(int column = 0; column < 4; column++)
			{
				input_file >> board[row][column];
				if(board[row][column] == '.') has_empty = true; 
			}
		}

		// check winner - rows
		for(int row = 0; !winner && row < 4; row++)
		{			
			char Check = board[row][0];
			if(Check == 'T') Check = board[row][1];
			if(Check == '.') continue;
			int column = 1;
			for(; !winner && column < 4; column++)
			{
				if(board[row][column] == 'T') continue;
				if(board[row][column] != Check) break;
			}
			if(column == 4)
			{
				winner = true;
				output_file << "Case #" << (i + 1) << ": " << Check << " won" << endl;
				break;
			}
		}
		if(winner) continue;

		// check winner - cols
		for(int column = 0; !winner && column < 4; column++)
		{			
			char Check = board[0][column];
			if(Check == 'T') Check = board[1][column];
			if(Check == '.') continue;
			int row = 1;
			for(; !winner && row < 4; row++)
			{
				if(board[row][column] == 'T') continue;
				if(board[row][column] != Check) break;
			}
			if(row == 4)
			{
				winner = true;
				output_file << "Case #" << (i + 1) << ": " << Check << " won" << endl;
				break;
			}			
		}
		if(winner) continue;

		// check diagonals
		{
			char Check = board[0][0];
			if(Check == 'T') Check = board[1][1];
			if(Check != '.')
			{
				int j = 1;
				for(; !winner && j < 4; j++)
				{
					if(board[j][j] == 'T') continue;
					if(board[j][j] != Check) break;					
				}
				if(j == 4)
				{
					winner = true;
					output_file << "Case #" << (i + 1) << ": " << Check << " won" << endl;
				}	
				if(winner) continue;
			}
		}
		{
			char Check = board[0][3];
			if(Check == 'T') Check = board[1][2];
			if(Check != '.')
			{
				int j = 1;
				for(; !winner && j < 4; j++)
				{
					if(board[j][3-j] == 'T') continue;
					if(board[j][3-j] != Check) break;					
				}
				if(j == 4)
				{
					winner = true;
					output_file << "Case #" << (i + 1) << ": " << Check << " won" << endl;				
				}	
				if(winner) continue;
			}
		}

		// no winner - check draw
		if(has_empty)
		{
			output_file << "Case #" << (i + 1) << ": Game has not completed" << endl;			
		}
		else
		{
			output_file << "Case #" << (i + 1) << ": Draw" << endl;			
		}
	}

	input_file.close();
	output_file.close();

	return 0;
}