#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <utility>
#include <iterator>
#include <sstream>

#include <boost/algorithm/string/split.hpp>
#include <boost/algorithm/string/classification.hpp>
#include <boost/algorithm/string/join.hpp>

using namespace std;
using boost::algorithm::is_any_of;
using boost::algorithm::split;
using boost::algorithm::join;

int main()
{
  size_t NCASES;

  cin >> NCASES;

  for (size_t CASE = 0; CASE < NCASES; CASE++) {
    unsigned int N, M;
    cin >> N >> M;

    string tmp;
    getline(cin, tmp);

    set<string> dirs;
    string line;
    for (size_t n = 0; n < N; n++) {
      getline(cin, line);
      vector<string> components;
      split(components, line, is_any_of("/"));

      string dir;
      for (unsigned int k = 1; k < components.size(); k++) {
        dir += "/" + components[k];
        dirs.insert(dir);
      }
    }

    size_t creations = 0;
    for (size_t m = 0; m < M; m++) {
      getline(cin, line);
      vector<string> components;
      split(components, line, is_any_of("/"));

      string dir;
      for (size_t z = 1; z < components.size(); z++) {
        dir += "/" + components[z];
        if (dirs.find(dir) == dirs.end()) {
          dirs.insert(dir);
          creations++;
        }
      }
    }
    
    cout << "Case #" << (CASE + 1) << ": " << creations << endl;
  }
}
