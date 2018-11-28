#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>


using namespace std;



int GetOpen(char& p_rChar)
{
	switch (p_rChar)
	{
		case '(':
			return 1;
		case ')':
			return 2;
		default:
			return 0;
	}
}

int GetCount(string& p_rsWord, vector<string> p_vsPatterns, int p_iFlag)
{
	int iCount(0);
	int iState(0);
	bool bUnique = false;
	vector<int> vIndexes;
	set<string> p_vsTempPatterns;
	for(size_t i = 0; i < p_rsWord.length(); ++i)
	{
		if (p_iFlag)
		{
			iState = GetOpen(p_rsWord[i]);

			if (iState == 1)
				bUnique = true;
			else
				if (iState == 2)
				{
					iCount++;
					bUnique = false;
					p_vsPatterns.clear();
					copy(p_vsTempPatterns.begin(), p_vsTempPatterns.end(), inserter(p_vsPatterns, p_vsPatterns.end()));
					p_vsTempPatterns.clear();
				}
			if(iState)
				continue;
		}
			for(size_t j = 0; j < p_vsPatterns.size(); ++j)
			{
				if (p_vsPatterns[j][iCount] == p_rsWord[i])
					p_vsTempPatterns.insert(p_vsPatterns[j]);
			}
			

		if (!bUnique)
			iCount++;

		if (!p_iFlag)
		{
			p_vsPatterns.clear();
			copy(p_vsTempPatterns.begin(), p_vsTempPatterns.end(), inserter(p_vsPatterns, p_vsPatterns.end()));
			p_vsTempPatterns.clear();
		}
	}
	return p_vsPatterns.size();
}

int main()
{
	int iL, iD, iN, counter(0), oCounter(1);
	vector<string> vsPatterns, vsLanguage;
	string inputLine;
	ifstream iFile;
	ofstream oFile;
	iFile.open("A-small-attempt2.in");
	oFile.open ("A-small-attempt2.out");

	if (iFile.is_open())
	{
		iFile >> iL >> iD >> iN;
		while(!iFile.eof())
		{
			getline(iFile, inputLine);
			if(!inputLine.empty())
			{
				if (counter < iD)
					vsPatterns.push_back(inputLine);
				else
					if(inputLine.find('(') != string::npos)
					{
						oFile << "Case #" << oCounter++ << ": " << GetCount(inputLine, vsPatterns, 1) << endl;
					}
					else
						oFile << "Case #" << oCounter++ << ": " << GetCount(inputLine, vsPatterns, 0) << endl;
				counter++;
			}
		}
		iFile.close();
		oFile.close();
	}
}
