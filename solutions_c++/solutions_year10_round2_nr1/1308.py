// Problem A: (Round 1B, Google Code Jam 2010)
// Author: Su Shi (Carmack.Shi@gmail.com)
// Usage: [execute] < inputfile > outputfile

#include <iostream>
#include <vector>
#include <string>
#include <set>
using namespace std;

int NumberOfMkDirs(set<string>& exist_path, const vector<string>& new_paths) {

  int count = 0;

  for (int i = 0; i < new_paths.size(); ++i) {
    string new_path = new_paths[i];

    while (!new_path.empty()) {
      if (exist_path.find(new_path) != exist_path.end())
        break;

      ++count;
      exist_path.insert(new_path);

      size_t pos = new_path.find_last_of('/');
      new_path = new_path.substr(0, pos);
    }
  }

  return count;
}

int main() {

  int t, n, m;

  cin >> t;

  for (int i = 1; i <= t; ++i) {
    cin >> n >> m;

    set<string> exsit_paths;
    vector<string> new_paths;
    string path;

    for (int j = 0; j < n; ++j) {
      cin >> path;
      exsit_paths.insert(path);
    }

    for (int k = 0; k < m; ++k) {
      cin >> path;
      new_paths.push_back(path);
    }

    cout << "Case #"<< i << ": " << NumberOfMkDirs(exsit_paths, new_paths)
         << endl;
  }

  return 0;

}