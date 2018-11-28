#include <iostream>
#include <fstream>
#include <istream>

struct board
{
	char value[4][4];
	friend  std::istream& operator>> (std::istream& is, board& val)
	{
		for(int x = 0; x < 4; x++)
		{
			for(int y = 0; y < 4; y++)
			{
				is >> val.value[x][y];
			}
		}

		return is;
	}

	bool checkComplete()
	{
		for(int x = 0; x < 4; x++)
		{
			for(int y = 0; y < 4; y++)
			{
				if(value[x][y] == '.')
					return false;
			}
		}
		return true;
	}

	bool checkWinner(char w)
	{
		//line
		
		for(int x = 0; x < 4; x++)
		{
			bool ok = true;
			for(int y = 0; y < 4; y++)
			{
				if(value[x][y] != w && value[x][y] != 'T'){
					ok = false;
					break;
				}
			}
			if(ok)
				return ok;
		}

		for(int x = 0; x < 4; x++)
		{
			bool ok = true;
			for(int y = 0; y < 4; y++)
			{
				if(value[y][x] != w && value[y][x] != 'T'){
					ok = false;
					break;
				}
				
			}
			if(ok)
				return ok;
		}

		bool left = true, right = true;
		for(int i = 0; i < 4; i++)
		{
			if(value[i][i] != w && value[i][i] != 'T'){
				left = false;
			}

			if(value[3-i][i] != w && value[3-i][i] != 'T'){
				right = false;
			}
		}

		return left || right;
	}


};

int main()
{
	std::ifstream ifs("A-large.in");
	std::ofstream ofs("a.out");

	int number;

	ifs >> number;

	board test;
	for(int i = 0;i < number; i++)
	{
		ifs >> test;

		ofs << "Case #" << (i+1) << ": ";


		if(test.checkWinner('X'))
		{
			ofs << "X won";
		}
		else if(test.checkWinner('O'))
		{
			ofs << "O won";
		}
		else if(!test.checkComplete())
		{
			ofs << "Game has not completed";
		}
		else
		{
			ofs << "Draw";
		}

		ofs << std::endl;
	}

	return 0;
}