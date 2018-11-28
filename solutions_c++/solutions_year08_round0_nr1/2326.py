// save_universe.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;


vector <string> engines;
vector <string> queries;

ifstream input;
ofstream output;

int switches;
int lqcei;
int queriesProcessed;

int calcFirst(int queriesIdxStart = 1)
{
	int maxEngineQueriesCount = 0;
	int longestQueriesCountEngineIdx = 1;
	int counter = 0;
	for (int i=1; i<engines.size(); ++i)
	{
		counter = 0;
		for (int j=queriesIdxStart; j<queries.size(); ++j, ++counter)
		{
			if (engines[i]!=queries[j]) continue;
			else break;
		}
		if (counter>maxEngineQueriesCount)
		{
			maxEngineQueriesCount = counter;
			longestQueriesCountEngineIdx = i;
		}
	}
	lqcei = longestQueriesCountEngineIdx;
	return maxEngineQueriesCount; //tyle przetworzyl pierwszy wybrany silnik
}

int calculateSwitches()
{
	//cout << "START\n" ;
	queriesProcessed = 0;
	switches = 0;
	lqcei = 0;
	queriesProcessed = calcFirst();
	if (queriesProcessed >= queries.size()-1) return 0;
	while (queriesProcessed<queries.size()-1)
	{
		//cout << "\t\tSTART\n";
		++switches;
		queriesProcessed += calcFirst( queriesProcessed+1 );
		//cout << "\t\tqueriesProcessed="<<queriesProcessed<<endl;
		//cout << "\t\tswitches=" << switches << endl;
		//char c;
		//cin >> c;
	}
	return switches;
}

void printData()
{
	cout << endl << "ENGINES:\n";
	for (int i=0; i<engines.size(); ++i)
	{
		cout << engines[i] << " | ";
	}
	cout << endl << "QUERIES:\n";
	for (int j=0; j<queries.size(); ++j)
	{
		cout << queries[j] << " | ";
	}
	cout << endl;
}

void readSingleTest()
{
	string tempEngine;
	string tempQuery;
	int numberOfEngines;
	input >> numberOfEngines;
	//XXX
	//cout << "\nilosc engines w tescie: " << numberOfEngines;
	for (int i=0; i<=numberOfEngines; ++i)
	{
		//printData();
		getline(input, tempEngine);
		engines.push_back( tempEngine );
	}
	int numberOfQueries;
	input >> numberOfQueries;
	//XXX
	//cout << "\n ilosc queries w tescie: " << numberOfQueries;
	for (int j=0; j<=numberOfQueries; ++j)
	{
		getline(input, tempQuery) ;
		queries.push_back( tempQuery );
	}
}

void readData()
{
	int numberOfTests;
	input >> numberOfTests;
	// XXX
	//cout << "\nilosc testow: " << numberOfTests;
	for (int i=0; i<numberOfTests; ++i)
	{
		readSingleTest();

		output << "Case #" << i+1 << ": " << calculateSwitches() << "\n";

		//printData();
		engines.clear();
		queries.clear();
	}
}


int main()
{
	input.open("input.txt");
	output.open("output.txt");
	readData();

	//string s;
	//cin >> s;
	input.close();
	output.close();
	return 0;
}

