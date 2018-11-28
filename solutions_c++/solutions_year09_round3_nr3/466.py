#include <algorithm>
#include <fstream>
#include <functional>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
	char     line[64];
	ifstream input;
	int      p;
	int      q;
	int      s;
	int      i;
	int      j;
	int      lineLength                    = 0;
	int      c[100];
	int      testCaseIndex                 = 0;
	int      testCases                     = 0;
	ofstream output;
	vector < int > tbr;

	//
	//  Open the input file.
	//
	input.open("C-small-attempt0.in", ios_base::in);
	if (false == input.is_open())
	{
		printf("Error opening the input file.");
		goto exit;
	}

	//
	//  Open the output file.
	//
	output.open("C-small-attempt0.out", ios_base::out);
	if (false == output.is_open())
	{
		printf("Error opening the output file.");
		goto exit;
	}

	int bs;

	//
	//  Get the number of test cases.
	//
	input >> testCases;
	for (testCaseIndex = 0; testCaseIndex < testCases; testCaseIndex++)
	{
		bs = 1000000;
		input >> p >> q;
		tbr.erase(tbr.begin(), tbr.end());

		while (q > 0)
		{
			int p;
			input >> p;
			tbr.push_back(p - 1);
			q--;
		}

		sort(tbr.begin(), tbr.end());

		do
		{
			s = 0;
			i;
			for (i = 0; i < 100; i++)
				c[i] = 1;

			for (i = 0; i < tbr.size(); i++)
			{
				c[tbr[i]] = 0;
				for (j = tbr[i] + 1; j < p; j++)
				{
					if (0 == c[j])
						break;
					s++;
				}

				for (j = tbr[i] - 1; j >= 0; j--)
				{
					if (0 == c[j])
						break;
					s++;
				}
			}

			if (bs > s)
				bs = s;
		}while (next_permutation(tbr.begin(), tbr.end()));

		output << "Case #" << testCaseIndex + 1 << ": " << bs << endl;
	}

	exit : ;

	if (input.is_open())
		input.close();

	if (output.is_open())
		output.close();

	return 0;
}
