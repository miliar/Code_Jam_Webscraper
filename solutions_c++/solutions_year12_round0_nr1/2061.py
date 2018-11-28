#pragma warning(disable:4996)

#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

char mapping[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
//                 {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};

int main(int argc, char *argv[])
{
	if (argc != 2)
	{
		cerr << "USAGE: " << argv[0] << " <input file name>" << endl;
		return 1;
	}

	FILE* fIn = fopen(argv[1], "r");

	if (fIn == NULL)
	{
		cerr << "CANNOT OPEN FILE: " << argv[1] << endl;
		return 2;
	}

	FILE* fOut = fopen("problemA.out", "w");

	char line[128];
	int noOfSamples = atoi(fgets(line, 128, fIn));

	for (int i=0; i<noOfSamples; i++)
	{
		fprintf(fOut, "Case #%d: ", i+1);

		fgets(line, 128, fIn);

		for (int j=0; line[j] != '\0' && line[j] != '\n'; j++)
		{
			if (line[j] == ' ')
			{
				fprintf(fOut, " ");
			}
			else
			{
				fprintf(fOut, "%c", mapping[line[j]-'a']);
			}
		}

		fprintf(fOut, "\n");
	}

	fclose(fIn);
	fclose(fOut);

	return 0;
}
