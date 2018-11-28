#include <iostream>
#include <fstream>

using namespace std;

#define isO(A) ( A=='O' || A=='T' ? 1 : 0 )
#define isX(A) ( A=='X' || A=='T' ? 1 : 0 )

int checkHorizon(char data[4][5])
{
	char check;
	int Owin;
	int Xwin;
	
	for(int i=0; i<4; i++)
	{
		Owin = 1;
		Xwin = 1;

		for(int j=0; j<4; j++)
		{
			Owin = Owin * isO(data[i][j]);
			Xwin = Xwin * isX(data[i][j]);
		}

		if(Owin == 1)
			return 1;
		if(Xwin == 1)
			return 2;
	}

	return 0;
}

int checkVertical(char data[4][5])
{
	char check;
	int Owin;
	int Xwin;
	
	for(int i=0; i<4; i++)
	{
		Owin = 1;
		Xwin = 1;

		for(int j=0; j<4; j++)
		{
			Owin = Owin * isO(data[j][i]);
			Xwin = Xwin * isX(data[j][i]);
		}

		if(Owin == 1)
			return 1;
		if(Xwin == 1)
			return 2;
	}

	return 0;
}

int checkCross(char data[4][5])
{
	char check;
	int Owin;
	int Xwin;
	
	Owin = 1;
	Xwin = 1;

	for(int i=0; i<4; i++)
	{
		Owin = Owin * isO(data[i][i]);
		Xwin = Xwin * isX(data[i][i]);
	}

	if(Owin == 1)
		return 1;
	if(Xwin == 1)
		return 2;

	Owin = 1;
	Xwin = 1;

	for(int i=0; i<4; i++)
	{
		Owin = Owin * isO(data[i][3-i]);
		Xwin = Xwin * isX(data[i][3-i]);
	}

	if(Owin == 1)
		return 1;
	if(Xwin == 1)
		return 2;


	return 0;
}

int main()
{
	int N;
	char data[4][5];
	int result;
	int notend;
	char resultText[4][32] ={
		"Game has not completed",
		"O won",
		"X won",
		"Draw"
		
	};
	int T_X, T_Y;

	ifstream fin;
	ofstream fout;

	//fin = ifstream("input.txt");
	//fout = ofstream("output.txt");
	fin = ifstream(stdin);
	fout = ofstream(stdout);

	fin>>N;

	for(int count=1; count<=N; count++)
	{
		T_X = T_Y = -1;
		notend = 0;

		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				char temp;
				fin>>data[i][j];
				if(data[i][j] == 'T')
				{
					T_X = j;
					T_Y = i;
				}
				if(data[i][j] == '.')
					notend = 1;
			}
		}

		result = checkHorizon(data);
		if( !result)
			result = checkVertical(data);
		if( !result )
			result = checkCross(data);

		if(result == 0)
		{
			if(notend == 0)
			{
				result = 3;
			}
		}

		fout << "Case #" << count << ": " << resultText[ result ] << endl;
	}

	return 0;
}