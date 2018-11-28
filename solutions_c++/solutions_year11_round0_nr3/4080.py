#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
using std::cout;
using std::endl;
using std::ifstream;
using std::ofstream;
using std::istringstream;
using std::string;
using std::vector;

bool boolArrayAdd(bool boolArray[], int len)
{
	bool carry = true;
	for(int i = 0; i <= len; i++)
	{
		if(carry == false)
			return false;
		bool nextCarry = carry;
		nextCarry &= boolArray[i];
		boolArray[i] ^= carry;
		carry = nextCarry;
	}
	return true;
}

int main(int argc, char *argv[])
{
	if(argc < 3)
		cout << "Usage: " << argv[0] << " <input file> <output file>" << endl;
	
	ifstream inputFile(argv[1]);
	ofstream outputFile(argv[2]);
	unsigned int testCases;
	inputFile >> testCases;
	
	for(unsigned int caseNum = 0; caseNum < testCases; caseNum++)
	{
		unsigned int candyNum;
		inputFile >> candyNum;
		
		vector<unsigned int> candyBag;
		bool group[candyNum];
		for(unsigned int i = 0; i < candyNum; i++)
		{
			unsigned int candyValue;
			inputFile >> candyValue;
			candyBag.push_back(candyValue);
			group[i] = false;
		}
		
		unsigned int maxVal = 0;
		unsigned int groupA, groupB, groupANum, groupBNum;
		while(boolArrayAdd(group, candyNum) == false)
		{
			groupA = 0;
			groupB = 0;
			groupANum = 0;
			groupBNum = 0;
			for(unsigned int i = 0; i < candyBag.size(); i++)
			{
				if(group[i])
				{
					groupA ^= candyBag[i];
					groupANum++;
				}
				else
				{
					groupB ^= candyBag[i];
					groupBNum++;
				}
			}
			if((groupA == groupB) && (groupANum * groupBNum != 0))
			{
				groupA = 0;
				groupB = 0;
				for(unsigned int i = 0; i < candyBag.size(); i++)
				{
					if(group[i])
						groupA += candyBag[i];
					else
						groupB += candyBag[i];
				}
				if(maxVal < ((groupA > groupB) ? groupA : groupB))
					maxVal = ((groupA > groupB) ? groupA : groupB);
			}
		}
		if(maxVal == 0)
			outputFile << "Case #" << caseNum + 1 << ": " << "NO" << endl;
		else
			outputFile << "Case #" << caseNum + 1 << ": " << maxVal << endl;
	}
	outputFile.close();
	inputFile.close();
	return 0;
}