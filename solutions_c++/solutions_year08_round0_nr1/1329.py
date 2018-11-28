// SaveTheUniverse.cpp : Defines the entry point for the console application.
//


#include <stdio.h>
#include <tchar.h>
#include <iostream>
#include <vector>
#include <fstream>
#include <cassert>
#include <string>
#include <algorithm>
using namespace std;


void GetInputLines(istream & in, int lines, vector<string> & strs);
void GetInputLines(istream & in, vector<string> & strs);
class PrintString
{
public:
	void operator() (const string & s)
	{
		cout << s << endl;
	}
};

int FindOptimalSwitch(const vector<string> & engines, const vector<string> & queries);

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("input.txt");
	ofstream out("output.txt");
	if( !in )
	{
		cout << "can't open input file" << endl;
		return 1;
	}

	if( !out )
	{
		cout << "can't open input file" << endl;
		return 1;
	}
	

	int totalCase = 0;
	in>> totalCase;
	cout << totalCase << endl;

	assert( totalCase > 0 );
	for( int i = 1; i <= totalCase; ++i )
	{
		vector<string> engines;
		vector<string> queries;
		GetInputLines(in,engines);
		GetInputLines(in,queries);
		int ret = FindOptimalSwitch(engines,queries);
		cout << "Case #" << i <<": " << ret << endl;
		out << "Case #" << i <<": " << ret << endl;
	}

}


void GetInputLines(istream & in, vector<string> & strs)
{
	int lines = 0;
	in >> lines;
	in.ignore();
	cout << lines << endl;
	GetInputLines( in, lines, strs);
//	std::for_each( strs.begin(), strs.end(), PrintString());
}

void GetInputLines(istream & in, int lines, vector<string> & strs)
{
	strs.clear();
	strs.reserve(lines);

	for( int i = 1; i <= lines; ++i )
	{
		char str[1024];
		in.getline(str,1024);
		strs.push_back(str);
	}
}



void ResetMarks(vector<bool> & marks)
{
	for( size_t i = 0; i < marks.size(); ++i )
		marks[i] = false;
}

int FindOptimalSwitch(const vector<string> & engines, const vector<string> & queries)
{
	int switches = 0;
	int markCount = 0;
	string currEngine;
	vector<bool> marks(engines.size());

	for( size_t i = 0; i < queries.size(); ++i )
	{
		for( size_t j = 0; j < engines.size(); ++j )
		{
			if( engines[j] == queries[i] && !marks[j])
			{
				marks[j] = true;
				markCount++;
				if( markCount == engines.size() )
				{
					ResetMarks(marks);
					marks[j] = true;
					switches++;
					markCount = 1;
				}
				break;
			}
		}
	}


	return switches;
}
