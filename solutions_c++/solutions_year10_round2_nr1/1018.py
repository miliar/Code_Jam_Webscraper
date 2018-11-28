#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

class Dir {
public:
  Dir() {
    subfolders.clear();
  }

  map<string, Dir> subfolders;

  void addSubFolder(vector<string> path) {
    string subfolder = path[0];

    addSubFolder(subfolder);
    path.erase(path.begin());

    if(path.size() > 0)
      subfolders[subfolder].addSubFolder(path);
  }

  void addSubFolder(string path) {
    if(!hasSubFolder(path))
      subfolders[path] = Dir();
  }

  bool hasSubFolder(string path) {
    map<string, Dir>::iterator it = subfolders.find(path);

    return it != subfolders.end();
  }

  int depth(vector<string> path) {
    if(path.empty())
      return 0;

    map<string, Dir>::iterator it = subfolders.find(path[0]);

    if(it == subfolders.end())
      return 0;

    path.erase(path.begin());

    return it->second.depth(path) + 1;
  }

  void printFolders(string path) {
    if(subfolders.empty()) {
      cout << path << endl;

      return;
    }

    for(map<string, Dir>::iterator it = subfolders.begin(); it != subfolders.end(); ++it)
      it->second.printFolders(path + "/" + it->first);
  }
};

vector<string> pathSplit(const string &path) {
  int start = 1;
  vector<string> res;

  for(unsigned int i = 1; i < path.size(); ++i)
    if(path[i] == '/') {
      res.push_back(path.substr(start, i-start));
      
      start = i+1;
    }

  res.push_back(path.substr(start));

  return res;
}

int main() {
  int t, m, n;

  cin >> t;

  for(int i = 0; i < t; ++i) {
    Dir root;
    unsigned int mkdirs = 0;

    cin >> n >> m;

    for(int j = 0; j < n; ++j) {
      string str;

      cin >> str;

      vector<string> spath = pathSplit(str);
      root.addSubFolder(spath);
      //root.printFolders("");

      //for(unsigned int k = 0; k < spath.size(); ++k)
      //  cout << spath[k] << endl;
    }

    for(int j = 0; j < m; ++j) {
      string str;

      cin >> str;

      vector<string> spath = pathSplit(str);


      mkdirs += (spath.size() - root.depth(spath));

      root.addSubFolder(spath);
    }

    cout << "Case #" << (i+1) << ": " << mkdirs << endl;
  }

  return 0;
}