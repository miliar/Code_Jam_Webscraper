#include <iostream>
#include <string.h>
#include <fstream>
#include <map>


using namespace std;


map<string, int>	map_Engines;
string		a_Engines[128];
int			i_Engines;
int			i_Queries;

int			i_SwitchCount;


void Reset()
{
	map_Engines.clear();
	for (int i = 0; i < 128; i++)
	{
		a_Engines[i] = "";
	}
	i_Engines = 0;
	i_Queries = 0;

	i_SwitchCount = 0;

}


void FillEngineMap()
{
	for (int i = 0; i < i_Engines; i++)
	{
		map_Engines.insert(pair<string, int>(a_Engines[i], 1));
	}
}



int main (int argc, char **argv)
{
	if (argc != 3)
	{
		cerr << "usage: " << argv[0] << " <input file> <output file>" << endl;
		exit(-1);
	}

	ifstream input;
	input.open(argv[1]);
	ofstream output;
	output.open(argv[2]);

	int iCases;
	char zLine[128];
	input.getline(zLine, 128);
	iCases = atoi(zLine);

	for (int iCase = 1; iCase <= iCases; iCase++)
	{
		Reset();


		input.getline(zLine, 128);
		i_Engines = atoi(zLine);
		for (int iEngine = 0; iEngine < i_Engines; iEngine++)
		{
			input.getline(zLine, 128);
			a_Engines[iEngine] = zLine;
			//cout << "Engine = " << zLine << endl;
		}

		FillEngineMap();

		input.getline(zLine, 128);
		i_Queries = atoi(zLine);
		for (int iQuery = 0; iQuery < i_Queries; iQuery++)
		{
			input.getline(zLine, 128);
			//cout << "Query = " << zLine << endl;

			map_Engines.erase(zLine);
			if (map_Engines.empty())
			{
				i_SwitchCount++;
				cout << "Engine " << zLine << " switched. # " << i_SwitchCount << endl;

				FillEngineMap();
				map_Engines.erase(zLine);
			}
		}

		output << "Case #" << iCase << ": " << i_SwitchCount << endl;
	}


	input.close();
	output.close();

	exit(0);
}
