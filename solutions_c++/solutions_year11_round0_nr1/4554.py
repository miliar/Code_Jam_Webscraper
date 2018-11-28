#include <iostream>
#include <fstream>
#include <stdio.h>
using namespace std;

struct Button
{
	char color;
	int number;
	bool isPushed;
};

int getInput( Button buttons[] , ifstream &inFile);
int getSeconds( int numButtons , Button buttons[]);
int doAction ( Button buttons[] , int buttonNum , int numButtons, char color , int position);
void output( int seconds , int caseNum , ofstream &outFile);

int main()
{
	ifstream inFile;
	ofstream outFile;
	int numCases;
	int seconds;
	int numButtons;
	Button buttons[100];
	
	outFile.open("Qual-A-Large.out");
	if (!outFile.good())
		outFile.clear();
	if (!outFile.is_open())
	{
		fopen("Qual-A-Large.out","w");
		outFile.open("Qual-A-Large.out");
	}
	
	inFile.open("A-large.in");
	inFile >> numCases;

	if (!inFile.is_open());
	else
	{
		for ( int caseNum = 1 ; caseNum <= numCases ; caseNum++)
		{
			numButtons = getInput( buttons , inFile);
			seconds = getSeconds( numButtons , buttons);
			output( seconds , caseNum , outFile);
		}
	}

	return 0;
}

int getInput( Button buttons[] , ifstream &inFile)
{
	int numButtons;

	inFile >> numButtons;
	for ( int x = 0 ; x < numButtons ; x++ )
	{
		inFile >> buttons[x].color >> buttons[x].number;
		buttons[x].isPushed = false;
	}

	return numButtons;
}

int getSeconds( int numButtons , Button buttons[])
{
	int seconds = -1;
	int orangePosition = 0;
	int bluePosition = 0;

	for ( int x = 0 ; x < numButtons ; x++ )
	{
		while ( !buttons[x].isPushed )
		{
			orangePosition = doAction( buttons , x , numButtons , 'O' , orangePosition);
			bluePosition = doAction( buttons , x , numButtons , 'B' , bluePosition);
			seconds++;
		}
	}

	return seconds;
}

int doAction( Button buttons[] , int buttonNum , int numButtons , char color , int position)
{
	if ( color == buttons[buttonNum].color )
	{
		if ( position == buttons[buttonNum].number )
		{
			buttons[buttonNum].isPushed = true;
			return position;
		}
		else if ( position < buttons[buttonNum].number )
		{
			return position + 1;
		}
		else
		{
			return position - 1;
		}
	}
	else
	{
		for (; buttonNum < numButtons ; buttonNum++ )
		{
			if ( color == buttons[buttonNum].color )
			{
				if ( position == buttons[buttonNum].number )
				{
					return position;
				}
				else if ( position < buttons[buttonNum].number)
				{
					return position + 1;
				}
				else 
				{
					return position - 1;
				}
			}
		}
		return position; 
	}
}

void output( int seconds , int caseNum , ofstream &outFile)
{
	outFile << "Case #" << caseNum << ": " << seconds << endl;
}