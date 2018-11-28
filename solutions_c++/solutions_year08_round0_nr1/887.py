#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string> 
#include <vector>

using namespace std;


int main() {
  int num_cases;
  string line;
  getline (cin, line);
  {
    istringstream is (line);
    is >> num_cases;
  }
  for (int case_num  = 1; case_num <= num_cases; ++case_num) {
    int num_engines;
    getline (cin, line);
    {
      istringstream is (line);
      is >> num_engines;
    }
    map<string,int> enginemap;
    for (int i = 0; i < num_engines; ++i) {
      getline (cin, line);
      enginemap.insert (make_pair (line, enginemap.size()));
    }
    int num_queries;
    getline (cin, line);
    {
      istringstream is (line);
      is >> num_queries;
    }
    vector<int> queries;
    for (int i = 0; i < num_queries; ++i) {
      getline (cin, line);
      queries.push_back (enginemap[line]);
    }
    if (num_queries == 0) {
      cout << "Case #" << case_num << ": 0\n";
      continue;
    }
    
    vector<int> num_switches (num_engines,0);
    num_switches[queries[0]] = -1;
    for (int q = 1; q < num_queries; ++q) {
      int best_curr = 100000;
      for (int i = 0; i < num_engines; ++i) {
        if (num_switches[i] != -1) best_curr = min (best_curr, num_switches[i]);
      }
      vector<int> tmp (num_engines,-1);
      for (int i = 0; i < num_engines; ++i) {
        if (queries[q] == i) continue;
        if (num_switches[i] != -1) tmp[i] = min (num_switches[i], best_curr + 1);
        else tmp[i] = best_curr + 1;
      }
      tmp.swap (num_switches);
    }
    int ret = 100000000;
    for (int i = 0; i < num_engines; ++i) {
      if (num_switches[i] != -1) ret = min (ret, num_switches[i]);
    }
    cout << "Case #" << case_num << ": "<< ret << "\n";
  }

}
