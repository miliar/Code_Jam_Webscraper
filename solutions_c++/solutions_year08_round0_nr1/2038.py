#include <iostream>
#include <string>
#include <set>
#include <list>

using namespace std;

int main() {
  int sets;
  int c0, c1;
  char input[102];
  set<string> engines, usable;
  list<string> queries;
  int switches;
  cin >> sets;
  for(c0 = 0; c0 < sets; ++c0) {
    engines.clear();
    for(cin >> c1, cin.getline(input, 100); c1--;) {
      cin.getline(input, 101);
      engines.insert(string(input));
    }
    for(cin >> c1, cin.getline(input, 100); c1--;) {
      cin.getline(input, 101);
      queries.push_back(string(input));
    }
    switches = 0;
    while (!queries.empty()) {
      usable = engines;
      while (usable.size() > 1 && !queries.empty()) {
	usable.erase(queries.front());
	queries.pop_front();
      }
      while (!queries.empty() && queries.front() != *usable.begin()) queries.pop_front();
      if (!queries.empty()) ++switches;
    }
    cout << "Case #" << c0 + 1 << ": " << switches << endl;
  }
  return 0;
}
