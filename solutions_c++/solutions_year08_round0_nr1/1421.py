#include <iostream>
#include <iterator>
#include <string>
#include <sstream>
#include <vector>
#include <set>
using namespace std;

int main(int argc, char *argv[])
{
    string line;
    getline(cin, line);
    istringstream iss(line);
    int num_cases;
    iss >> num_cases;

    for (int i = 0 ; i < num_cases ; ++i) {
	int num_switches(0);

	getline(cin, line);
	istringstream iss(line);

	int num_engines;
	iss >> num_engines;
	set<string> engines;
//cerr << "num_engines = " << num_engines << endl;
	for (int x = 0 ; x < num_engines ; ++x) {
	    string engine;
	    getline(cin, engine);
	    engines.insert(engine);
	}
#if 0
cerr << "engines = ";
std::copy(engines.begin(), engines.end(), ostream_iterator<string>(cerr, ","));
cerr << endl;
#endif
	getline(cin, line);
	int num_queries;
	istringstream iss2(line);
	iss2 >> num_queries;
	vector<string> queries;

	for (int x = 0 ; x < num_queries ; ++x) {
	    string query;
	    getline(cin, query);
	    queries.push_back(query);
	}

#if 0
cerr << "queries = ";
std::copy(queries.begin(), queries.end(), ostream_iterator<string>(cerr, ","));
cerr << endl;
#endif
	vector<vector<int> > available;

	vector<int> switches(num_engines, 0);
	for (int y = num_queries - 1 ; y >= 0 ; --y) {
	    set<string>::iterator iter = engines.find(queries[y]);
	    set<string>::iterator begin = engines.begin();

	    for (int x = 0 ; x < num_engines ; ++x) {
		++switches[x];
	    }
	    switches[distance(begin, iter)] = 0;

	    // FIXME ineficient
	    available.reserve(num_queries);
	    available.insert(available.begin(), switches);
	}

	int engine_num = -1;

	for (int y = 0 ; y < num_queries ; ++y) {
	    const vector<int> &switches = available[y];
#if 0
cerr << "switches = ";
std::copy(switches.begin(), switches.end(), ostream_iterator<int>(cerr, ","));
cerr << endl;
#endif
	    set<string>::iterator iter = engines.begin();
	    advance(iter, engine_num);
	    if (y == 0 ||  (*iter == queries[y])) {
		// Need to switch engines, find the minimum
		int max_index(-1);
		int max_val(-1);

		for (int i = 0 ; i < switches.size() ; ++i) {
		    if (i == engine_num) continue;
		    if (switches[i] > max_val) {
			max_val = switches[i];
			max_index = i;
		    }
		}
//cerr << "max_val = " << max_val << ", max_index = " << max_index << endl;

	    	if (max_index != engine_num) {
		    if (engine_num >= 0) { ++num_switches; }
		    engine_num = max_index;
//cerr << "setting engine_num to " << max_index << ", num_switches = " << num_switches << endl;
		}
	    }
	}

	cout << "Case #" << i + 1 << ": " << num_switches << endl;
    }

    return 0;
}
