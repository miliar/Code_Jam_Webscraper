#include "RoboData.h"
#include <iostream>

RoboData::RoboData(void):curPosition(1), curState(0)
{
}

RoboData::~RoboData(void)
{
}

void RoboData::addData(int whichButon)
{
	int numberOfMoves= (whichButon-curPosition);
	int incre = numberOfMoves <0?-1:1; 
	while(numberOfMoves != 0)
	{
		states.push_back(1);
		curPosition+=incre;
		numberOfMoves-=incre;
	}
	states.push_back(2);
}

unsigned RoboData::getState()
{
	if(curState < states.size()) 
	return states[curState];
	else
		return 0;
}

unsigned RoboData::getNextState()
{
	if(curState < states.size()) 
	return states.at(curState++);
	else
		return 0;
}

unsigned RoboData::numberOfMoves() const
{
	return states.size();
}

void RoboData::moveStates(int &totTime, RoboData& bRobo)
{
	if(getState() == 2) // both push 
	{	
		if(bRobo.getState() == 1)
		{
			bRobo.getNextState();
		}
		++totTime;	
		getNextState();				
	}
	else if(getState() == 1) // move both push 
	{	
		if(bRobo.getState() == 1)
		{
			bRobo.getNextState();
		}
		++totTime;	
		getNextState();	
		moveStates(totTime, bRobo);
	}
	else
	{
		++totTime;
		getNextState();
		bRobo.getNextState();
		moveStates(totTime, bRobo);				
	}
}

void RoboData::dumpStates(const int& type)
{
	std::vector<unsigned>::iterator begIter = states.begin();
	std::vector<unsigned>::iterator endIter = states.end();
	for (;begIter!= endIter; ++begIter)
	{
		if(type == 0)
		{
			std::cout << *begIter << " ";
		}
		else
		{
			if(*begIter == 1)
			std::cout << 'M' << " ";
			else if (*begIter == 2)
            std::cout << 'P' << " ";
		}
	}
	std::cout << std::endl;
}
