
#include <cstdio>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

struct node {
  map<string, node *> children;
};

node * root;

vector<string> parse(string filename)
{
  vector<string> path;
  unsigned idx = 1;
  unsigned ndx;
  while (idx < filename.size())
  {
    ndx = filename.find_first_of('/', idx);
    if (ndx == string::npos) ndx = filename.size();
    path.push_back(filename.substr(idx, ndx - idx));
    idx = ndx+1;
  }

  return path;
}

size_t add(vector<string> & path)
{
  node * n = root;
  size_t new_nodes = 0;
  for (size_t i = 0; i < path.size(); i++)
  {
    if (n->children.find(path[i]) == n->children.end())
    {
      n->children[path[i]] = new node();
      new_nodes++;
    }

    n = n->children[path[i]];
  }

  return new_nodes;
}

void clear(node * n = root)
{
  for (map<string, node *>::iterator it = n->children.begin(); it != n->children.end(); it++)
    clear(it->second);
  delete n;
}

void solve(int CASE)
{
  string pathname;
  vector<string> path;
  int n, m;
  cin >> n >> m;

  root = new node();

  for (size_t i = 0; i < n; i++)
  {
    cin >> pathname;
    path = parse(pathname);
    add(path);
  }

  size_t mkdirs = 0;
  for (size_t i = 0; i < m; i++)
  {
    cin >> pathname;
    path = parse(pathname);
    mkdirs += add(path);
  }

  clear();
  printf("Case #%d: %u\n", CASE, mkdirs);
}


int main()
{
  int t;
  cin >> t;
  for (int i = 1; i <= t; i++)
    solve(i);
}
