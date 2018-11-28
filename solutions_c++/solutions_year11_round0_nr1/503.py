#include <stdlib.h>
#include <fstream>
#include <iostream>
using namespace std;

#define INPUT_FILE "A-large.in"
#define OUTPUT_FILE "BotTrust.out"

int nTest;
ifstream input;	
ofstream output;

int oIndex;
int iIndex;
int oWait;
int iWait;
int total;
int nStep;

void Solve(int index)
{
	char c;
	int j;
	int dis;
	total = 0;
	oIndex = 1;
	iIndex = 1;
	oWait = 0;
	iWait = 0;
	input >> nStep;
	for (int i = 0; i < nStep; i++)
	{
		input >> c;
		input >> j;
		if (c == 'O')
		{
			dis = abs(j - oIndex);
			if (oWait < dis)
			{
				total += (dis - oWait);
				iWait += (dis - oWait);
			}
			oWait = 0;
			iWait ++;
			oIndex = j;
		}
		else
		{
			dis = abs( j - iIndex);
			if (iWait < dis)
			{
				total += (dis - iWait);
				oWait += (dis - iWait);
			}
			iWait = 0;
			oWait ++;
			iIndex = j;
		}
		total ++;
	}
	output << "Case #" << index + 1 << ": " << total << endl;
}

void main()
{
	input.open(INPUT_FILE);
	output.open(OUTPUT_FILE);
	input >> nTest;
	for (int i =0; i < nTest; i++)
		Solve(i);		
	input.close();
	output.close();
}