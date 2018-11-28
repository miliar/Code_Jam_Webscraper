// TrainTimetable.cpp : Defines the entry point for the console application.
//

#include "StdAfx.h"

#include <string>
#include <vector>
#include <list>
#include <set>
#include <fstream>
#include <iostream>
#include <strstream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef enum
{
	eReady,
	eDeparture
} eventType;

typedef int	daytime;

typedef pair<daytime,eventType>	trainEvent;
typedef list<trainEvent>		eventList;
typedef vector<string>			stringVector;


void explode(string & text, char separator, stringVector & words)
{
	int n = text.length();
	int start, stop;
	start = text.find_first_not_of(separator);

	words.clear();

	while ((start >= 0) && (start < n))
	{
		stop = text.find_first_of(separator, start);
		if ((stop < 0) || (stop > n)) stop = n;

		words.push_back(text.substr(start, stop - start));
		start = text.find_first_not_of(separator, stop+1);
	}
}

bool ReadFileToVector(char const *szFilename,stringVector &file)
{
	string oneline;
	
	file.clear();
	
	ifstream source (szFilename, ios_base::in);
	if ( !source.is_open()) return false;
	
	while (getline(source, oneline, '\n'))
		file.push_back (oneline);

	return true;
}

bool WriteVectorToFile(char const *szFilename,stringVector &file)
{
	ofstream target (szFilename, ios_base::out);

	if ( !target.is_open()) return false;


	stringVector::iterator iter;

	for ( iter = file.begin() ; iter != file.end(); iter++)
	{
		target << *iter << "\n";

		cout << *iter << "\n";
	}
	
	return true;
}

daytime StringToDaytime(string strTime)
{
	stringVector lstTemp;
	explode(strTime,':',lstTemp);

	int H = atoi(lstTemp[0].c_str());
	int M = atoi(lstTemp[1].c_str());

	return (H*60)+M;
}

void MakeEventList(stringVector::iterator &iter, eventList &trainEventsA,	eventList &trainEventsB)
{
	int i;

	// load turnaround time
	int turnAroundTime = atoi(iter->c_str());
	iter++;
	
	// load NA/NB
	stringVector lstTemp;
	explode(*iter,' ',lstTemp);
	
	int startACount = atoi(lstTemp[0].c_str());
	int startBCount = atoi(lstTemp[1].c_str());

	trainEventsA.clear();
	trainEventsB.clear();
	
	iter++;
	
// 	// make event from time list A
	for ( i=0 ; i < startACount ; i++ )
	{
		explode(*(iter++),' ',lstTemp);
		
		daytime tDeparture	= StringToDaytime(lstTemp[0]);
		daytime tReady		= StringToDaytime(lstTemp[1]);
	
		trainEventsA.push_back(trainEvent(tDeparture,eDeparture));
		trainEventsB.push_back(trainEvent(tReady+turnAroundTime,eReady));
	}
	
	// make event from time list B
	for ( i=0 ; i < startBCount ; i++ )
	{
		explode(*(iter++),' ',lstTemp);
		
		daytime tDeparture	= StringToDaytime(lstTemp[0]);
		daytime tReady		= StringToDaytime(lstTemp[1]);
		
		trainEventsB.push_back(trainEvent(tDeparture,eDeparture));
		trainEventsA.push_back(trainEvent(tReady+turnAroundTime,eReady));
	}


	trainEventsA.sort();
	trainEventsB.sort();
}

int CountTrainToStart(eventList &trainEvents)
{
	int readyCount=0;
	int startCount=0;

	cout << "---------------------------------------------------" << endl;

	for ( eventList::iterator iter = trainEvents.begin() ; iter != trainEvents.end() ; iter++ )
	{
		if ( iter->second == eDeparture )
		{
			if ( readyCount ) readyCount--;
			else startCount++;
		}
		else readyCount++;
	}

	return startCount;
}

void ProcessCase(stringVector::iterator &iter, int &readyTrainAtA, int &readyTrainAtB)
{
	int i;
	string strItem;

	eventList trainEventsA;
	eventList trainEventsB;

	MakeEventList(iter, trainEventsA,trainEventsB);



	///////////////////////////////////////////
	// Counting trains to start from A
	readyTrainAtA = CountTrainToStart(trainEventsA);

	// Counting trains to start from B
	readyTrainAtB = CountTrainToStart(trainEventsB);

}

bool ProcessFile(stringVector &source, stringVector &result)
{
	stringVector::iterator iter = source.begin();

	int caseCount = atoi(iter->c_str());
	iter++;

	for ( int i=0 ; i < caseCount ; i++ )
	{
		int readyTrainAtA;
		int readyTrainAtB;

		ProcessCase(iter,readyTrainAtA,readyTrainAtB);

		ostringstream strResult;
		strResult << "Case #" << i+1 << ": " << readyTrainAtA << " " << readyTrainAtB;

		result.push_back(strResult.str());
	}

	return true;
}


int main(int argc, char* argv[])
{
	stringVector vsource;
	stringVector vresult;

	if ( !ReadFileToVector("input.txt",vsource) ) return -2;
	ProcessFile(vsource,vresult);

	WriteVectorToFile("test.txt",vresult);

	getchar();

	return 0;
}
