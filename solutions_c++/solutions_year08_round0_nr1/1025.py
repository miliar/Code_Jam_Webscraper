#include <iostream>
#include <fstream>
#include <stdio.h>
#include <map>
#include <string>

using namespace std;

//TODO: undefine DEBUG
#define DEBUG 1
#ifdef DEBUG
#define DBG(arg) cout << arg << endl;
#else
#define DBG(arg)
#endif

class SEHelper
{
private:
	map<string, bool> seMap;
	int seCount;
	int count;

public:

	void Clear()
	{
		DBG("CLEAR ALL: ");
		seMap.clear();
		count = 0;
		seCount = 0;
	}

	void Populate(string s)
	{
		seMap.insert(make_pair(s, true));
		seCount++;
		DBG("ADDED: " << s);
	}

	void ResetAll()
	{
		map<string, bool>::iterator iter;
		for( iter = seMap.begin(); iter != seMap.end(); ++iter )
		{
			iter->second = true;
		}
		count = seCount;
		DBG("RESET ALL: ");
	}

	bool AddSE(string s)
	{
		DBG(s << seMap[s]);
		if(seMap[s])
		{
			DBG("REMOVE: " << s);
			seMap[s] = false;
			count--;
		}

		if(!count)
			return true;

		return false;
	}
};

class TestCaseHandler
{	
private:
	//TODO: change the data structure as per question
	SEHelper se;
	
	int switches;

	int testCaseId;	
	ifstream inFile;

public:

	static int totalTests;

	TestCaseHandler(char *filename)
	{
		inFile.open(filename);

		if (!inFile)
		{
			cerr << "Unable to open the input file - " << filename << endl;
			exit (-1);
		}

		inFile >> totalTests;
		testCaseId = 0;

		DBG("TOTAL TESTS : " << totalTests);
	}

	//TODO: read the data as defined by the problem
	void ReadData()
	{
		testCaseId++;
		switches = 0;
		
		DBG("TestCase : " << testCaseId);

		int totalSEs;
		inFile >> totalSEs;

		DBG("SE Count : " << testCaseId);

		string seName;

		se.Clear();
		for(int i=0; i<totalSEs; i++)
		{
			inFile >> seName;
			se.Populate(seName);
		}

		DBG("SE Add Done!");
	}

	friend ostream& operator << (ostream& os, TestCaseHandler& tsd);	

	//TODO: process information to generate some relevant data
	void Process()
	{
		int inputCount;
		inFile >> inputCount;

		DBG("Input Count : " << inputCount);

		for(int i=0; i<inputCount; i++)
		{
			string seInput;
			inFile >> seInput;

			DBG("INPUT : " << seInput);

			if(se.AddSE(seInput))
			{
				switches++;
				se.ResetAll();
			}
		}

		DBG("Test case complete!");
	}

	//TODO: interpret the information to return result.
	void GetResult(char * buffer)
	{
		sprintf(buffer, "%d", switches);
	}
};

int TestCaseHandler::totalTests = 0;

ostream& operator << (ostream& os, TestCaseHandler& tch)
{
	//TODO: change the output definition
	char buffer[100];

#ifdef DEBUG
	DBG(buffer);
#endif

	tch.GetResult(buffer);
	os << "Case #" << tch.testCaseId << ": " << buffer;
}

int main(int argc, char* argv[])
{
	if (argc != 2)
	{
		cerr << "Invalid arguments supplied" << endl;
		cerr << "Usage : " << argv[0] << "<filename>" << endl;
		exit (-1);
	}

	TestCaseHandler tch(argv[1]);	
	for (int i = 0; i < TestCaseHandler::totalTests; i++)
	{
		tch.ReadData();		
		tch.Process();		
		cout << tch << endl;
	}

	return 0;
}