#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <map>
#include <sstream>

using namespace std;

const int nSize = 4;

int CheckLine(vector<string>& vRows, int nStartRow, int nStartCol, int nRowAdv, int nColAdv, char& Result)
{
	int nEmpty = 0;
	int nX = 0;
	int nO = 0;
	int nT = 0;

	int i = 0;
	int j = 0;

	for( int i = 0; i < nSize; i++ )
	{
		switch(vRows[nStartRow][nStartCol])
		{
		case '.':
			nEmpty++;
			break;
		case 'X':
			nX++;
			break;
		case 'O':
			nO++;
			break;
		case 'T':
			nT++;
			break;
		}
		nStartRow += nRowAdv;
		nStartCol += nColAdv;

	}
	if( nX + nT == nSize )
		Result = 'X';
	else if( nO + nT == nSize )
		Result = 'O';

	return nEmpty;
}

int main()
{
	//ifstream in("A-small-attempt0.in");
    //ofstream out("A-small-attempt0.out");

	ifstream in("A-large.in");
    ofstream out("A-large.out");

	int iTasks;
	in >> iTasks;

	const int nMaxLines = 10;
	for( int iCount = 1; iCount <= iTasks; iCount++ )
	{
		string sRow;
		vector<string> vRows(nSize);
		for( int i = 0; i < nSize; i++ )
			in >> vRows[i];

		char Winner = '.';
		int nEmpty = 0;
		for( int i = 0; i < nMaxLines && Winner == '.'; i++ )
		{
			if( i < nSize )
			{
				nEmpty += CheckLine(vRows, i, 0, 0, 1, Winner);
			}
			else if( i < nSize * 2)
			{
				nEmpty += CheckLine(vRows, 0, i - nSize, 1, 0, Winner);
			}
			else if( i < nMaxLines - 1)
			{
				nEmpty += CheckLine(vRows, 0, 0, 1, 1, Winner);
			}
			else
			{
				nEmpty += CheckLine(vRows, 0, nSize-1, 1, -1, Winner);
			}
		}
		out << "Case #" << iCount << ": ";

		if( Winner != '.' )
		{
			out << Winner << " won" << endl;
		}
		else
		{
			if( nEmpty == 0 )
			{
				out << "Draw" << endl;
			}
			else
			{
				out << "Game has not completed" << endl;
			}


		}
		string s;
		//in >> s;
	}
	return 0;
}
