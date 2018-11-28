// TrainTimetable.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <vector>
#include <fstream>
#include <iostream>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

struct Test
{
int turnAround;
vector<pair<string, string> > NA;
vector<pair<string, string> > NB;
};

int getValue(string& s)
{
	string temp = s.substr(0, 2) + s.substr(3, 2);

	return atoi(temp.c_str());
}

int timeAdd(int op1, int op2)
{
	int firstTwo = op1 / 100;
	int lastTwo = op1 % 100;

	if (lastTwo + op2 >= 60)
	{
		return (firstTwo + 1) * 100 + (lastTwo + op2 - 60);
	}
	else
	{
		return firstTwo * 100 + (lastTwo + op2);
	}
}

pair<int, int> solve(Test& test)
{
	int memA[2500];
	int memB[2500];

	memset(memA, 0, sizeof(memA));
	memset(memB, 0, sizeof(memB));

	sort(test.NA.begin(), test.NA.end());
	sort(test.NB.begin(), test.NB.end());

	int i = 0;
	int j = 0;

	int retA = 0;
	int retB = 0;

	while (i < test.NA.size() || j < test.NB.size())
	{
		if (i >= test.NA.size())
		{
			int k = 0;

			int start = getValue(test.NB[j].first);
			int end = getValue(test.NB[j].second);

			for (k = 0; k <=start; k++)
			{
				if (memB[k] != 0)
				{
					memB[k]--;
					break;
				}
			}

			if (k > start) retB++;
			memA[timeAdd(end, test.turnAround)]++;

			j++;
		}
		else if (j >= test.NB.size())
		{
			int k = 0;

			int start = getValue(test.NA[i].first);
			int end = getValue(test.NA[i].second);

			for (k = 0; k <=start; k++)
			{
				if (memA[k] != 0)
				{
					memA[k]--;
					break;
				}
			}

			if (k > start) retA++;
			memB[timeAdd(end, test.turnAround)]++;
			i++;
		}
		else 
		{
			if (test.NA[i].first <= test.NB[j].first)
			{
				int k = 0;

				int start = getValue(test.NA[i].first);
				int end = getValue(test.NA[i].second);

				for (k = 0; k <=start; k++)
				{
					if (memA[k] != 0)
					{
						memA[k]--;
						break;
					}
				}

				if (k > start) retA++;
				memB[timeAdd(end, test.turnAround)]++;
				i++;
			}
			else
			{
				int k = 0;

				int start = getValue(test.NB[j].first);
				int end = getValue(test.NB[j].second);

				for (k = 0; k <= start; k++)
				{
					if (memB[k] != 0)
					{
						memB[k]--;
						break;
					}
				}

				if (k > start) retB++;
				memA[timeAdd(end, test.turnAround)]++;
				j++;
			}
		}
	}

	return make_pair(retA, retB);
}

int main(int argc, char* argv[])
{
	string filename(argv[1]);

	fstream fs(filename.c_str(), ios::in);

	vector<Test> testCases;

	int N;

	fs >> N;

	int i;

	for (i = 0; i < N; ++i)
	{
		Test test;

		fs >> test.turnAround;

		int na, nb;

		fs >> na >> nb;

		int j;

		for (j = 0; j < na;  j++)
		{
			string start, end;

			fs >> start >> end;

			test.NA.push_back(make_pair(start, end));
		}

		for (j = 0; j < nb; j++)
		{
			string start, end;

			fs >> start >> end;

			test.NB.push_back(make_pair(start, end));
		}

		testCases.push_back(test);
	}


	fs.close();

	fstream ofs("output.txt", ios::out);

	for (i = 1; i <= N; i++)
	{
		pair<int, int> pr = solve(testCases[i-1]);

		ofs << "Case #" << i << ": " << pr.first << " " << pr.second << endl;
	}
	
	return 0;
}
