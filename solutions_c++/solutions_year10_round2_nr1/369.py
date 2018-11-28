#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <set>
#include <vector>
#include <list>
#include <algorithm>
#include <cmath>
#include <cfloat>
#include <string>

typedef unsigned long long ull;

#define FOR(i,n) for (int i=0; i<(n); i++)
#define ALL(v) (v).begin(),(v).end()
#define PV(v) for (int __i=0; __i<(v).size(); __i++) cout << (v)[__i] << " "; cout << endl;

using namespace std;

class Node
{
public:
  map<string,Node*> children;
  bool exists;
};

void DFS(Node *n, int &ret)
{
  if (!n->exists)
    ret++;
  for (map<string,Node*>::iterator i=n->children.begin(); i!=n->children.end(); i++)
    {
      //      cout << "checking " << i->first << endl;
      DFS(i->second,ret);
    }
}

void DFSDel(Node *n)
{
  for (map<string,Node*>::iterator i=n->children.begin(); i!=n->children.end(); i++)
    DFSDel(i->second);

  delete n;
}

int main()
{
  int _N;
  cin >> _N;

  int N,M;

  for (int _n=0; _n<_N; _n++)
    {
      cout << "Case #" << _n+1 << ": ";

      cin >> N >> M;
      Node *root=new Node;
      root->exists=true;

      for (int i=0; i<N; i++)
	{
	  string s;
	  cin >> s;

	  Node *c=root;
	  for (int j=1; j<s.size(); j++)
	    {
	      string dir;
	      while (s[j]!='/' && j<s.size())
		{
		  dir.push_back(s[j]);
		  j++;
		}
	      if (c->children.find(dir)==c->children.end())
		{
		  c->children[dir]=new Node;
		  c->children[dir]->exists=true;
		  c=c->children[dir];
		}
	      else
		c=c->children.find(dir)->second;
	    }
	}

      for (int i=0; i<M; i++)
	{
	  string s;
	  cin >> s;

	  Node *c=root;
	  for (int j=1; j<s.size(); j++)
	    {
	      string dir;
	      while (s[j]!='/' && j<s.size())
		{
		  dir.push_back(s[j]);
		  j++;
		}
	      if (c->children.find(dir)==c->children.end())
		{
		  c->children[dir]=new Node;
		  c->children[dir]->exists=false;
		  c=c->children[dir];
		}
	      else
		c=c->children.find(dir)->second;
	    }
	}

      int ret=0;
      DFS(root,ret);
      cout << ret;

      DFSDel(root);

      cout << endl;
    }

  return 0;
}
