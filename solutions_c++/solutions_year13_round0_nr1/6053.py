#include <iostream>
#include <fstream>

using namespace std;

#define WIN				4

#define DRAW			2
#define NOTCOMPLETE		1
#define XWIN			8
#define OWIN			16

int GetStatus(char input[4][4]);

int Process(char input[4][4], char check);

int main()
{
	ifstream fin("C:\\Users\\KishoreVen\\Downloads\\A-large.in", ios::in);
	ofstream fout("output.out", ios::out);

	int t;

	int *results;

	fin>>t;

	results = new int[t];

	char input[4][4];

	for(int i = 0; i < t; i++)
	{
		for(int x = 0; x < 4; x++)
		{
			for(int y = 0; y < 4; y++)
			{
				fin>>input[x][y];				
			}
		}

		results[i] = GetStatus(input);
	}

	fin.close();

	for(int i = 0; i < t; i++)
	{
		fout<<"Case #"<<i + 1<<": ";
		if(results[i] == XWIN)
		{
			fout<<"X won"<<endl;
		}
		else if(results[i] == OWIN)
		{
			fout<<"O won"<<endl;
		}
		else if(results[i] == DRAW)
		{
			fout<<"Draw"<<endl;
		}
		else if(results[i] == NOTCOMPLETE)
		{
			fout<<"Game has not completed"<<endl;
		}
	}

	fout.close();

	return 0;
}


int GetStatus(char input[4][4])
{
	int result;

	char xInput[4][4];

	int emptyCount = 0;

	//Processing for X victory

	for(int x = 0; x < 4; x++)
	{
		for(int y = 0; y < 4; y++)
		{
			xInput[x][y] = input[x][y];

			if(input[x][y] == 'T')
			{
				xInput[x][y] = 'X';
			}
			else if(input[x][y] == '.')
			{
				emptyCount++;
			}
		}
	}

	result = Process(xInput, 'X');

	if(result == WIN)
	{
		return XWIN;
	}

	//Processing for O victory

	char yInput[4][4];

	for(int x = 0; x < 4; x++)
	{
		for(int y = 0; y < 4; y++)
		{
			yInput[x][y] = input[x][y];

			if(input[x][y] == 'T')
			{
				yInput[x][y] = 'O';
			}			
		}
	}

	result = Process(yInput, 'O');

	if(result == WIN)
	{
		return OWIN;
	}

	if(emptyCount == 0)
	{
		return DRAW;
	}

	return NOTCOMPLETE;
}


int Process(char input[4][4], char check)
{
	int result = NOTCOMPLETE;

	int xCount = 0, yCount = 0;

	//rows & columns
	for(int i = 0; i < 4; i++)
	{
		xCount = 0;
		yCount = 0;
		for(int j = 0; j < 4; j++)
		{
			if(input[i][j] == check)
			{
				xCount++;
			}
			if(input[j][i] == check)
			{
				yCount++;
			}
		}

		if(xCount == 4 || yCount == 4)
		{
			result = WIN;

			return result;
		}
	}

	
	if(input[0][0] == check && input[1][1] == check && input[2][2] == check && input[3][3] == check)
	{
		result = WIN;
	}
	else if(input[3][0] == check && input[2][1] == check && input[1][2] == check && input[0][3] == check)
	{
		result = WIN;
	}	

	return result;
}