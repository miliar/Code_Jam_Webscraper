// SnapperChain.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <boost/dynamic_bitset.hpp>

using namespace std;

int main()
{
	ifstream inputFile ("A-small-attempt1.in");
	ofstream outputFile ("output.out");
	if(!inputFile.is_open())
		return 0;
	if(!outputFile.is_open())
		return 0;
	
	string line;
	int totalCases = 0;
	inputFile >> totalCases;
	getline(inputFile, line);  //Get to next line

	for (int i=0; i < totalCases; ++i)  
	{
		int N = 0, K = 0;
		inputFile >> N;
		inputFile >> K;
		getline(inputFile, line);  //Get to next line

		boost::dynamic_bitset<> snappers(N); // all 0's by default
		boost::dynamic_bitset<> power(N); // all 0's by default
		power[0] = 1;

		for (int loop = 0; loop < K; ++loop)
		{
			for (boost::dynamic_bitset<>::size_type i = 0; i < power.size(); ++i)
			{
				if(power[i])
				{
					snappers.flip(i);
				}
				if(!power[i] || i == (power.size()-1))
				{
					for (boost::dynamic_bitset<>::size_type j = 0; j < power.size(); ++j)
					{
						if(snappers[j])
							power[j+1] = 1;
						else
						{
							for (boost::dynamic_bitset<>::size_type k = j+1; k < power.size(); ++k)
							{
								power[k] = 0;
							}
							break;
						}
					}
					break;
				}
			}
		}

		snappers.flip();
		outputFile << "Case #" << (i+1) << ": ";
		if(snappers.none())
			outputFile  << "ON";
		else
			outputFile << "OFF";
		outputFile << endl;
		power.clear();
		snappers.clear();
	}
	
	inputFile.close();
	outputFile.close();
	return 0;
}

