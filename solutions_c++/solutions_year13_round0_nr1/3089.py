/*

 *
 */

#define XWON	0
#define OWON	1
#define DRAW	2
#define NCMP	3
 
#include <iostream>
#include <fstream>
#include <algorithm>
#include <stack>



using namespace std;

int testPad(char Pad[4][4])
{
	
	char first;
	
	// check rows
	bool RowWin = true;
	first = 0;
	for(int i = 0; i < 4; i++) {
		for(int j = 0; j < 4; j++) {
			if(Pad[i][j] == '.')				{ RowWin = false; break; }
			if(first == 0 && Pad[i][j] != 'T' && Pad[i][j] != '.')	first = Pad[i][j];
			else if(first == 0)					continue;
			
			
			if(first != Pad[i][j] && Pad[i][j] != 'T') {
				RowWin = false;
				break;
			}
		}
		if(RowWin && first != 0)	break;
		first = 0;
		RowWin = true;
	}

	if(RowWin && first == 'X')	return XWON;
	if(RowWin && first == 'O')	return OWON;
	
	
	// check cols
	bool ColWin = true;
	first = 0;
	for(int j = 0; j < 4; j++) {
		for(int i = 0; i < 4; i++) {
			if(Pad[i][j] == '.')				{ ColWin = false; break; }
			if(first == 0 && Pad[i][j] != 'T' && Pad[i][j] != '.')	first = Pad[i][j];
			else if(first == 0)					continue;
			
			
			if(first != Pad[i][j] && Pad[i][j] != 'T') {
				ColWin = false;
				break;
			}
		}
		if(ColWin && first != 0)	break;
		first = 0;
		ColWin = true;
	}
	
	if(ColWin && first == 'X')	return XWON; 
	if(ColWin && first == 'O')	return OWON;
	
	
	// check diagonals
	bool DiaWin = true;
	first = 0;
	for(int j = 0; j < 4; j++) {
		if(Pad[j][j] == '.')				{ DiaWin = false; break; }
		if(first == 0 && Pad[j][j] != 'T' && Pad[j][j] != '.')	first = Pad[j][j];
		else if(first == 0)					continue;
				
		if(first != Pad[j][j] && Pad[j][j] != 'T') {
			DiaWin = false;
			break;
		}
	}
	
	if(DiaWin && first == 'X')	return XWON;
	if(DiaWin && first == 'O')	return OWON;
	
	DiaWin = true;
	first = 0;		// first char in the row
	for(int j = 3; j >= 0; j--) {
		if(Pad[3-j][j] == '.')					{ DiaWin = false; break; }
		if(first == 0 && Pad[3-j][j] != 'T' && Pad[3-j][j] != '.')	first = Pad[3-j][j];
		else if(first == 0)						continue;
		
		
		if(first != Pad[3-j][j] && Pad[3-j][j] != 'T') {
			DiaWin = false;
			break;
		}
	}
		
	if(DiaWin && first == 'X')	return XWON;
	if(DiaWin && first == 'O')	return OWON;
	
	
	for(int i = 0; i < 4; i++)
		for(int j = 0; j < 4; j++)
			if(Pad[i][j] == '.') 
				return NCMP;
	
	return DRAW;		
}


int main()
{
	ifstream inf;
	ofstream outf;
	inf.open("A-large.in", ios::in);
	outf.open("output.txt");


	int T;
	int result;
	string line;
	char Pad[4][4];
	
	inf >> T;
	for(int k = 0; k < T; k++)
	{
		// get one test case
		for(int i = 0; i < 4; i++)
		{
			inf >> line;
			for(int j = 0; j < 4; j++)
				Pad[i][j] = line[j];
		}
		//inf >> line;		// empty line
		// finish getting one test case
		
		// test the pad
		int result = testPad(Pad);
		outf << "Case #" << (k+1) << ": ";
		
		if(result == XWON)
			outf << "X won";
		else if(result == OWON)
			outf << "O won";
		else if(result == DRAW)
			outf << "Draw";
		else
			outf << "Game has not completed";
	
		outf << endl;
		
		
	}


	inf.close();
	outf.close();
	return 0;
}
