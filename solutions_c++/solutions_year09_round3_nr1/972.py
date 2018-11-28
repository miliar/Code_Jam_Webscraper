/*
 * A.cpp
 *
 *  Created on: Sep 13, 2009
 *      Author: bernberg11
 */

#include <iostream>
#include <fstream>
#include <map>
#include <cstdlib>
#include <math.h>
using namespace std;

int main(int argc, char * argv[])
{
	int num_cases;
	ifstream infile;

	infile.open(argv[1]);
	if (!infile)
	{
	   cout << "Invalid file name" << endl;
	   exit(1);
	}
	infile >> num_cases;


	for (int i=0; i < num_cases; i++)
	{
		string num;
		infile >> num;
		map <char,unsigned long long> decoder;
		unsigned long long next_num = 1;
		unsigned long long base;
		for (string::iterator it=num.begin(); it!= num.end(); it++)
		{
			if (decoder.count(*it) == 0)
			{
				decoder[*it] = next_num;
				if (next_num == 1) next_num = 0;
				else if (!next_num) next_num = 2;
				else next_num++;
			}
		}
		base = (unsigned long long)decoder.size();
		if (base == 1) base = 2;
		unsigned long long sum = 0;

		for (string::iterator it=num.begin(); it!= num.end(); it++)
		{

			sum += decoder[*it]*pow(base,num.end()-it-1);

		}

		cout << "Case #" << i+1 << ": " << sum << endl;
	}
	return 0;
}
