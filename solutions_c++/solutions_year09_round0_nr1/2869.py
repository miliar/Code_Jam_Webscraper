#include <string>
#include <list>
#include <fstream>
#include <iostream>

using namespace std;

void main()
{
	ifstream inFile("c:\\CodeJam\\A-large.in");
	ofstream outFile("c:\\CodeJam\\out");

	int L, D, numberOfCases;

	string words[5000];

	inFile >> L >> D >> numberOfCases ;

	for(int i = 0 ; i < D ; i++)
	{
		inFile >> words[i];
	}

	for(int caseNumber = 1; caseNumber <= numberOfCases ; caseNumber++)
	{
		int result = 0;

		string matchString;
		inFile >> matchString;

		for(int i = 0 ; i < D ; i++)
		{
			int pMatch = 0;
			int pWord = 0;

			do
			{
				if(matchString.at(pMatch) == '(')
				{				
					bool FoundOne = false;
					pMatch++;

					while(matchString.at(pMatch) != ')')
					{
						if(matchString.at(pMatch) == words[i].at(pWord))
						{
							FoundOne = true;
						}

						pMatch++;
					}

					if(FoundOne)
					{
						pWord++;
						pMatch++;

						if(pWord == words[i].length())
						{
							result++;
							break;
						}
						else
							continue;

					}
					else
						break;
				}				
				else if(matchString.at(pMatch) != words[i].at(pWord))
				{
					break;
				}

				pWord++;
				pMatch++;

				if(pWord == words[i].length())
				{
					result++;
					break;
				}
			}
			while(pMatch < matchString.length());
		}

		outFile << "Case #" << caseNumber << ":" << " " << result << endl;
	}
}


