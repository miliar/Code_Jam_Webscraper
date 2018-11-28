#include <iostream>
#include <fstream>
#include <set>
using std::ifstream;
using std::cerr;	using std::cout;	using std::endl;
using std::set;
using std::string;

int main(int argc, char** argv) {
	ifstream infile(argv[1]);

	int num_cases;
	infile >> num_cases;

	for(int i = 0; i < num_cases; i++) {
		cout << "Case #" << i+1 << ": ";

		int num_engines;

		infile >> num_engines;
		cerr << "num_engines: " << num_engines << endl;
		infile.ignore(100, '\n');

		for(int j = 0; j < num_engines; j++) {
			char ch_name[101];
			infile.getline(ch_name, 102);
			cerr << ch_name << endl;
		}

		int num_queries;
		infile >> num_queries;
		infile.ignore(100, '\n');
		cerr << "num_queries: " << num_queries << endl;

		int num_switches = 0;
		set<string> encountered;

		for(int j = 0; j < num_queries; j++) {
			char ch_name[101];
			string name;
			infile.getline(ch_name, 102);
			name = ch_name;
			encountered.insert(name);
			cerr << encountered.size() << endl;
			if(encountered.size() == num_engines) {
				num_switches++;
				encountered.clear();
				encountered.insert(name);
			}
		}
		cout << num_switches << endl;
	}

	return 0;
}
