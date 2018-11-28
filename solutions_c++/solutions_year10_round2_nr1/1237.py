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

	int M, N, numberOfCases;

	inFile >> numberOfCases ; 

	for(int caseNumber = 1; caseNumber <= numberOfCases ; caseNumber++)
	{
		inFile >>M >> N;

		map<string, bool> m;

		int result = 0;

		string path;
		

		for(int i = 0 ; i < M ; i++)
		{
			inFile >> path;
			m.insert(make_pair(path, true));
		}

		for(int i = 0 ; i < N ; i++)
		{
			inFile >> path;
			m.insert(make_pair(path, false));
		}

		string prev = "/";

		for(map<string, bool>::iterator it = m.begin(); it != m.end(); it++)
		{
			if(it->second == false)
			{
				string path = it->first;

				int i;

				for(i = 0; i < prev.length() ; i++)
				{
					if(i >= path.size() ||  prev.at(i) != path.at(i))
						break;
				}

				string s = path.substr(i);

				char spath[100];
				strcpy(spath, s.data());

				char *tok = strtok(spath, "/");
				while (tok != 0)
				{
					result++;
					tok = strtok(0, "/");
				}
			}

			prev = it->first;
		}		

		outFile << "Case #" << caseNumber << ":" << " " << result << endl;
	}
}
