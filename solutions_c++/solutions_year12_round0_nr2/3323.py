
#include "stdafx.h"
#include "iostream"
#include "string"
#include "iostream"
#include "fstream"
#include "assert.h"
#include "sstream"
#include "vector"


int _tmain(int argc, _TCHAR* argv[])
{
	// Check there are two arguments.  First argument is input, second is output.
	assert(argc == 3);

	// Open input file.
	std::ifstream infile;
	infile.open(argv[1]);
	assert(infile.is_open());
	assert(infile.good());

	// Open output file.
	std::ofstream outfile(argv[2]);

	// Read in number of testcases.
	int t;
	infile >> t;
	infile.ignore(2000,'\n');

	int n,s,p,answer,surprises;
	std::vector<int> totals;

	for (int i=0; i<t; i++)
	{
		// Read next line
		std::string line;
		std::getline(infile, line);

		std::stringstream linestrm(line);

		linestrm >> n >> s >> p;
				
		totals.clear();
		for (int j=0; j < n; j++)
		{
			int score;
			linestrm >> score;
			totals.push_back(score);
		}

		answer = 0;
		surprises = 0;
		std::vector<int>::iterator it;
		for (it = totals.begin(); it != totals.end(); it++)
		{
			int total = *it;
			if (total > ((3 * p) - 3))
			{
				answer++;
			}
			else if ((total > ((3 * p) - 5)) && ((((3 * p) - 5) > 0)))
			{
				surprises++;
			}
			else if ((total > ((3 * p) - 4)) && ((((3 * p) - 5) > 0)))
			{
				surprises++;
			}
		}
		
		answer += std::min(surprises, s);

		outfile << "Case #" << i+1 << ": " << answer << std::endl;

	}
			
	// Close input and output files.
	infile.close();
	outfile.close();

	system("pause");

	return 0;
}

