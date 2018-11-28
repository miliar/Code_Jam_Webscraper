// GoogleCodeJam08.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <vector>
#include <fstream>
#include <iostream>
#include <string>
#include <set>

using namespace std;

struct Test
{
vector<string> engines;
vector<string> searchs;
};

int solve(Test& test)
{
	int L = test.engines.size();

	int i = 0;
	int j = 0;

	int ret = 0;

	if (test.searchs.size() == 0) return 0;

	while (i < test.searchs.size())
	{
	  set<string> s;

	  int j = i;

	  while (j < test.searchs.size())
	  {
		  if (s.size() < test.engines.size() - 1 || (s.size() == test.engines.size() - 1 && s.find(test.searchs[j]) != s.end()))
		  {
			  s.insert(test.searchs[j]);
			  j++;
		  }
		  else
		  {
			  break;
		  }
	  }

	  ret++;
	  i = j;
	}

	return ret-1;
}

int main(int argc, char* argv[])
{
	string filename(argv[1]);

	fstream fs(filename.c_str(), ios::in);

	vector<Test> testCases;

	char buf[256];

	int N;

	memset(buf, 0, sizeof(buf));

	fs.getline(buf, 256);

	N = atoi(buf);

	int i;

	for (i = 0; i < N; i++)
	{
		Test test;

		memset(buf, 0, sizeof(buf));
		fs.getline(buf, 256);

		int numEngines = atoi(buf);
		
		int k;

		for (k = 0; k < numEngines; k++)
		{
		  memset(buf, 0, sizeof(buf));
		  fs.getline(buf, 256);
		  test.engines.push_back(string(buf));
		}

		memset(buf, 0, sizeof(buf));
		fs.getline(buf, 256);
		int numSearches = atoi(buf);

		for (k = 0; k < numSearches; k++)
		{
		  memset(buf, 0, sizeof(buf));
		  fs.getline(buf, 256);
		  test.searchs.push_back(string(buf));			
		}

		testCases.push_back(test);
	}

	fs.close();

	fstream ofs("output.txt", ios::out);

	for (i = 1; i <= N; i++)
	{
		ofs << "Case #" << i << ": " << solve(testCases[i-1]) << endl;
	}

	ofs.close();
	
	return 0;
}
