#include <cstdlib>
#include <string>
#include <sstream>
#include <iostream>
#include <iostream>
#include <fstream>
#include <map>
#include <algorithm>


using namespace std;


map<char, char> mapping;
string in_mapping  = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
string out_mapping = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";

void getmappings(const string& in, const string& out) {
	// clearing, just in case it's called more than once
	mapping.clear();

	// sanity check
	if (in.length() != out.length()) {
		cerr << "ERROR: mapping string length differs" << endl;
		exit(EXIT_FAILURE);
	}

	// get mapping from samples
	for (size_t i = 0; i < in.length(); ++i) {
		const map<char, char>::iterator& it = mapping.find(in[i]);
		if (it != mapping.end()) {
			//cout << "  (mapping already exists: \nmapping['" << in[i] << "']= '" << out[i] << "'" << endl;
			if (it->second != out[i]) {
				cerr << "ERROR: mapping already exists but characters differ:" << endl;
				cerr << "  - in:  " << it->first << endl;
				cerr << "  - out: " << it->second << endl;
				cerr << "  - new: " << out[i] << endl;
			}
		}
		mapping[in[i]] = out[i];
	}

	/*
	  Debug output
	 */
	cout << "Mapping (size of alphabet: " << mapping.size() << "):" << endl;
	string orig;
	string trans;
	for (map<char, char>::iterator it = mapping.begin(); it != mapping.end(); ++it) {
		orig  += it->first;
		trans += it->second;
	}
	cerr << " - Original language: [" << orig  << "]" << endl;
	cerr << " - Transl.  language: [" << trans << "]" << endl;

	string trans_sorted(trans);
	sort(trans_sorted.begin(), trans_sorted.end());
	cerr << " - Transl.  l sorted: [" << trans_sorted << "]" << endl;
}

int main(int argc, char* argv[])
{
	getmappings(in_mapping, out_mapping);
	mapping['q'] = 'z';
	mapping['z'] = 'q';

	string basename = "A-small-attempt4";
	ifstream input_file(string(basename + ".in").c_str());
	ofstream output_file(string(basename + ".out").c_str());

	string line;
	string line_out;

	if (input_file.is_open()) {
		getline(input_file, line); // consume first line
		int numlines = atoi(line.c_str());

		int counter = 0;
		while (input_file.good() && (counter < numlines)) {
			getline(input_file, line);

			cerr << " < line: " << line << endl;
			string transl(line);
			for (string::iterator it = transl.begin(); it != transl.end(); ++it) {
				char c = *it;
				*it = mapping.find(c)->second;
			}
			cerr << " > tran: " << transl << endl;

			output_file << "Case #" << ++counter << ": " << transl << endl;
			cout << "Case #" << counter << ": " << transl << endl;
		}
		input_file.close();
	} else {
		cerr << "ERROR: Unable to open file" << endl;
	}

	return 0;
}
