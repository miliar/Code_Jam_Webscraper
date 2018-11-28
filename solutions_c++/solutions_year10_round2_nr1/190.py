#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cassert>

using namespace std;

struct Node {
  map<string, int> children;
};

vector<Node> nodes;
int nNodes;

typedef map<string, int>::iterator It;

int createPath(const string& path) {
  int i = 1;
  int iNode = 0;
  int nCreated = 0;
  
  while (i < (int) path.length()) {
    int j = i;
    for (j = i; j < (int) path.length() && path[j] != '/'; j++) {}
    string child = path.substr(i, j - i);
    //cout << "child=" << child << endl;
    
    It it = nodes[iNode].children.find(child);
    if (it == nodes[iNode].children.end()) {
      it = nodes[iNode].children.insert(pair<string, int>(child, nNodes)).first;
      nCreated++;
      nNodes++;
      assert(nNodes <= (int) nodes.size());
    }
    iNode = (*it).second;
    //cout << "iNode=" << iNode << endl;

    i = j + 1;
  }
  return nCreated;
}

void resetNodes() {
  nodes.clear();
  nodes.resize(50000);
  nNodes = 1;
}

int main() {
  int nCases;
  string path;
  cin >> nCases;
  for (int iCase = 0; iCase < nCases; iCase++) {
    int n, m;
    cin >> n >> m;
    resetNodes();
    for (int i = 0; i < n; i++) {
      cin >> path;
      createPath(path);
    }
    int nCmd = 0;
    for (int i = 0; i < m; i++) {
      cin >> path;
      nCmd += createPath(path);
    }
    cout << "Case #" << iCase + 1 << ": " << nCmd << endl;
  }
  return 0;
}
