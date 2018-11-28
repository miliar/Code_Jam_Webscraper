// tictactoetomek.cpp : Defines the entry point for the console application.


//#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>

using namespace std;
char set[4][4];
char set1[4][4];
char winner = 'S';
void check(char look)
{
	if(set1[0][0] == look && set1[0][1] == look && set1[0][2] == look && set1[0][3] == look)
		winner = look;
	if(set1[1][0] == look && set1[1][1] == look && set1[1][2] == look && set1[1][3] == look)
		winner = look;
	if(set1[2][0] == look && set1[2][1] == look && set1[2][2] == look && set1[2][3] == look)
		winner = look;
	if(set1[3][0] == look && set1[3][1] == look && set1[3][2] == look && set1[3][3] == look)
		winner = look;
	if(set1[0][0] == look && set1[1][0] == look && set1[2][0] == look && set1[3][0] == look)
		winner = look;
	if(set1[0][1] == look && set1[1][1] == look && set1[2][1] == look && set1[3][1] == look)
		winner = look;
	if(set1[0][2] == look && set1[1][2] == look && set1[2][2] == look && set1[3][2] == look)
		winner = look;
	if(set1[0][3] == look && set1[1][3] == look && set1[2][3] == look && set1[3][3] == look)
		winner = look;
	if(set1[0][0] == look && set1[1][1] == look && set1[2][2] == look && set1[3][3] == look)
		winner = look;
	if(set1[3][0] == look && set1[2][1] == look && set1[1][2] == look && set1[0][3] == look)
		winner = look;

}
bool isEmpty()
{
	for(int q=0;q<4;q++)
	{
		for(int a=0;a<4;a++)
		{
			if(set[q][a] == '.')
				return false;
		}
	}
	return true;


}
int main()
{
	ofstream fout("problem.out");
	ifstream fin("problem.in");

	int num=0;
	fin >> num;

	for(int ua=1;ua<=num;ua++)
	{
		winner = 'S';
		for(int i=0;i<4;i++)
		{
			for(int k=0;k<4;k++)
			{
				fin >> set[i][k];
				set1[i][k] = set[i][k];
				
			}
			
		}
	

	
		for(int i=0;i<4;i++)
		{
			for(int k=0;k<4;k++)
			{
				if(set[i][k] == 'T')
					set1[i][k] = 'X';
			}
		}
	
	check('X');

	if(winner != 'X')
	{
		
			for(int i=0;i<4;i++)
			{
				for(int k=0;k<4;k++)
				{
					if(set[i][k] == 'T')
						set1[i][k] = 'O';
				}
			}
		
		check('O');
		if(winner == 'O')
		{
			fout << "Case #" << ua << ": O won\n";
		}
	}
	else
	{
		fout << "Case #" << ua << ": X won\n";
	}

		if(winner == 'S')
		{
			if(!isEmpty())
				fout << "Case #" << ua << ": Game has not completed\n";
			else
				fout << "Case #" << ua << ": Draw\n";
		}
		
	}
	
	return 0;
}

