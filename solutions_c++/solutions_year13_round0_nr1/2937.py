#include<iostream>
#include<fstream>
#include<string>

using namespace std;

class Tile 
{
private:
	bool state[2];
	// 0 0  = blank
	// 0 1  = X
	// 1 0  = O
	// 1 1  = T
public:
	Tile()
	{
		state[0] = 0;
		state[1] = 0;
	}
	Tile(char c)
	{
		if(c=='.')
		{
			state[0] = 0;
			state[1] = 0;
		}
		else if(c=='X')
		{
			state[0] = 1;
			state[1] = 0;
		}
		else if(c=='O')
		{
			state[0] = 0;
			state[1] = 1;
		}
		else
		{
			state[0] = 1;
			state[1] = 1;
		}
	}
	void setTile(char c)
	{
		if(c=='.')
		{
			state[0] = 0;
			state[1] = 0;
		}
		else if(c=='X')
		{
			state[0] = 1;
			state[1] = 0;
		}
		else if(c=='O')
		{
			state[0] = 0;
			state[1] = 1;
		}
		else
		{
			state[0] = 1;
			state[1] = 1;
		}
	}
	bool checkX()
	{
		return state[0];
	}
	bool checkO()
	{
		return state[1];
	}
};

int main(void)
{
	fstream input("tictactoetomek.in", fstream::in);
	fstream output("tictactoetomek.out", fstream::out);
	int times;
	input >> times;
	char nextTile;
	Tile board[4][4];
	for(int casenum=0; casenum<times; casenum++)
	{
		input.ignore();
		for(int y=0;y<4;y++)
		{
			for(int x=0;x<4;x++)
			{
				nextTile = input.get();
				board[x][y].setTile(nextTile);
			}
			input.ignore();
		}

		//check rows
		bool evaluated = false;
		for(int y=0; y<4&&!evaluated; y++)
		{
			bool xWon = true, oWon = true;
			for(int x=0;x<4;x++)
			{
				if(!board[x][y].checkX())
					xWon = false;
				if(!board[x][y].checkO())
					oWon = false;
			}
			if(xWon)
			{
				evaluated = true;
				output << "Case #" << casenum+1 << ": X won" << endl;
			}
			else if(oWon)
			{
				evaluated = true;
				output << "Case #" << casenum+1 << ": O won" << endl;
			}
		}
		//check columns
		if(!evaluated)
		{
			for(int x=0; x<4&&!evaluated; x++)
			{
				bool xWon = true, oWon = true;
				for(int y=0;y<4;y++)
				{
					if(!board[x][y].checkX())
						xWon = false;
					if(!board[x][y].checkO())
						oWon = false;
				}
				if(xWon)
				{
					evaluated = true;
					output << "Case #" << casenum+1 << ": X won" << endl;
				}
				else if(oWon)
				{
					evaluated = true;
					output << "Case #" << casenum+1 << ": O won" << endl;
				}
			}
		}
		//diagonals
		//upper left-down right diagonal
		if(!evaluated)
		{
			bool xWon = true, oWon = true;
			for(int c=0;c<4&&!evaluated;c++)
			{
				if(!board[c][c].checkX())
					xWon = false;
				if(!board[c][c].checkO())
					oWon = false;
			}
			if(xWon)
			{
				evaluated = true;
				output << "Case #" << casenum+1 << ": X won" << endl;
			}
			else if(oWon)
			{
				evaluated = true;
				output << "Case #" << casenum+1 << ": O won" << endl;
			}
		}
		//upper right- lower left diagonal
		if(!evaluated)
		{
			bool xWon = true, oWon = true;
			for(int c=0;c<4&&!evaluated;c++)
			{
				if(!board[3-c][c].checkX())
					xWon = false;
				if(!board[3-c][c].checkO())
					oWon = false;
			}
			if(xWon)
			{
				evaluated = true;
				output << "Case #" << casenum+1 << ": X won" << endl;
			}
			else if(oWon)
			{
				evaluated = true;
				output << "Case #" << casenum+1 << ": O won" << endl;
			}
		}

		//No one won
		if(!evaluated)
		{
			//Check for an empty tile
			bool hasEmptyTile = false;
			for(int x=0;x<4;x++)
			{
				for(int y=0;y<4;y++)
				{
					if(!board[x][y].checkO()&&!board[x][y].checkX())
						hasEmptyTile = true;
				}
			}
			if(hasEmptyTile)
			{
				evaluated = true;
				output << "Case #" << casenum+1 << ": Game has not completed" << endl;
			}
			else
			{
				evaluated = true;
				output << "Case #" << casenum+1 << ": Draw" << endl;
			}
		}
	}
	return 0;
}