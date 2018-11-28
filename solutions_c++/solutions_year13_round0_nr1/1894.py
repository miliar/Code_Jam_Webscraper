// GoogleCodeJam_A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>

#define MAX_SIZE 4

using namespace std;

ifstream fin("D:\\Input.in");
ofstream fout("D:\\Output.txt");

int T;
char board[MAX_SIZE][MAX_SIZE];

char checkGame() //returns 'X', 'O', 'D', or 'I'
{
	bool open = false;
	for(int q = 0; q < MAX_SIZE; q++)
	{
		int xcount = 0, ocount = 0, tcount = 0;
		for(int w = 0; w < MAX_SIZE; w++)
		{
			if(board[q][w] == 'X') xcount++;
			else if(board[q][w] == 'O') ocount++;
			else if(board[q][w] == 'T') tcount++;
			else open = true;
		}
		if(xcount == 4 || (xcount == 3 && tcount == 1)) return 'X';
		else if(ocount == 4 || (ocount == 3 && tcount == 1)) return 'O';
	}

	for(int q = 0; q < MAX_SIZE; q++)
	{
		int xcount = 0, ocount = 0, tcount = 0;
		for(int w = 0; w < MAX_SIZE; w++)
		{
			if(board[w][q] == 'X') xcount++;
			else if(board[w][q] == 'O') ocount++;
			else if(board[w][q] == 'T') tcount++;
			else open = true;
		}
		if(xcount == 4 || (xcount == 3 && tcount == 1)) return 'X';
		else if(ocount == 4 || (ocount == 3 && tcount == 1)) return 'O';
	}

	int xcount = 0, ocount = 0, tcount = 0;
	for(int w = 0; w < MAX_SIZE; w++)
	{
		if(board[w][w] == 'X') xcount++;
		else if(board[w][w] == 'O') ocount++;
		else if(board[w][w] == 'T') tcount++;
		else open = true;
	}
	if(xcount == 4 || (xcount == 3 && tcount == 1)) return 'X';
	else if(ocount == 4 || (ocount == 3 && tcount == 1)) return 'O';

	xcount = 0, ocount = 0, tcount = 0;
	for(int w = 0; w < MAX_SIZE; w++)
	{
		if(board[3 - w][w] == 'X') xcount++;
		else if(board[3 - w][w] == 'O') ocount++;
		else if(board[3 - w][w] == 'T') tcount++;
		else open = true;
	}
	if(xcount == 4 || (xcount == 3 && tcount == 1)) return 'X';
	else if(ocount == 4 || (ocount == 3 && tcount == 1)) return 'O';

	if(open) return 'I';
	else return 'D';
}

int main()
{
	fin >> T;
	for(int i = 0; i < T; i++)
	{
		for(int j = 0; j < MAX_SIZE; j++) for(int k = 0; k < MAX_SIZE; k++) fin >> board[j][k];
		char comparchar = checkGame();
		if(comparchar == 'X') fout << "Case #" << i + 1 << ": " << "X won" << "\n";
		else if(comparchar == 'O') fout << "Case #" << i + 1 << ": " << "O won" << "\n";
		else if(comparchar == 'D') fout << "Case #" << i + 1 << ": " << "Draw" << "\n";
		else fout << "Case #" << i + 1 << ": " << "Game has not completed" << "\n";
	}
	return 0;
}