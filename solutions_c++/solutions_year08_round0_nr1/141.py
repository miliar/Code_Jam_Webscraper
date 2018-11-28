#include <stdio.h>
#include <stdlib.h>
#include <cstring>

#include <iostream>
#include <string>
#include <fstream>
#include <cmath>
#include <vector>
#include <map>
#include <set>
FILE* fp;
FILE* fout;

#define JAM_DEBUG

#define MAX_CHAR 100

#ifdef JAM_DEBUG
#define TEST_IN fp
#define TEST_OUT fout
#else
#define TEST_IN stdin
#define TEST_OUT stdout
#endif

std::set<std::string> Engines;
std::vector<std::string> Queries;

int Input()
{
	char szName[MAX_CHAR];
	int nNumEngine;
	int nNumQuery;

	Engines.clear();
	Queries.clear();
	
	fscanf(TEST_IN, "%d\n", &nNumEngine);
	for (int i=0; i<nNumEngine; i++)
	{
		fgets(szName, MAX_CHAR, TEST_IN);
		Engines.insert(szName);
	}
	fscanf(TEST_IN, "%d\n", &nNumQuery);
	Queries.reserve((size_t)nNumQuery);
	for (int i=0; i<nNumQuery; i++)
	{
		fgets(szName, MAX_CHAR, TEST_IN);
		Queries.push_back(szName);
	}
	return 0;
}

int Compute()
{
	int nNumSwitch = 0;
	std::set<std::string> appeared;
	for (int i=0; i<(int)Queries.size(); i++)
	{
		const std::string& query = Queries[i];
		if (Engines.find(query) != Engines.end())
		{
			appeared.insert(query);
			if (appeared.size() == Engines.size())
			{
				nNumSwitch++;
				appeared.clear();
				appeared.insert(query);
			}
		}
	}
	return nNumSwitch;
}

int Program()
{
	int nNumCase;
	fscanf(TEST_IN, "%d\n", &nNumCase);
	for (int i=0; i<nNumCase; i++)
	{
		Input();
		int ret = Compute();
		fprintf(TEST_OUT,"Case #%d: %d\n",i+1, ret);
	}
	return 0;
}

int main()
{
	fp = fopen("A-large.in", "r");
	fout = fopen("output.txt", "w");
	Program();
	fclose(fp);
	fclose(fout);
#ifdef JAM_DEBUG
	system("pause");
#endif
	return 0;
}

