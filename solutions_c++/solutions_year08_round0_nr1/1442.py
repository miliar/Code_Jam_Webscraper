#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

int getSwitches
(
	vector<string> * engines,	// engines
	vector<string> * searches	// search strings
) {

	// boundary cases
	if (engines->size() == 0 || searches->size() == 0) return 0;


	// search string pointer
	int pt = 0; 

	// switch counter
	int sc = 0;

	do
	{
		// switch to new engine
		sc++;

		// stores maximum traversal
		int mt = pt;

		// loop through available engines
		for (int i = 0; i < engines->size(); i++)
		{ 

			// temp pointer
			int tp = pt;

			// see how far we can go, based upon this choice
			for (; ; tp++)
				if (tp == searches->size() || (*searches)[tp]==(*engines)[i]) 
					break;

			// if we went further than all others
			if (tp > mt) mt = tp;

		}

		
		// record the maximal movement
		pt = mt;


	// check that the element pointer is valid
	} while (pt < searches->size());


	// return the lowest number of swtiches from this point forward
	return (sc - 1);

}

int main
(
	int argc,
	const char * argv[]
) {

	// get the file name
	const char * fname_in = argv[1];
	const char * fname_out = argv[2];

	// open the file
	ifstream infile(fname_in);
	ofstream outfile(fname_out);

	// for parsing
	string tmp;

	// get the number of search rounds
	getline(infile, tmp, (char)'\n');
	int rounds = atoi(tmp.c_str());
	cout << "Rounds : " << rounds << endl;

	// loop through rounds
	for (int i = 0; i < rounds; i++)
	{

		cout << "--> Round " << (i+1) << endl;

		// stores engines and searches for the current round
		vector<string> engines;
		vector<string> searches;
	
		// get the number of engines in the current round
		getline(infile, tmp, (char)'\n');
		int e = atoi(tmp.c_str());
		cout << "--> Engines : " << e <<  endl;

		// read the engines 1 by 1
		for (int j = 0; j < e; j++)
		{
			getline(infile, tmp, (char)'\n');
			engines.push_back(tmp);
		}

		// print out engines
		for (int j = 0; j < engines.size(); j++)
			cout << "\t" << engines[j] << endl;

		// get the number of searches in the current round
		getline(infile, tmp, (char)'\n');
		int s = atoi(tmp.c_str());
		cout << "--> Searches : " << s <<  endl;

		// read the searches 1 by 1
		for (int j = 0; j < s; j++)
		{
			getline(infile, tmp, (char)'\n');
			searches.push_back(tmp);
		}

		// priont out searches
		for (int j = 0; j < searches.size(); j++)
			cout << "\t" << searches[j] << endl;

		// get the solution
		outfile << "Case #" << (i+1) << ": " << getSwitches(&engines, &searches) << endl;

	}

	infile.close();
	outfile.close();

}
