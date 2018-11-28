// googleJam_QP1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <vector>
#include <iostream>

using std::ifstream;
using std::vector;
using std::pair;
using std::cout;
using std::endl;

int TimeToPress(int lastAct, int now, int curPosition, int targetPosition)
{
	//how long has o been idle?
	int idle=now-lastAct;

	//time to move from last to here
	int time=abs(curPosition-targetPosition)+1;
	//subtract idle time
	time-=idle;
	//clamp it
	if (time<1) time=1;

	return time;
}

int _tmain(int argc, _TCHAR* argv[])
{	
	int caseCount=0;
	ifstream inFile("A-large.in");
	std::ofstream outFile("A-large.out.txt");

	inFile>>caseCount;

	for (int curCase=1; curCase<=caseCount; ++curCase)
	{
		int numSteps=0, numSeconds=0;
		vector<pair<char,int>> sequence;
		int orangePos=0, bluePos=0;
		int lastOrangeMove=0, lastBlueMove=0;
		int orangePosition=1, bluePosition=1;
		
		inFile>>numSteps;
		
		for (int curStep=0; curStep<numSteps; ++curStep)
		{
			char who;
			int buttonNumber;
			inFile>>who>>buttonNumber;
			if (who=='O')
			{		
				numSeconds+=TimeToPress(lastOrangeMove,numSeconds,orangePosition,buttonNumber);				
				lastOrangeMove=numSeconds;
				orangePosition=buttonNumber;
			}
			else
			{
				numSeconds+=TimeToPress(lastBlueMove,numSeconds,bluePosition,buttonNumber);
				lastBlueMove=numSeconds;
				bluePosition=buttonNumber;
			}
		}
		outFile<<"Case #"<<curCase<<": "<<numSeconds<<endl;
	}

	return 0;
}

