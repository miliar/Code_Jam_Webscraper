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

typedef struct node
{
  string label;
  double val;
} node;

node tree[100];

bool closing(string &s)
{
  for (int i=0; i<s.size(); i++)
    if (s[i]!=')')
      return false;
  return true;
}

void readtree(int n)
{
  string s;
  while (true)
    {
      cin >> s;

      if (s.size()>1 && !closing(s)) 
	break;
      //      cout << "skipping " << s << endl;
    }

  int toadd;
  if (s[0]=='(')
    toadd=1;
  else
    toadd=0;

  const char *cstr=s.c_str()+toadd;

  if (s[s.size()-1]==')') //finished with number
    {
      s.resize(s.size()-1);
      sscanf(s.c_str()+toadd," %lf ",&(tree[n].val));
      //      printf("read from %s\n",s.c_str());
      tree[n].label.clear();
      //      cout << "node val " << tree[n].val << endl;
    }
  else
    {
      sscanf(cstr," %lf ",&(tree[n].val));
      //      cout << "node val " << tree[n].val << endl;

      cin >> s;
      if (s[0]==')')
	tree[n].label.clear();
      else
	{
	  //	  cout << " node label " << s << endl;
	  tree[n].label=s;
	  //	  cin >> s;

	  readtree(2*n+1);
	  readtree(2*n+2);
	}
    }
}

double getval(int n, set<string> &f)
{
  //  cout << "getvaling " << n << endl;
  if (tree[n].label.empty())
    return tree[n].val;

  if (f.find(tree[n].label) != f.end())
    {
      return tree[n].val*getval(2*n+1,f);
    }
  else
    {
      return tree[n].val*getval(2*n+2,f);
    }
}

int main()
{
  int _N;
  cin >> _N;

  int A,n,L;
  string s;
  set<string> features;

  cout << fixed;
  cout.precision(10);

  for (int _n=0; _n<_N; _n++)
    {
      cout << "Case #" << _n+1 << ":" << endl;

      cin >> L;
      readtree(0);

      while (true)
	{
	  cin >> s;
	  if (!closing(s))
	    break;
	}
      sscanf(s.c_str()," %d ",&A);
      //      cout << "A " << A << endl;;

      for (int i=0; i<A; i++)
	{
	  features.clear();
	  cin >> s >> n;
	  for (int j=0; j<n; j++)
	    {
	      cin >> s;
	      features.insert(s);
	    }
	  cout << getval(0,features) << endl;
	}
    }

  return 0;
}
