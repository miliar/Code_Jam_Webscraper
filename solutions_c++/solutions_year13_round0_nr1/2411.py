#include <iostream>
#include <string>
#include <fstream>
#include <string.h>
#include <stdio.h>
#include <ctype.h>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <stack>
#include <iomanip>
#include <math.h>
#include <map>
using namespace std;

#define LOCAL
#ifdef LOCAL  
    ifstream fin("D:/A-small-attempt0.in");  
    #define cin fin  
    ofstream fout("D:/output.txt");  
    #define cout fout   
#endif  

enum Status
{
	XWin,
	OWin,
	Draw,
	NotFinished
};

char ChessBoard[4][4];

Status Judge()
{
	bool notDraw = false;
	
	for(int i=0; i<4; i++)
	{
		int OCount = 0, XCount = 0, TCount = 0;
		for(int j=0; j<4; j++)
		{
			if(ChessBoard[i][j] == 'O')
				OCount++;
			else if(ChessBoard[i][j] == 'X')
				XCount++;
			else if(ChessBoard[i][j] == 'T')
				TCount++;	
		}
		if(OCount + TCount == 4)
			return OWin;
			
		if(XCount + TCount == 4)
			return XWin;
		
		if(XCount == 0 || OCount == 0)
			notDraw = true;
	}
	
	
	for(int j=0; j<4; j++)
	{
		int OCount = 0, XCount = 0, TCount = 0;
		for(int i=0; i<4; i++)
		{
			if(ChessBoard[i][j] == 'O')
				OCount++;
			else if(ChessBoard[i][j] == 'X')
				XCount++;
			else if(ChessBoard[i][j] == 'T')
				TCount++;
		}
		if(OCount + TCount == 4)
			return OWin;
			
		if(XCount + TCount == 4)
			return XWin;

		if(XCount == 0 || OCount == 0)
			notDraw = true;
	}
	
	int OCount = 0, XCount = 0, TCount = 0;
	for(int i=0; i<4; i++)
	{
		if(ChessBoard[i][i] == 'O')
			{
				OCount++;
			}
			else if(ChessBoard[i][i] == 'X')
			{
				XCount++;
			}
			else if(ChessBoard[i][i] == 'T')
			{
				TCount++;
			}
	}
	if(OCount + TCount == 4)
			return OWin;			
	if(XCount + TCount == 4)
			return XWin;
	if(XCount == 0 || OCount == 0)
			notDraw = true;
			
			
	OCount = 0; XCount = 0; TCount = 0;
	for(int i=0; i<4; i++)
	{
		if(ChessBoard[i][3-i] == 'O')
			{
				OCount++;
			}
			else if(ChessBoard[i][3-i] == 'X')
			{
				XCount++;
			}
			else if(ChessBoard[i][3-i] == 'T')
			{
				TCount++;
			}
	}
	if(OCount + TCount == 4)
			return OWin;			
	if(XCount + TCount == 4)
			return XWin;
	if(XCount == 0 || OCount == 0)
			notDraw = true;
	
	if(notDraw)
		return NotFinished;
	return Draw;
}

void print()
{
	for(int i=0; i<4; i++)
	{
		for(int j=0; j<4; j++)
		{
			cout << ChessBoard[i][j];
		}
		cout << endl;
	}
}

void printResult(int caseIndex, Status result)
{
	cout << "Case #" << caseIndex << ": "; 
	switch(result)
	{
		case XWin:
			cout << "X won" << endl;
			break;
		case OWin:
			cout << "O won" << endl;
			break;
		case Draw:
			cout << "Draw" << endl;
			break;
		case NotFinished:
			cout << "Game has not completed" << endl;
			break;
	}
}

int main()
{
	
	int caseNum; 
	cin >> caseNum;
	
	for(int i=0; i<caseNum; i++)
	{
		for(int j=0; j<4; j++)
		{
			cin >> ChessBoard[j];
			//string s; cin >> s;
			//for(int m=0; m<4; m++)
			//{
			//	ChessBoard[j][m] = s[m];
			//}
		}
		Status result = Judge();
		printResult(i+1, result);
	}
	
	
	
	//print();

#ifdef LOCAL     
    system("PAUSE");
#endif
    return 0;
}

