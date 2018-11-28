// water.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <vector>
#include <assert.h>
#include <algorithm>

typedef std::vector<int> vi;
typedef std::vector<vi> vvi;

#include <stdlib.h>
#include <iostream>
#include <string> 

#include <sstream>

std::string 
	int_to_str(unsigned long long i)
{
	std::string s;
	std::stringstream out;
	out << i;
	s = out.str();
	return s;
}

unsigned long long 
str_to_int(std::string s)
{
	return atoi(s.c_str());

}

int main
(int argc, char* argv[])
{
	std::ifstream file("in.txt");
	std::ofstream out("out.txt");

	int T;
	unsigned long long N;
	unsigned long long K;
	file >> T;

	for (int t=0; t<T; t++)
	{
		//read t
		file >> N;

		//
		std::string s;
		s = int_to_str(N);

		K= 10000000000000000000;

		vi perm;
		for (unsigned int i=0; i<s.size(); i++)
			perm.push_back(i);
		do
		{
			std::string new_s;
			new_s.resize(s.size());
			for (unsigned j=0; j<s.size(); j++)
				new_s[j] = s[ perm[j] ];
			if ((str_to_int (new_s) > N) && (str_to_int(new_s) < K))
				K = str_to_int(new_s);

			//zero may be inserted in any place
			for (unsigned j=0; j<s.size(); j++)
			{
				std::string copy =	new_s.substr(0, j) + std::string("0")
					+ new_s.substr(j, s.size());
			if ((str_to_int (copy) > N) && (str_to_int(copy) < K))
				K = str_to_int(copy);
			}

			std::string copy = new_s;
			copy.push_back('0');
			if ((str_to_int (copy) > N) && (str_to_int(copy) < K))
				K = str_to_int(copy);
		} 
		while (std::next_permutation(perm.begin(), perm.end()));




		
		out << "Case #" << t+1 << ": ";
		out << K ;
		out << std::endl;


	}


return 0;
}

