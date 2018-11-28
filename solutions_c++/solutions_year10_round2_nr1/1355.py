#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <map>

using namespace std;

class node {
  public:
    ~node();
    map<string, node *> children;
};

node::~node() {
  children.clear();
}

node *root = NULL;

void tokenize(string s, vector<string> &v) {
  v.clear();
  s.erase(s.begin());
  s += '/';
  istringstream iss(s, istringstream::in);
  string cur;
  do {
    getline(iss, cur, '/');
    if (!cur.empty()) {
      v.push_back(cur);
    }
  } while(!cur.empty());

}

void addpath(string path) {
  vector<string> v;
  tokenize(path, v);
  node *cn = root;
  for (size_t i = 0; i < v.size(); ++i) {
    map<string, node*>::iterator it = cn->children.find(v[i]);
    if (it != cn->children.end()) {
      cn = it->second;
    } else {
      node *nn = new node();
      cn->children[v[i]] = nn;
      cn = nn;
    }
  }
}

void dfs(node *n, vector<string> &v, int idx, int &ans) {
  if (idx == v.size()) return;
  map<string, node*>::iterator it = n->children.find(v[idx]);
  if (it != n->children.end()) {
    dfs(it->second, v, idx + 1, ans);
  } else {
    node *nn  = new node();
    n->children[v[idx]] = nn;
    ++ans;
    dfs(nn, v, idx + 1, ans);
  }
}

int main () {
  int T;
  cin >> T;
  for (int cc = 0; cc < T; ++cc) {
    root = new node();

    int N, M;
    cin >> N >> M;
    for (int i = 0; i < N; ++i) {
      string cur;
      cin >> cur;
      addpath(cur);
    }

    int ans = 0;
    for (int i = 0; i < M; ++i) {
      string cur;
      cin >> cur;
      vector<string> v;
      tokenize(cur, v);
      dfs(root, v, 0, ans);
    }

    cout << "Case #" << cc + 1 << ": " << ans << endl;

    delete root;
    root = NULL;
  }
}
