#include <iostream>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <set>
using namespace std;

set<int> results;

void process(string filepath)
{
	ifstream ifs(filepath.c_str());
	ofstream ofs("output");
	int LineCnt = 0;
	int numTestCases = 0;
	int upbound = 0, bottombound = 0; 
	int CaseCount = 1;
	string line;
	while (getline(ifs, line))
	{
		int numPairs = 0;
		if (LineCnt == 0) 
		{
			numTestCases = atoi(line.c_str());
			LineCnt++;
			continue;
		}
		int spacepos = line.find(' ');
		bottombound = atoi(line.substr(0, spacepos).c_str());
		upbound = atoi(line.substr(spacepos, line.size()).c_str());
		for (int i = bottombound; i < upbound; i++)
		{
			//convert to string
			stringstream ss;
			string originalNumber;
			ss << i;
			ss >> originalNumber;
			//reverse
			for (int j = 1; j <= originalNumber.size() - 1; j++)
			{
				string n = originalNumber;
				int t = 0;
				reverse(n.begin(), n.begin() + j);
				reverse(n.begin() + j, n.end());
				reverse(n.begin(), n.end());
				t = atoi(n.c_str());
				if (t > i && t <= upbound) 
				{
					numPairs++;
				}
			}
		}
		ofs<<"Case #"<<CaseCount++<<": "<<numPairs<<endl;
		results.clear();
	}
	ifs.close();
	ofs.close();
}

int main(int argc, char **argv)
{
	process(argv[1]);
}
