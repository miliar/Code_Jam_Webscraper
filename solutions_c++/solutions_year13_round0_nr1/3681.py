#include <iostream>
#include <string>
#include <fstream>

using namespace std;

char tablero[4][4];

bool checkLinea(int l, char color)
{
	for(int i = 0; i < 4; i++)
		if(tablero[l][i] != color && tablero[l][i] != 'T')
			return false;
	return true;
}
bool checkColumna(int l, char color)
{
	for(int i = 0; i < 4; i++)
		if(tablero[i][l] != color && tablero[i][l] != 'T')
			return false;
	return true;
}
bool checkDiag1(char color)
{
	for(int i = 0; i < 4; i++)
		if(tablero[i][i] != color && tablero[i][i] != 'T')
			return false;
	return true;
}
bool checkDiag2(char color)
{
	for(int i = 0; i < 4; i++)
		if(tablero[3-i][i] != color && tablero[3-i][i] != 'T')
			return false;
	return true;
}
bool checkFin()
{
	for(int i = 0; i < 4; i++)
		for(int j = 0; j < 4; j++)
			if(tablero[i][j] == '.')
				return false;
	return true;
}

bool checkColor(char color)
{
	for(int i = 0; i < 4; i++)
	{
		if(checkLinea(i, color))
			return true;
		if(checkColumna(i, color))
			return true;
	}
	if(checkDiag1(color))
		return true;
	if(checkDiag2(color))
		return true;
	return false;
}

int main()
{
	ifstream fin("a-l.in");
	ofstream fout("a-l.out");
	
	int t;
	fin >> t;
	
	for(int j = 0; j < t; j++)
	{
		fout << "Case #" << j+1 << ": ";
		for(int i = 0; i < 4; i++)
		{
			for(int k = 0; k < 4; k++)
			{
				char c;
				fin >> c;
				tablero[i][k] = c;
			}
		}
		if(checkColor('X'))
			fout << "X won" << endl;
		else if(checkColor('O'))
			fout << "O won" << endl;
		else if(!checkFin())
			fout << "Game has not completed" << endl;
		else
			fout << "Draw" << endl;
	}
	
	return 0;
	
}
