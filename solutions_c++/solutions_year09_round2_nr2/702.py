#include <iostream>
#include <vector>
#include <list>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <map>
#include <string>


std::string itos(int a)
{
	char buf[100];
	itoa(a, buf, 100);
	return std::string(buf);
}


int main(int argc, char *argv[])
{
	std::ifstream input(argv[1]);

	int nbCases;

	input >> nbCases;

	for (int iter_case = 0; iter_case < nbCases; iter_case++)
	{

		std::string str;

		input >> str;


		bool res = next_permutation(str.begin(), str.end());

		if (res == false)
		{
			char value = 'a';
			//std::string tmp = "0" + res;
			for (int i = 0; i < str.size(); i++)
				if (str[i] != '0')
				{
					value = str[i];
					str[i] = '0';
					break;
				}
			
				str.insert(str.begin(), value);
		}

		std::cout << "Case #" << iter_case + 1 << ": " << str << std::endl;		
	}
}


// Case #1: 151
// Case #2: 1105
// Case #3: 6323

