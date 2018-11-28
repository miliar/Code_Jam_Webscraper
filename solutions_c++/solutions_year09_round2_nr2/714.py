#include<iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>
#include <string>
using namespace std;


int main(int argc, char** argv)
{
	char * input = argv[1];
	std::ifstream file (input);
	int NbrCase;
	file >> NbrCase;
		
	for (int k = 1; k <= NbrCase; ++k)
	{
		long long int total = 0;
		string str;

		file >> str;


		bool permutation;
		permutation = next_permutation(str.begin(), str.end());
		if (!permutation)
		{
			str.insert(str.begin(), 0);
			for (int i = 1; i < str.size(); ++i)
				if (str[i] != '0')
				{
					str[0] = str[i];
					str[i] = '0';
					break;
				}
		}


			
		std::cout << "Case #" << k << ": " << str << endl;
	}
	return 0;
}
