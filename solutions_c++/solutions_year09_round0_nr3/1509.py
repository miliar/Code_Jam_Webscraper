#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>

using namespace std;

#define MAX_STRING_LENGTH 500

int main(void)
{
	char         line[MAX_STRING_LENGTH + 1] = { 0 };
	ifstream     input;
	int          result                      = 0;
	int          testCaseIndex               = 0;
	int          testCases                   = 0;
	long         table[MAX_STRING_LENGTH]    = { 0 };
	ofstream     output;
	string       targetString                = "welcome to code jam";
	unsigned int i                           = 0;
	unsigned int j                           = 0;
	unsigned int k                           = 0;
	unsigned int s                           = 0;

	//
	//  Open the input file.
	//
	input.open("C-large.in", ios_base::in);
	if (false == input.is_open())
	{
		printf("Error opening input file.");
		goto exit;
	}

	//
	//  Open the output file.
	//
	output.open("C-large.out", ios_base::out);
	if (false == output.is_open())
	{
		printf("Error opening output file.");
		goto exit;
	}

	//
	//  Get the number of test cases from the input file; move past the new line.
	//
	input >> testCases;
	input.getline(line, sizeof (line));

	//
	//  Process each test case.
	//
	for (testCaseIndex = 0; testCaseIndex < testCases; testCaseIndex++)
	{
		memset(line, 0, sizeof (line));
		input.getline(line, sizeof (line));

		if ('\0' == line[0])
			continue;

		//  Clear the table keeping track of the number possible.
		memset(table, 0, sizeof (table));

		for (j = 0; '\0' != line[j]; j++)
		{
			if ('w' == line[j])
				table[j] = 1;
		}

		s = targetString.size();
		for (i = 1; i < s; i++)
		{
			for (j = 0; '\0' != line[j]; j++)
			{
				if (0 == table[j] || targetString[i - 1] != line[j])
					continue;

				for (k = j + 1; '\0' != line[k]; k++)
				{
					if (targetString[i] == line[k])
					{
						table[k] += table[j];
						table[k] %= 10000;
					}
				}

				table[j] = 0;
			}
		}

		result = 0;
		for (i = 0; '\0' != line[i]; i++)
			result += table[i];

		output << "Case #" << (testCaseIndex + 1) << ": " << setw(4) << setfill('0') <<
			(result % 10000) << endl;
	}

	exit : ;

	if (true == input.is_open())
		input.close();

	if (true == output.is_open())
		output.close();

	return 0;
}

