/*

This is a C++ program.  It was compiled with g++ 3.4.4 in Cygwin.

This program reads from stdin and outputs to stdout.  In Linux, use:

g++ thisprogram.cpp
./a.out < in.txt > out.txt

*/

#include <iostream>
#include <string>

using namespace std;

struct item
{
	int maxStart;
	int maxStop;
	int location;
};

item findBestEngine(string[], int, string[], int);

int main()
{
	int numTestCases;

	cin >> numTestCases;

	for(int caseNumber = 1; caseNumber <= numTestCases; caseNumber++)
	{
		int numSearchEngines, numQueries;
		string searchEngines[100];
		string queries[1000];
		int order[1000];

		cin >> numSearchEngines;
		cin.get();

		for(int i = 0; i < numSearchEngines; i++)
			getline(cin, searchEngines[i]);

		cin >> numQueries;
		cin.get();

		for(int i = 0; i < numQueries; i++)
		{
			getline(cin, queries[i]);
			order[i] = -1;
		}

		item tempItem;
		string newQueries[1000];
		int newNumQueries;
		int start, stop, orderLength = 0;
		bool done = false;

		while(!done)
		{
			start = 0;

			while( (start < numQueries) && (order[start] != -1) )
				start++;

			if(start == numQueries)
				done = true;
			else
			{
				stop = start;

				while(order[stop] == -1)
					stop++;

				newNumQueries = stop - start;

				for(int i = 0; i < newNumQueries; i++)
					newQueries[i] = queries[start + i];

				tempItem = findBestEngine(searchEngines,
					numSearchEngines, newQueries, newNumQueries);

				for(int i = tempItem.maxStart; i < tempItem.maxStop; i++)
				{
					order[start + i] = tempItem.location;
					orderLength++;
				}
			}
		}

		int n = order[0];
		int count = 0;

		for(int i = 1; i < orderLength; i++)
			if(order[i] != n)
			{
				n = order[i];
				count++;
			}

		cout << "Case #" << caseNumber << ": " << count << '\n';
	}

	return(0);
}

item findBestEngine(string searchEngines[], int numSearchEngines,
		string queries[], int numQueries)
{
	int count, line;
	string name;
	int maxList[100];
	int maxStopList[100];

	for(int i = 0; i < numSearchEngines; i++)
	{
		name = searchEngines[i];
		count = 0;
		line = 0;
		maxList[i] = -1;

		while(line < numQueries)
		{
			if(queries[line] != name)
				count++;
			else
			{
				if(count > maxList[i])
				{
					maxList[i] = count;
					maxStopList[i] = line;
				}
break;
			}

			line++;
		}

		if(count > maxList[i])
		{
			maxList[i] = count;
			maxStopList[i] = line;
		}

	}

	int maxLocation = 0;

	for(int i = 1; i < numSearchEngines; i++)
		if(maxList[i] > maxList[maxLocation])
			maxLocation = i;

	item i;
	i.maxStart = maxStopList[maxLocation] - maxList[maxLocation];
	i.maxStop = maxStopList[maxLocation];
	i.location = maxLocation;

	return(i);
}
