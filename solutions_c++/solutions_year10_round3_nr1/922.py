#include <string>
#include <list>
#include <fstream>
#include <iostream>
#include <map>

using namespace std;

void main()
{
	ifstream inFile("c:\\CodeJam\\A-small.in");
	ofstream outFile("c:\\CodeJam\\out");

	int numberOfCases;

	inFile >> numberOfCases ; 

	for(int caseNumber = 1; caseNumber <= numberOfCases ; caseNumber++)
	{
		int result = 0;
		int N;

		inFile >> N ;

		map<int, int> m;

		for(int i = 0; i < N ; i++)
		{
			int s,e;

			inFile >> s >> e ;
			m.insert(make_pair(s,e));
		}

		for(map<int, int>::iterator it = m.begin(); it != m.end() ; it++)
		{
			for(map<int, int>::iterator it2 = it; it2 != m.end() ; it2++)
			{
				if(it->first < it2->first && it->second > it2->second)
					result++;
			}
		}

		outFile << "Case #" << caseNumber << ":" << " " << result << endl;
	}
}
