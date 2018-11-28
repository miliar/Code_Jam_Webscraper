#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <cstdlib>
#define MAX_NUM_PERLINE 105

using namespace std;

char *original = "abcdefghijklmnopqrstuvwxyz";
char *tranlated = "ynficwlbkuomxsevzpdrjgthaq";

char translate(char c)
{
	int i = 0;
	while(i < 26 && tranlated[i] != c)	++i;
	if (i < 26)		return original[i];
	else			return c;
}

int main(int argc, char *argv[])
{
	if (argc < 2)
	{
		cout << "Missing arguments!" << endl;
		return -1;
	}

	ifstream inputFile = ifstream(argv[1]);
	string outputFileName = string(argv[1]) + ".out";
	ofstream outputFile = ofstream(outputFileName.c_str());
	if (!inputFile || !outputFile)
	{
		cout << "Open file error" << endl;
		return -2;
	}
	char line[MAX_NUM_PERLINE];
	memset(line, 0, MAX_NUM_PERLINE);
	inputFile.getline(line, MAX_NUM_PERLINE);
	int caseNum = atoi(line);
	int i = 0, j, count;
	while (i < caseNum)
	{
		memset(line, 0, MAX_NUM_PERLINE);
		inputFile.getline(line, MAX_NUM_PERLINE);
		count = strlen(line);
		for (j = 0; j != count; ++j)
		{
			line[j] = translate(line[j]);
		}
		outputFile << "Case #" << ++i << ": " << line << endl;
	}
	outputFile.flush();
	inputFile.close();
	outputFile.close();
	return 0;
}