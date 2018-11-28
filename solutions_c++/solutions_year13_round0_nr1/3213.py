/*
 * sola.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: ben
 */

//============================================================================
// Name        : jam_test.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <fstream>
//#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

#define X_WON "X won"
#define O_WON "O won"
#define DRAW "Draw"
#define NOT_COMP "Game has not completed"

int main(int argc, char** argv)
{

	if(argc!=3)
	{
		cout << "Usage:" << endl;
		cout << "jam_test infile outfile" << endl;
		return 0;
	}

	ifstream infile(argv[1]);
	ofstream outfile(argv[2]);

	if(!infile)
		cout << "Input file open error!" << endl;

	if(!outfile)
		cout << "Output file open error!" << endl;

	int nCase;

	char ch;
	int i,j, ti, tj;
	bool notComp = false;
	char data[4][4], dataR[4][4];
	short testValueX = 0;
	short testValueXR = 0;
	short testValueO = 0;
	short testValueOR = 0;
	char winner = 'N';

	infile >> nCase ;
	//cout << "Case Num:" << nCase << endl;

	for(int iCase=0; iCase<nCase; iCase++)
	{
		cout << "Case #" << iCase+1 << ": " << endl;
		outfile << "Case #" << iCase+1 << ": ";

		notComp = false;
		winner = 'N';
		testValueX = testValueXR = testValueO = testValueOR = 0;
		ti = tj = -1;

		for(i=0; i<4; i++)
		{
			for(j=0; j<4; j++)
			{
				infile >> ch;
				data[i][j] = dataR[j][i] = ch;

				if(ch == '.')
				{
					notComp = true;
				}
				else if(ch == 'T')
				{
					ti = i;
					tj = j;
					testValueX |= (1<<(i*4+j));
					testValueXR |= (1<<(j*4+i));
					testValueO |= (1<<(i*4+j));
					testValueOR |= (1<<(j*4+i));
				}
				else if( ch == 'X')
				{
					testValueX |= (1<<(i*4+j));
					testValueXR |= (1<<(j*4+i));
				}
				else //if( ch == 'O')
				{
					testValueO |= (1<<(i*4+j));
					testValueOR |= (1<<(j*4+i));
				}

				//cout << ch;
			}
			//cout << endl;
		}

		for(i=0; i<4; i++)
		{
			if( ((0xf<<i*4) & testValueX) == (0xf<<i*4))
			{
				winner = 'X';
				break;
			}
			else if( ((0xf<<i*4) & testValueO) == (0xf<<i*4))
			{
				winner = 'O';
				break;
			}
			else if( ((0xf<<i*4) & testValueXR) == (0xf<<i*4))
			{
				winner = 'X';
				break;
			}
			else if( ((0xf<<i*4) & testValueOR) == (0xf<<i*4))
			{
				winner = 'O';
				break;
			}
		}

		//test diagonal
		if(winner != 'X' && winner !='O')
		{
			if(ti != -1)
				data[ti][tj] = 'X';
			//test diagonal
			if( (data[0][0] & data[1][1] & data[2][2] & data[3][3] & 'X') == 'X'
				|| (data[0][3] & data[1][2] & data[2][1] & data[3][0] & 'X') == 'X')
				winner = 'X';

			if(ti != -1)
				data[ti][tj] = 'O';
			if( (data[0][0] & data[1][1] & data[2][2] & data[3][3] & 'O') == 'O'
				|| (data[0][3] & data[1][2] & data[2][1] & data[3][0]) & 'O' == 'O')
				winner = 'O';
		}

		if(winner == 'X')
		{
			outfile << X_WON << endl;
			//cout << X_WON << endl;
		}
		else if(winner == 'O')
		{
			outfile << O_WON << endl;
			//cout << O_WON << endl;
		}
		else if(notComp)
		{
			outfile << NOT_COMP << endl;
			//cout << NOT_COMP << endl;

		}
		else
		{
			outfile << DRAW << endl;
			//cout << DRAW << endl;
		}

		//outfile << count << endl;
		//outfile << endl;

	}
	outfile << endl;

	return 0;
}



