#include <fstream>
#include <iostream>

using namespace std;

int main()
{
	bool     doZero;
	char     line[64];
	ifstream input;
	int      base;
	int      i;
	int      lineLength                    = 0;
	int      nextNum;
	int      testCaseIndex                 = 0;
	int      testCases                     = 0;
	long long multiplier;
	long long sum;
	long long table[256];
	ofstream output;

	//
	//  Open the input file.
	//
	input.open("A-large.in", ios_base::in);
	if (false == input.is_open())
	{
		printf("Error opening the input file.");
		goto exit;
	}

	//
	//  Open the output file.
	//
	output.open("A-large.out", ios_base::out);
	if (false == output.is_open())
	{
		printf("Error opening the output file.");
		goto exit;
	}

	//
	//  Get the number of test cases.
	//
	input >> testCases;
	for (testCaseIndex = 0; testCaseIndex < testCases; testCaseIndex++)
	{
		memset(line, 0, sizeof (line));
		input.getline(line, sizeof (line));
		sum = 0;

		lineLength = strlen(line);
		if (0 == lineLength)
		{
			testCaseIndex--;
			continue;
		}

		base = 0;
		for (i = 0; i < 256; i++)
			table[i] = -1;
		for (i = 0; i < lineLength; i++)
		{
			if (-1 == table[line[i]])
			{
				table[line[i]] = -2;
				base++;
			}
		}

		if (base == 1)
			base = 2;

		for (i = 1, multiplier = 1; i < lineLength; i++)
			multiplier *= base;

		doZero = true;
		i = 0;
		table[line[i++]] = 1;
		sum += multiplier;
		multiplier /= base;
		nextNum = 2;

		for (i = 1; i < lineLength; i++)
		{
			if (table[line[i]] >= 0)
			{
				sum += multiplier * table[line[i]];
			}
			else
			{
				if (true == doZero)
				{
					table[line[i]] = 0;
					doZero = false;
				}
				else
				{
					table[line[i]] = nextNum;
					sum += multiplier * nextNum++;
				}
			}

			multiplier /= base;
		}

		output << "Case #" << testCaseIndex + 1 << ": " << sum << endl;
	}

	exit : ;

	if (input.is_open())
		input.close();

	if (output.is_open())
		output.close();

	return 0;
}
