#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <stdlib.h>

#include "boost/tuple/tuple.hpp"
#include "boost/bind.hpp"

using namespace boost;
using namespace std;

std::vector<std::string> tokenize_str(const std::string & str,
							const std::string & delims);
bool value_comparer(const std::pair<std::string, size_t>& lhs,
				const std::pair<std::string, size_t>& rhs);

typedef vector<int> Freq;

int main()
{
	ifstream inputFile ("A-small-attempt0.in");
	if(!inputFile.is_open())
		return 0;
	ofstream outputFile ("output.in");
	if(!outputFile.is_open())
	{
		inputFile.close();
		return 0;
	}
	int totalCases = 0;
	inputFile >> totalCases;
	string line;
	for (int i=0; i < totalCases; ++i)  
	{
		int keys, alphabets, times;
		inputFile >> times;
		inputFile >> keys;
		inputFile >> alphabets;
		getline(inputFile, line);	//Get to next line
		Freq freq;
		for (int j=0; j < alphabets; ++j)  
		{
			int f;
			inputFile >> f;
			freq.push_back(f);
		}		
		getline(inputFile, line);	//Get to next line
		sort(freq.begin(), freq.end(), greater<int>());
		int nTimes = 0;
		for(int k=0; k<freq.size(); ++k)
		{
			int f = freq[k];
			if(f > 0)
			{
				nTimes += f * ((k / keys)+1);
			}
		}
		outputFile << "Case #" << (i+1) << ": " << nTimes << endl;
	}
	
	inputFile.close();
	outputFile.close();
	return 0;
}

bool value_comparer(const std::pair<std::string, size_t>& lhs,
				const std::pair<std::string, size_t>& rhs)
{
	return lhs.second < rhs.second;
}

std::vector<std::string> tokenize_str(const std::string & str,
							const std::string & delims)
{
	using namespace std;
	// Skip delims at beginning, find start of first token
	string::size_type lastPos = str.find_first_not_of(delims, 0);
	// Find next delimiter @ end of token
	string::size_type pos     = str.find_first_of(delims, lastPos);


	// output vector
	vector<string> tokens;


	while (string::npos != pos || string::npos != lastPos)
	{
		// Found a token, add it to the vector.
		tokens.push_back(str.substr(lastPos, pos - lastPos));
		// Skip delims.  Note the "not_of". this is beginning of token
		lastPos = str.find_first_not_of(delims, pos);
		// Find next delimiter at end of token.
		pos     = str.find_first_of(delims, lastPos);
	}


	return tokens;
}
