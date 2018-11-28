// ProbA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "fstream"

#define INFILE "A-small-attempt0.in"
#define OUTFILE "A-small.out"

using namespace std;

char mat[4][4];
bool isFree;
bool explore(int i, int j, int dirx, int diry, char &won)
{
	for (int index=0; index<3; index++)
	{
		switch (mat[i+dirx*index][j+diry*index])
		{
		case '.':
			return false;
			break;
		case 'T':

			break;
		case 'O':
			if (mat[i+dirx*(index+1)][j+diry*(index+1)] == 'X')
				return false;
			if (mat[i+dirx*(index+1)][j+diry*(index+1)] == '.')
				return false;
			won = 'O';
			break;
		case 'X':
			if (mat[i+dirx*(index+1)][j+diry*(index+1)] == 'O')
				return false;
			if (mat[i+dirx*(index+1)][j+diry*(index+1)] == '.')
				return false;
			won = 'X';			 
			break;
		}
	}
	return true;
}

int _tmain(int argc, _TCHAR* argv[])
{
	char str[1000];
	char won;
	ifstream infile(INFILE);
	ofstream outfile(OUTFILE);
	int t;
	infile>>t;
	infile.getline(str,1000);
	for (int i=0; i<t; i++)
	{
		isFree = false;
		for (int j=0; j<4; j++)
		{
			for (int k=0; k<4; k++)
			{
				infile>>mat[j][k];
				if (mat[j][k] == '.')
					isFree = true;
			}
			infile.getline(str,1000);
		}
		infile.getline(str,1000);
		
		outfile <<"Case #"<<(i+1)<<": ";
		
		if (explore(0,0,0,1,won)) 
		{			
			outfile <<won<<" won\n";
		}
		else
			if (explore(0,0,1,1,won))
			{
				outfile <<won<<" won\n";
			}
			else
				if (explore(0,0,1,0,won))
				{
					outfile <<won<<" won\n";
				}
				else
					if (explore(0,1,1,0,won))
					{
						outfile <<won<<" won\n";
					}
					else
						if (explore(0,2,1,0,won))
						{
							outfile <<won<<" won\n";
						}
						else
							if (explore(0,3,1,0,won))
							{
								outfile <<won<<" won\n";
							}
							else
								if (explore(0,3,1,-1,won))
								{
									outfile <<won<<" won\n";
								}
								else
									if (explore(1,0,0,1,won))
									{
										outfile <<won<<" won\n";
									}
									else
										if (explore(2,0,0,1,won))
										{
											outfile <<won<<" won\n";
										}
										else
											if (explore(3,0,0,1,won))
											{
												outfile <<won<<" won\n";
											}
											else
												if (isFree)
													outfile <<"Game has not completed\n";
												else
													outfile <<"Draw\n";
	}

	infile.close();
	outfile.close();
	return 0;
}

