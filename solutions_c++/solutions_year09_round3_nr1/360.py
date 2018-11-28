#include <algorithm>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <set>
#include <vector>
#include <cstdint>
#include <map>

using namespace std;

namespace {
  inline int64_t war(const string n) {
    string x = n;
    sort(x.begin(), x.end());
    x.resize(unique(x.begin(), x.end()) - x.begin());
    int64_t base = max(static_cast<int64_t>(2), static_cast<int64_t>(x.size()));
    //cerr << base << ": ";
    vector<int64_t> vals;
    map<char, int64_t> basemap;
    int nextbase = 1;
    for (int i = 0; i < n.length(); ++i) {
      int64_t next;
      if (basemap.find(n[i]) != basemap.end()) {
        next = basemap[n[i]];
      } else {
        next = nextbase;
        basemap[n[i]] = next;
        
        if (nextbase > 1)
          ++nextbase;
        else if (nextbase == 0)
          nextbase = 2;
        else if (nextbase == 1)
          nextbase = 0;
      }
      vals.push_back(next);
      //cerr << next << ", ";
    }
    //cerr << '\n';
    int64_t ret = 0;
    for (int i = 0; i < n.length(); ++i) {
      ret *= base;
      ret += vals[i];
    }
    return ret;
  }
}

int main(int argc, char *argv[]) {
  int ntrials = 0;
  cin >> ntrials;
  std::string line;
  for (int i = 1; i <= ntrials; ++i) {
    cin >> line;
    cout << "Case #" << i << ": " << war(line) << '\n';
  }
  return 0;
}

