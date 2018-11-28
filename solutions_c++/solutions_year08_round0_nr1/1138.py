

#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;



int saveUniverse(ifstream& in) {

	// get the number of search engines
	string str;
	getline(in, str);
	int nEngines = atoi(str.c_str());

	// read the names of the search engines
	string *engines = new string[nEngines];
	//bool *availableEngines = new bool[nEngines];

	// create string -> id mapping
	map<string, bool> availableEngines;

	for (int i = 0; i < nEngines; ++i) {
		getline(in, str);
		engines[i] = str;
		//availableEngines[i] = true;
		availableEngines[str] = true;
	}

	// now we read line by line, flagging engines as unavailable as we go
	getline(in, str);
	int nCases = atoi(str.c_str());
	int nAvailable = nEngines;
	int nSwitches = 0;
	cout << "Starting cases..." << endl;
	for (int i = 0; i < nCases; ++i) {
		getline(in, str);
		//cout << "Read: " << str << endl;

		// disable engine if this line is an existing search engine
		if (availableEngines.count(str) != 0 && availableEngines[str]) {
			availableEngines[str] = false;
			--nAvailable;

			// if no engines are left, we add a counter and switch to another one
			if (nAvailable == 0) {
				cout << "Last engine (" << str << ") used, switching on line " << i << "..." << endl;
				++nSwitches;

				// re-enable all search engines, except this one
				for (map<string, bool>::iterator it = availableEngines.begin(); it != availableEngines.end(); ++it) {
					availableEngines[it->first] = true;
				}

				// disable the current one again
				availableEngines[str] = false;
				nAvailable = nEngines - 1;
			}
		}
	}

	return nSwitches;
}


int main(int argc, char **argv) {

	// load file
	ifstream stream("A-large.in");

	// open write file
	ofstream out("output.txt");

	// read lines from file
	string str;
	getline(stream, str);

	// get the number of cases
	int nCases = atoi(str.c_str());

	// for each case
	for (int i = 0; i < nCases; ++i) {
		int switches = saveUniverse(stream);
		out << "Case #" << (i+1) << ": " << switches << endl;
		cout << "Case #" << (i+1) << ": " << switches << endl;
	}
	return 0;
};
