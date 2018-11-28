// SavingTheUniverse.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <string>
#include <vector>
#include <map>
#include <set>
#include <fstream>
#include <iostream>
#include <strstream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef vector<string>	stringVector;
typedef set<string> engineSet;


bool ReadFileToVector(char const *szFilename,stringVector &file)
{
	string oneline;
	
	file.clear();
	
	ifstream source (szFilename, ios_base::in);
	if ( !source.is_open()) return false;
	
	while (getline(source, oneline, '\n'))
		file.push_back (oneline);
}

bool WriteVectorToFile(char const *szFilename,stringVector &file)
{
	ofstream target (szFilename, ios_base::out);

	if ( !target.is_open()) return false;

	stringVector::iterator iter;

	for ( iter = file.begin() ; iter != file.end(); iter++)
	{
		target << *iter << "\n";
	}
	
	return true;
}


int CountSwitching(engineSet &engines, stringVector &queries)
{
	int switchCount=0;
			
	stringVector::iterator iter = queries.begin();

	//copy map
	engineSet enginesTemp = engines;

	for ( ; iter != queries.end() ; iter++ )
	{
		enginesTemp.erase(*iter);

		if ( enginesTemp.size() == 0 ) 
		{
			// engine switching - checking all of cases
			switchCount++;
			
			enginesTemp = engines;
			enginesTemp.erase(*iter);
		}
	}

	return switchCount;
}

int ProcessCase(stringVector::iterator &iter)
{
	engineSet engines;
	stringVector queryVector;

	int i;

	// load engine set
	int engineCount = atoi(iter->c_str());
	iter++;

	for ( i=0 ; i < engineCount ; i++ )
		engines.insert(*(iter++));


	// load queries
	int queryCount = atoi(iter->c_str());
	iter++;

	for ( i=0 ; i < queryCount ; i++ )
		queryVector.push_back(*(iter++));


	if ( !engineCount ) return 0;
	if ( !queryCount ) return 0;

	int ret = CountSwitching(engines,queryVector);

	return ret;
}

bool ProcessFile(stringVector &source, stringVector &result)
{
	stringVector::iterator iter = source.begin();

	int caseCount = atoi(iter->c_str());
	iter++;

	for ( int i=0 ; i < caseCount ; i++ )
	{
		int ret = ProcessCase(iter);

		ostringstream strResult;
		
		strResult << "Case #" << i+1 << ": " << ret;

		result.push_back(strResult.str());

		cout << strResult.str() << endl;
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
