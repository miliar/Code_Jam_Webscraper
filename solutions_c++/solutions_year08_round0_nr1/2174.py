// GCJ.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <string>
#include <vector>

using namespace std;

string readStr(FILE* fp)
{
	char buffer[101] = "";
	char c;
	int n = 0;
	while ((c = fgetc(fp)) != '\n' && c != EOF)
	{
		buffer[n++] = c;
	}
	buffer[n] = 0;
	return string(buffer);
}

int getInd(const string& s, const vector<string>& names)
{
	int ind = 0;
	for (vector<string>::const_iterator iter = names.begin(); iter != names.end(); iter++)
	{
		if (*iter == s)
			return ind;
		ind++;
	}
	return ind;
}

void test(FILE* fp, int caseIndex)
{
	int ne, nq;
	fscanf(fp, "%d\n", &ne);
	vector<string> engines;
	engines.reserve(ne);

	for (int i = 0; i < ne; i++)
	{
		string s = readStr(fp);
		engines.push_back(s);
	}

	fscanf(fp, "%d\n", &nq);
	int *queries = new int[nq];
	int len = 0;
	for (int i = 0; i < nq; i++)
	{
		string s = readStr(fp);
		int ind = getInd(s, engines);
		if (len > 0)
		{
			if (queries[len - 1] != ind)
			{
				queries[len] = ind;
				len++;
			}
		}
		else
		{
			queries[len] = ind;
			len++;
		}
	}

	int switches = 0;
	int qLeft = len;
	while (qLeft > 0)
	{
		int maxE = -1;
		for (size_t i = 0; i < engines.size(); i++)
		{
			int steps = 0;
			while (i != (size_t)queries[(len - qLeft) + steps] && steps < len)
			{
				steps++;
			}
			if (steps > maxE)
				maxE = steps;
		}
		qLeft -= maxE;
		if (qLeft > 0)
			switches++;
	}

	printf("Case #%d: %d\n", caseIndex, switches);

	delete[] queries;
}

// argv[1] shall contain the input file name, says A-small.in
int main(int argc, char* argv[])
{
	FILE* fp = fopen(argv[1], "r");
	
	int numCases = 0;
	fscanf(fp, "%d\n", &numCases);
	for (int i = 0; i < numCases; i++)
	{
		test(fp, i + 1);
	}

	fclose(fp);
	
	return 0;
}

