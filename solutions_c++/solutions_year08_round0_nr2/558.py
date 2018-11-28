// Template for code jam!
//
#include "stdafx.h"
//#include <math.h>
#include <fstream>
#include <string>
#include <vector>
//#include <map>
//#include <queque>
//#include <stack>
//#include <set>

using namespace std;

typedef struct t_travel{
	int departure;
	int arrive;
	bool reused;
} travel;

//other functions may go here!


//main function!

int inline convertTimeMin(string& time)
{
	return atoi(time.substr(0, 2).c_str())*60 + atoi(time.substr(3, 2).c_str());
}

void inline calcAB(vector<travel>& travelA, vector<travel>& travelB, int& totalA, int& totalB)
{
	int searchA = 0;
	int searchB = 0;
	totalA = totalB = 0;
	int search, smallest, index, compare;
	bool check;
	
	if(travelA.size() == 0)
	{
		totalA = 0;
		totalB = travelB.size();
		return;
	}
	else if(travelB.size() == 0)
	{
		totalA = travelA.size();
		totalB = 0;
		return;
	}

	while((searchA < travelA.size()) || (searchB < travelB.size()))
	{
		if((searchA < travelA.size()) && ((searchB >= travelB.size()) || travelA[searchA].departure <= travelB[searchB].departure))
		{
			index = search = 0;
			smallest = -1; // quick fix too
			check = false;
			while(search < searchB)
			{
				if((travelB[search].arrive <= travelA[searchA].departure) && (!travelB[search].reused))
				{
					check = true;
					if(travelB[search].arrive < smallest || (smallest == -1))
					{
						smallest = travelB[search].arrive;
						index = search;
					}
				}
				search++;
			}
			if(check)
				travelB[index].reused = true;	
			else
				totalA++;
			searchA++;
		}
		else if(searchB < travelB.size())
		{
			index = search = 0;
			smallest = -1;
			check = false;
			while(search < searchA)
			{
				if((travelA[search].arrive <= travelB[searchB].departure) && (!travelA[search].reused))
				{
					check = true;
					if(travelA[search].arrive < smallest || (smallest == -1))
					{
						smallest = travelA[search].arrive;
						index = search;
					}
				}
				search++;
			}
			if(check)
				travelA[index].reused = true;	
			else
				totalB++;
			searchB++;
		}
	}	
}

int _tmain(int argc, _TCHAR* argv[])
{
    ifstream inputFile("B-large.in");
    ofstream outputFile("B-large.out", std::ios::trunc);
    if((!inputFile.is_open()) || (!outputFile.is_open()))
    {
      //error openning input/output file!
      return 0;
    }

	int numIterations;
	int numCases = 1;
	string receive;
	inputFile >> numIterations;
	vector<travel> travelA, travelB;
	int turnAround, numTripsA, numTripsB;
	int time, search, a, b;
	travel aux;
	aux.reused = false;
	while(numCases <= numIterations)
	{
		//parsing code goes here
		travelA.clear();
		travelB.clear();
		
		inputFile >> turnAround;
		inputFile >> numTripsA;
		inputFile >> numTripsB;
		for(int x=0; x<numTripsA; x++)
		{
			inputFile >> receive;
			time = convertTimeMin(receive);
			inputFile >> receive;
			for(search=0; search<travelA.size(); search++)
			{
				if(time < travelA[search].departure)
					break;
			}
			aux.departure = time;
			aux.arrive = convertTimeMin(receive)+turnAround;
			travelA.insert(travelA.begin()+search, aux);
		}
		for(int x=0; x<numTripsB; x++)
		{
			inputFile >> receive;
			time = convertTimeMin(receive);
			inputFile >> receive;
			for(search=0; search<travelB.size(); search++)
			{
				if(time < travelB[search].departure)
					break;
			}
			aux.departure = time;
			aux.arrive = convertTimeMin(receive)+turnAround;
			travelB.insert(travelB.begin()+search, aux);
		}

		//problem code goes here
		calcAB(travelA, travelB, a, b);
		outputFile << "Case #" << numCases << ": " << a << " " << b << endl;
		numCases++;
	}
	return 0;
}