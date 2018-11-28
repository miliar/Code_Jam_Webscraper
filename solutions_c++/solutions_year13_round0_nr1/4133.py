#include <iostream>
#include <fstream>

using namespace std;

ifstream input ("input.txt");
ofstream output ("output.txt");

void check(int number)
{
	bool empty = false;
	char grid [4][4];
	for(int i = 0;i < 4;i++)
	{
		for(int i2 = 0; i2 < 4;i2++)
		{
			input >> grid[i][i2];
			if(grid[i][i2] == '.') empty = true;

		}
	}
	bool owin = false;
	bool xwin = false;
	for(int i = 0;i < 4;i++)
	{
		bool o = true;
		bool x = true;
		for(int i2 = 0;i2 < 4;i2++)
		{
			if(grid[i][i2] != 'O' && grid[i][i2] != 'T') o = false;
			if(grid[i][i2] != 'X' && grid[i][i2] != 'T') x = false;
		}
		if(o) owin = true;
		if(x) xwin = true;
	}

	for(int i = 0;i < 4;i++)
	{
		bool o = true;
		bool x = true;
		for(int i2 = 0;i2 < 4;i2++)
		{
			if(grid[i2][i] != 'O' && grid[i2][i] != 'T') o = false;
			if(grid[i2][i] != 'X' && grid[i2][i] != 'T') x = false;
		}
		if(o) owin = true;
		if(x) xwin = true;
	}

	bool o = true;
	bool x = true;
	for(int i = 0;i<4;i++)
	{
		if(grid[i][i] != 'O' && grid[i][i] != 'T') o = false;
		if(grid[i][i] != 'X' && grid[i][i] != 'T') x = false;
	}
	if(o) owin = true;
	if(x) xwin = true;

	o = true;
	x = true;
	for(int i = 0;i<4;i++)
	{
		if(grid[i][3-i] != 'O' && grid[i][3-i] != 'T') o = false;
		if(grid[i][3-i] != 'X' && grid[i][3-i] != 'T') x = false;
	}
	if(o) owin = true;
	if(x) xwin = true;

	if(owin)
	output << "Case #" << number << ": O won\n";
	else if(xwin)
	output << "Case #" << number << ": X won\n";
	else if (empty)
	output << "Case #" << number << ": Game has not completed\n";
	else
	output << "Case #" << number << ": Draw\n";
}

int main()
{
	int T;
	input >> T;

	for(int i = 1;i<=T;i++)
	{
		check(i);
	}
    return 0;
}
