// TicTacToeTomek.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <tchar.h>
#include <iostream>

using namespace std;

char *Results[4]= {
	"O won",
	"X won",
	"Draw",
	"Game has not completed"
};

enum _Game {
	_O=1,
	_X,
	_T,
	_D
};


int _tmain(int argc, _TCHAR* argv[])
{
	unsigned int T;
	char c;
	cin >> T;

	for(unsigned int i=0; i<T; i++)
	{
		bool bDotFound = false;
		_Game Game[4][4];
		for(unsigned int j=0; j<4; j++)
		{
			for(unsigned int k=0; k<4; k++)
			{
				cin >> c;
				switch (c)
				{
				case 'X':
					Game[j][k]=_X;
					break;
				case 'O':
					Game[j][k]=_O;
					break;
				case 'T':
					Game[j][k]=_T;
					break;
				default:
					Game[j][k]=_D;
					bDotFound = true;
					break;
				}
			}
		}


		{
			int Result=-1;
			bool bFound = false;

			for(int j=0; (j<4) && !bFound; j++)
			{
				if(Game[j][0]&Game[j][1] &&
					Game[j][0]&Game[j][2] &&
					Game[j][0]&Game[j][3])
				{
					switch(Game[j][0])
					{
					case _O:
						bFound = true;
						Result = 0;
						break;
					case _X:
						bFound = true;						
						Result = 1;
						break;
					}
				}
			}
			for(int k=0; (k<4) && !bFound; k++)
			{
				if(Game[0][k]&Game[1][k] &&
					Game[0][k]&Game[2][k] &&
					Game[0][k]&Game[3][k])
				{
					switch(Game[0][k])
					{
					case _O:
						bFound = true;
						Result = 0;
						break;
					case _X:
						bFound = true;
						Result = 1;
						break;
					}
				}
			}
			if(!bFound)
			{
				if(Game[0][0]&Game[1][1] &&
					Game[0][0]&Game[2][2] &&
					Game[0][0]&Game[3][3])
				{
					switch(Game[0][0])
					{
					case _O:
						bFound = true;
						Result = 0;
						break;
					case _X:
						bFound = true;
						Result = 1;
						break;
					}
				}
			}
			if(!bFound)
			{
				if(Game[0][3]&Game[1][2] &&
					Game[0][3]&Game[2][1] &&
					Game[0][3]&Game[3][0])
				{
					switch(Game[0][3])
					{
					case _O:
						bFound = true;
						Result = 0;
						break;
					case _X:
						bFound = true;
						Result = 1;
						break;
					}
				}
			}
			cout << "Case #" << i+1 << ": ";
			if(Result == -1)
			{
				if(bDotFound)
				{
					Result = 3;
				}
				else
				{
					Result = 2;
				}
			}
			cout << Results[Result] <<endl;
		}

	}

	return 0;
}

