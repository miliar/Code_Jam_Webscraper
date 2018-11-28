
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <list>

using namespace std;
int main (int argc, char * const argv[]) {
    
	ifstream input(argv[1], ifstream::in);
	
	int testsNb;
	string s;
	getline(input, s);
	istringstream stream(s);
	stream >> testsNb;
	
	ofstream outfile(argv[2]);
	
	cout << "Testing " << testsNb << " cases..." << endl;
	
	int cases = 0;
	while (input.good() && getline(input, s) && !input.eof()) {
		// Get number of candies
		int candies;
		istringstream(s) >> candies;
		// Get values of candies
		getline(input, s);
		char *tmp = strdup(s.c_str());
		char *token = strtok(tmp, " ");
		list<int> values;
		list<int>::iterator it;
		while (token != NULL) {
			values.push_back(atoi(token));
			token = strtok(NULL, " ");
		}	
		free(tmp);
		cases++;
		int total = 0;
		for (it = values.begin(); it != values.end(); it++) {
			total ^= *it;
		}
		if (total != 0) {
			outfile << "Case #" << cases << ": NO" << endl;
		}
		else {
			// Sort them into ascending order
			values.sort();
			// Remove smallest element
			values.pop_front();
			long long int maxi = 0;
			for (it = values.begin(); it != values.end(); it++) {				
				maxi += *it;
			}
			outfile << "Case #" << cases << ": " << maxi << endl;
		}
		
	}	
	
	input.close();
	outfile.close();
    return 0;
	
}
