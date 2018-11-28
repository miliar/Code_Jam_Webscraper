#include <string>
#include <list>
#include <fstream>
#include <iostream>

using namespace std;

void main()
{
	ifstream inFile("c:\\CodeJam\\A-small.in");
	ofstream outFile("c:\\CodeJam\\out");

	int K, N, numberOfCases;

	inFile >> numberOfCases;

	for(int caseNumber = 1; caseNumber <= numberOfCases ; caseNumber++)
	{
		char buffer[30];
		bool ON = true;
		int m = 0;

		inFile >> N >> K;

		if(K == 0)
			ON = false;
		else
		{
			itoa(K, buffer, 2);

			int l = strlen(buffer);
			if( l < N )
				ON = false;
			else
			{
				for(int i = l-1 ; i >= l-N ; i--)
				{
					if(buffer[i] != '1')
					{
						ON = false;
						break;
					}
				}
			}
		}

		outFile << "Case #" << caseNumber << ":" << " " << (ON?"ON":"OFF") << endl;
	}
}
