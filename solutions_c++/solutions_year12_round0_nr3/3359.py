
#include "stdafx.h"
#include "iostream"
#include "string"
#include "iostream"
#include "fstream"
#include "assert.h"
#include "sstream"
#include "vector"
#include "map"
#include "set"

int msg_pow(int a, int b);
double fact(double n);
double choose(double n, double k);
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

	int a,b;
	double answer;
	
	for (int i=0; i<t; i++)
	{
		// Read next line
		std::string line;
		std::getline(infile, line);

		std::stringstream linestrm(line);

		linestrm >> a >> b;
				
		// Find the number of digits in a.
		int no_digits = 1;

		for (int j = 1; j < 10; j++)
		{
			if ((a / (msg_pow(10, j)) == 0))
			{
				no_digits = j;
				break;
			}
		}

		// Loop from a to b.
		std::map<int, int> uniques; // first is number, second is number of permutations
		std::map<int, int>::iterator it;
		int rolling_no;
		bool found;
		std::set<int> perms;
		for (int k = a; k <= b; k++)
		{
			//std::cout << "Loop next number: " << k << std::endl;
			found = false;

			// Check whether the first number is in the set.
			it = uniques.find(k);
			if (it != uniques.end())
			{
				//std::cout << "Already found this number" << std::endl;
				found = true;
				continue;
			}

			perms.clear();
			perms.insert(k);

			// Loop through the possible permutations.
			rolling_no = k;
			int num_perms = 1;
			for (int l = 0; l < (no_digits - 1); l++)
			{
				// Find the next number
				int rem = rolling_no % 10;
				rolling_no = rolling_no - rem;
				rolling_no = rolling_no / 10;
				rolling_no = rolling_no + (rem * msg_pow(10, (no_digits - 1)));

				// Check whether this number is in the right range, and we haven't already found it.
				if ((rolling_no >= a) && (rolling_no <= b) && (perms.find(rolling_no) == perms.end()))
				{
					perms.insert(rolling_no);
					num_perms++;
				}


				// Check whether the current number is in the set.
				//std::cout << "Next permutation" << rolling_no << std::endl;
				it = uniques.find(rolling_no);
				if (it != uniques.end())
				{
					//std::cout << "Already found this permutation" << std::endl;
					found = true;
					break;
				}


			}

			if (!found)
			{
				uniques[k] = num_perms;
			}
		}

		if (no_digits == 1)
		{
			answer = 0;
		}
		else 
		{
			// Loop through map.
			std::map<int,int>::iterator it;
			answer = 0;
			for (it = uniques.begin(); it != uniques.end(); it++)
			{
				answer+= choose((*it).second, 2);
			}
		}

		outfile << "Case #" << i+1 << ": " << answer << std::endl;	
	}
			
	// Close input and output files.
	infile.close();
	outfile.close();

	system("pause");

	return 0;
}

int msg_pow(int a, int b)
{
	int result = 1;
	for (int i = 0; i < b; i++)
	{
		result = result * a;
	}
	return(result);
}

double fact(double n)
{
	if (n == 0)
	{
		return 1;
	}
	else 
	{
		return (n * fact(n-1));
	}
}

double choose(double n, double k)
{
	if (n < k) 
	{
		return(0);
	}
	else 
	{
		return(fact(n)/((fact(k))*(fact(n-k))));
	}
}