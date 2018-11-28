#include <iostream>
#include <fstream>
#include <sstream>
#include <map>

using namespace std;

void resetSearchEngineMap(map<string, bool>& semap)
{
	for (map<string, bool>::iterator it=semap.begin(); it != semap.end(); it++)
	{
		(*it).second = false;
	}
}

// Assumes only one entry in the map is false.
string getRemainingSearchEngine(const map<string, bool>& semap)
{
	for (map<string, bool>::const_iterator it=semap.begin(); it != semap.end(); it++)
	{
		if (!(*it).second)
			return (*it).first;
	}
	throw "Corrupted Search Engine Map";
	return string();
}

int main (int argc, char** argv)
{
	if (argc < 3)
	{
		cerr << "Usage: " << argv[0] << ": INPUT OUTPUT" << endl;
		return 1;
	}
	ifstream infile;
	ofstream outfile;
	infile.open(argv[1]);
	outfile.open(argv[2]);
	string line;
	getline(infile, line);
	istringstream iss;
	int nCases = 0;
	iss.str(line);
	iss >> nCases;
	for (int i = 0; i < nCases; i++)
	{
		getline(infile, line);
		iss.clear();
		iss.seekg(0,ios::beg);
		iss.str(line);
		int nSearchEngines = 0;
		iss >> nSearchEngines;
		map<string, bool> searchEngines;
		for (int j = 0; j < nSearchEngines; j++)
		{
			getline(infile, line);
			searchEngines[line] = false;
		}

		getline(infile, line);
		iss.clear();
		iss.seekg(0,ios::beg);
		iss.str(line);
		int nQueries = 0;
		iss >> nQueries;
		int remainingSearchEngines = nSearchEngines;
		int switchCount = 0;
		string switchIfMatched = "";
		for (int k = 0; k < nQueries; k++)
		{
			getline(infile, line);
			if (line == switchIfMatched)
			{
				switchCount++;
				resetSearchEngineMap(searchEngines);
				remainingSearchEngines = nSearchEngines;
				switchIfMatched = "";
			}
			if (!searchEngines[line])
			{
				searchEngines[line] = true;
				remainingSearchEngines--;
				if (remainingSearchEngines == 1)
				{
					switchIfMatched = getRemainingSearchEngine(searchEngines);
				}
			}
		}		
		outfile << "Case #" << (i+1) << ": " << switchCount << endl;
	}
	infile.close();
	outfile.close();
}
