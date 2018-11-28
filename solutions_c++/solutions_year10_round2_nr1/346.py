#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <map>
#include <set>

using namespace std;

typedef long long ll;
typedef pair <int, int> pii;
typedef vector <int> vi;

int T;

vector <vector <string> > s;
vector <vector <string> > x;

int n, m;

char c[100100];

vector <string> getV()
{
  vector <string> res;
  int i = 1;
  int n1 = strlen(c);
  string y = "";
  while (i < n1)
  {
    if (c[i] == '/')
    {
      res.push_back(y);
      y = "";
    }
    else
      y += c[i];
    ++i;
  }
  res.push_back(y);
  return res;
}

struct Node
{
  string v;
  vector <Node *> ch;
  Node() {}
  Node(const string &s)
  {
    v = s;
  }
};

Node *tree;

vector <string> V;

Node *create(int st)
{
  Node *nd = new Node(V[st]);
  if (st == V.size() - 1)
    return nd;
  nd->ch.push_back(create(st + 1));
  return nd;
}

int add(Node *node, int st)
{
  if (st >= V.size()) return 0;
  for (int i = 0; i < node->ch.size(); ++i)
  {
    if (node->ch[i]->v == V[st])
    {
      return add(node->ch[i], st + 1);
    }
  }
  node->ch.push_back(create(st));
  return V.size() - st;

}

int main()
{
  scanf("%d", &T);
  for (int t = 0; t < T; ++t)
  {
    s.clear();
    x.clear();
    scanf("%d %d", &n, &m);
    gets(c);
    s.resize(n);
    x.resize(m);
    for (int i = 0; i < n; ++i)
    {
      gets(c);
      s[i] = getV();
    }
    for (int i = 0; i < m; ++i)
    {
      gets(c);
      x[i] = getV();
    }
    tree = new Node("root");
    for (int i = 0; i < n; ++i)
    {
      V = s[i];
      add(tree, 0);
    }
    int res = 0;
    for (int i = 0; i < m; ++i)
    {
      V = x[i];
      res += add(tree, 0);
    }
    printf("Case #%d: %d\n", t+1, res);
  }
  return 0;
}