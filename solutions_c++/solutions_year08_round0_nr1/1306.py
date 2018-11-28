#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <vector>

using namespace std;

// Engines
//
// This is simply a string -> unique integer ID map
// (IDs start at 0)
class Engines
{
  typedef map<string, int> EngineMap;
public:
  Engines(void) {}

  // insert: Add one more search engine
  void insert(const string& name) {
    names.insert(EngineMap::value_type(name, names.size()));
  }

  // find: Look up a search engine name, to find its ID
  int find(const string& name)
  {
    return names.find(name)->second;
  }
  
private:
  EngineMap names;
};



int main(void)
{
  istringstream sstr;
  string line;

  // Get number of test cases
  getline(cin, line);
  sstr.clear();
  sstr.str(line);
  int N;
  sstr >> N;             // N = number of test cases

  for (int test=1; test<=N; ++test) {
    // Read the list of search engines and create a map to id numbers for them
    Engines engines;
    int S;
    getline(cin, line);
    sstr.clear();
    sstr.str(line);
    sstr >> S;           // S = number of search engines

    for (int i=1; i<=S; ++i) {
      string name;
      getline(cin, name);
      engines.insert(name);
    }

    // Read all queries, mapping them to search engine id numbers.
    // The vector match tells which engine IDs have appeared so far
    // among the queries. Simultaneously matches is the number of
    // "true" values in match.
    // When all bits in match are set, we need to switch to another
    // search engine. When that happens, all bits in match are cleared,
    // except for the current id.
    vector<bool> match(S, false);
    int matches  = 0;
    int switches = 0;

    int Q;
    getline(cin, line);
    sstr.clear();
    sstr.str(line);
    sstr >> Q;           // Q = number of queries

    for (int i=1; i<=Q; ++i) {
      string query;
      getline(cin, query);
      int id = engines.find(query);

      if (!match[id]) {
	// Previously not found search engine name in query
	match[id] = true;
	++matches;

	if (matches == S) {
	  // All search engine names have been queried - we have to switch
	  ++switches;
	  match.assign(S, false);
	  match[id] = true;
	  matches = 1;
	}
      }
    }

    cout << "Case #" << test << ": " << switches << endl;
  }
}
