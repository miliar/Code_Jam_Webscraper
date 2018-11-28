#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <stdlib.h>
using namespace std;

#define GRID_DIM 4

void printWinner(char winner, int testCaseNum)
{
		cout << "Case #" << testCaseNum << ": " << winner << " won" <<endl;
//		exit(0);
}

char winnerCheckHorVer(char grid[][GRID_DIM], int row0Col1)
{
	int x=0;
	int o=0;
	int dots=0;
	int t=0;

	char elem;
	for(int i=0; i<GRID_DIM; i++)
	{
		x=0; o=0; t=0;
		for(int j=0; j<GRID_DIM; j++)
		{
			if(row0Col1==0)
				elem = grid[i][j];
			else
				elem = grid[j][i];

			if(elem=='X') x++;
			if(elem=='O') o++;
			if(elem=='.') dots++;
			if(elem=='T') t++;
		}

		if(x == GRID_DIM || (x == GRID_DIM-1 && t==1) )
			return 'X';
		if(o == GRID_DIM || (o == GRID_DIM-1 && t==1) )
			return 'O';
	}
	if(dots>0)
		return 'n';
	else
		return '-';
}

char winnerCheckDiag(char grid[][GRID_DIM], int lead0nonlead1)
{
	int x=0;
	int o=0;
	int dots=0;
	int t=0;

	char elem;
	for(int i=0; i<GRID_DIM; i++)
	{
		if(lead0nonlead1 == 0)
			elem = grid[i][i];
		else
			elem = grid[i][GRID_DIM-1-i];

		if(elem=='X') x++;
		if(elem=='O') o++;
		if(elem=='.') dots++;
		if(elem=='T') t++;
	}

	if(x == GRID_DIM || (x == GRID_DIM-1 && t==1) )
		return 'X';
	if(o == GRID_DIM || (o == GRID_DIM-1 && t==1) )
		return 'O';

	return '-';
}

int main()
{
	string line;
	int numtc;
	ifstream myfile1 ("A-large.in");
//	ifstream myfile1 ("input.txt");
	if (myfile1.is_open())
	{
		getline (myfile1,line);
		numtc = atoi(line.c_str());
	}

	char grid[GRID_DIM][GRID_DIM];
	char temp[4];
	ifstream myfile ("A-large.in");
//	ifstream myfile ("input.txt");
	getline (myfile,line);
	for(int testCaseNum=1; testCaseNum <= numtc; testCaseNum++)
	{
		if (myfile.is_open())
		{
			int i=0;
			while ( myfile.good() )
			{
				getline (myfile,line);
				if(line=="") break;
				strcpy(temp, line.c_str());
				for(int j=0; j<GRID_DIM; j++) grid[i][j] = temp[j];
				i++;
			}
		}


		char c1 = winnerCheckHorVer(grid, 0);
		if(c1 != '-' && c1 != 'n')
		{
			printWinner(c1, testCaseNum);
			continue;
		}
		char c2 = winnerCheckHorVer(grid, 1);
		if(c2 != '-' && c2 != 'n')
		{
			printWinner(c2, testCaseNum);
			continue;
		}
		char c3 = winnerCheckDiag(grid, 0);
		if(c3 != '-' && c3 != 'n')
		{
			printWinner(c3, testCaseNum);
			continue;
		}
		char c4 = winnerCheckDiag(grid, 1);
		if(c4 != '-' && c4 != 'n')
		{
			printWinner(c4, testCaseNum);
			continue;
		}

		else if(c1 == 'n')
			cout << "Case #" << testCaseNum << ": Game has not completed" << endl;
		else
			cout << "Case #" << testCaseNum << ": Draw" << endl;
		 
	}
	myfile.close();
	return 0;
}

