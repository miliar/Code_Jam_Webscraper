#include <string>
#include <iostream>
#include <sstream>
#include <fstream>

using namespace std;

int main(int argc, char* argv[])
{
	int testCases = 0;
	int numSearchEng = 0;
	int numQueries = 0;
	int optimumSwitch = 0;
	int tempQryPos, currQryPos;
	int i, j, k;

	ifstream fin;
	ofstream fout;

	string searchEngine[100];
	string queries[1000];
	string searchStr;

	fin.open("input.txt");
	fout.open("output.txt");

	fin >> testCases;

	for (i = 0; i < testCases; i++)
	{
		fin >> numSearchEng;
		getline(fin, searchEngine[0]);

		for (j = 0; j < numSearchEng; j++)
		{
			getline(fin, searchEngine[j]);
		}

		fin >> numQueries;
		getline(fin, queries[0]);

		for (j = 0; j < numQueries; j++)
			getline(fin, queries[j]);

		j = 0;
		tempQryPos = 0;
		currQryPos = 0;
		optimumSwitch = 0;
		while (j < numQueries)
		{
			for (k = 0; k < numSearchEng; k++)
			{
				j = currQryPos;
				while ((searchEngine[k].compare(queries[j]) != 0) && (j < numQueries)) j++;

				if (j > tempQryPos) tempQryPos = j;
			}
			currQryPos = tempQryPos;
			j = tempQryPos;
			optimumSwitch++;
		}
		if (optimumSwitch > 0)
			optimumSwitch--;

		fout << "Case #" << i + 1 << ": " << optimumSwitch << endl;
	}

	return 0;
}


