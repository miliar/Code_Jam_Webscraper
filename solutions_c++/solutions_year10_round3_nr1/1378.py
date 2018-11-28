//============================================================================
// Name        : codejam_1Ca.cpp
// Author      : Ivan Sovic
// Version     :
// Copyright   : Copyright Ivan Sovic, 2010.
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;

int t=0, n=0;

class Line
{
public:

	unsigned int y[2];

	bool parallel()
	{
		if (y[0] == y[1])
			return true;
		return false;
	}

	int intersects(Line &op1)
	{
		if (parallel()==true && op1.parallel()==true && y[0]!=op1.y[0])
			return 0;

		if ((y[0]<op1.y[0] && y[1]>op1.y[1]) || (op1.y[0]<y[0] && op1.y[1]>y[1]))
			return 1;

		return 0;
	}
};

vector<Line> lines;
vector<unsigned long int> results;

vector<Line> parallelLines;
vector<Line> normalLines;



void readInput()
{
	unsigned int newA=0, newB=0;
	unsigned long int currentResult=0;
	Line newLine;

	scanf ("%d", &t);

	for (int i=0; i<t; i++)
	{
		scanf ("%d", &n);

		currentResult = 0;
		normalLines.clear();
		parallelLines.clear();

		for (int j=0; j<n; j++)
		{
			scanf ("%u %u", &newA, &newB);
			newLine.y[0] = newA;
			newLine.y[1] = newB;

			if (newLine.parallel() == true)
			{
				for (unsigned int k=0; k<normalLines.size(); k++)
				{
					currentResult += newLine.intersects(normalLines[k]);
				}

				parallelLines.push_back(newLine);
			}
			else
			{
				for (unsigned int k=0; k<normalLines.size(); k++)
				{
					currentResult += newLine.intersects(normalLines[k]);
				}


				for (unsigned int k=0; k<parallelLines.size(); k++)
				{
					currentResult += newLine.intersects(parallelLines[k]);
				}

				normalLines.push_back(newLine);
			}
		}

		results.push_back(currentResult);
	}
}



/*

#include <stdlib.h>
#include <time.h>

void generate()
{
	unsigned int testN=0, size=0;
	unsigned long int newA=0, newB=0;
	FILE *fp;
	fp = fopen("test.txt", "w");

	srand ( time(NULL) );

	testN = 1000;
	size = 10000;

	fprintf (fp, "1\n");
	fprintf (fp, "%u\n", testN);

	for (unsigned int i=0; i<testN; i++)
	{
		newA = rand() % size + 1;
		newB = rand() % size + 1;

		fprintf (fp, "%lu %lu\n", newA, newB);
	}

	fclose (fp);
}
*/

void writeOutput()
{
	for (unsigned int i=0; i<results.size(); i++)
		printf ("Case #%d: %lu\n", (i+1), results[i]);
}

int main()
{
//	generate();
	readInput();
	writeOutput();
}
