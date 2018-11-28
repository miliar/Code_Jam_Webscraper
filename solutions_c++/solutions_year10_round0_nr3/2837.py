// themePark.cpp : définit le point d'entrée pour l'application console.
//

#include "stdafx.h"
#include <cstdlib>
#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;

struct Group
{
	int count;
	Group* next;
};

struct Case
{
	int runs;
	int places;
	Group * queue;
};

void initQueue(Group* currentGroup, int maxQueueNbr)
{
	for(int i = 0 ; i < maxQueueNbr ; i ++)
	{
		currentGroup[i].next = &currentGroup [ (i+1)>=maxQueueNbr?0:(i+1) ];
	}

}

int computeTheCase(Case* aCase)
{
	int euroAmount=0;

	Group* currentGroup = &aCase->queue[0];

	for(int runs = 0 ; runs < aCase->runs ; runs)
	{
		int placeUsed = 0;
		Group* initialGroup = currentGroup;

		while(placeUsed + currentGroup->count <= aCase->places)
		{
			if(currentGroup->count > aCase->places)
				return -1; //themePark fail, one of the groups must split.
			placeUsed += currentGroup->count;
			currentGroup = currentGroup->next;

			if(currentGroup == initialGroup)
				break;

		}
		euroAmount+= placeUsed;
		runs++;
	}

	return euroAmount;
}

int _tmain(int argc, _TCHAR* argv[])
{
	//Open file
	std::ifstream myInput ("d:\\C-small-attempt0.in");
	if(!myInput)
		return 0;

	int maxCase;
	myInput >> maxCase;	
	std::ofstream myOutput("d:\\output.txt");


	for(int i = 0; i < maxCase ; i++)
	{
		Case mycase;
		myInput >> mycase.runs;
		myInput >> mycase.places;
		
		int grpNbrs;
		myInput >> grpNbrs;
		
		mycase.queue = new Group[grpNbrs];
		initQueue(mycase.queue,grpNbrs);

		for(int i = 0 ; i < grpNbrs ; i++)
			{
				int currentGroupSize;
				myInput >> currentGroupSize;
				mycase.queue[i].count = currentGroupSize;
			}

		int euroAmount = computeTheCase(&mycase);
		if(i>0)
			myOutput << "\n";
		myOutput << "Case #";
		myOutput << i+1;
		myOutput << ": ";
		myOutput << euroAmount;
		

		delete [] mycase.queue;

	}
	



	myInput.close();
	myOutput.close();

	return 0;
}

