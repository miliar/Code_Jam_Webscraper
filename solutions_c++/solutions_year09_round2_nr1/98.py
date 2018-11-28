#include <cstdio>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std;

typedef long long int huge;
const int inf=0x3f2f1f0f;
const huge hinf=0x3fff2fff1fff0fffll;

#define foreach(i...) _foreach(i)
#define all(v) v.begin(), v.end()
#define _foreach(i, b, e) for(__typeof(b) i=b; i!=e; i++)

class tree
{
public:
  string v;
  double p;
  tree *l, *r;
  tree()
  {
    l=r=NULL;
  }
};

double calculate(tree* t, set<string> a, double p)
{
  p*=t->p;
  if (t->v.empty())
    return p;
  if (a.find(t->v)!=a.end())
    return calculate(t->l, a, p);
  return calculate(t->r, a, p);
}

tree *read()
{
  tree *t = new tree;
  char name[50];
  scanf(" ( %lf", &(t->p));
  if (scanf(" %[a-z]", name)==1)
    {
      t->v=string(name);
      t->l=read();
      t->r=read();
    }
  scanf(" )");
  return t;
}

void deltree(tree* t)
{
  if (t)
    {
      deltree(t->l);
      deltree(t->r);
      delete t;
    }
}

int main()
{
  int test;
  int n, m;
  char name[50];
  tree* t=NULL;
  set<string> animal;
  scanf(" %d", &test);
  for(int i=1; i<=test; ++i)
    {
      printf("Case #%d:\n", i);
      scanf("%*d");
      t=read();
      scanf(" %d", &n);
      for(int j=0; j<n; ++j)
	{
	  scanf(" %*[a-z] %d", &m);
	  animal.clear();
	  for(int k=0; k<m; ++k)
	    {
	      scanf(" %[a-z]", name);
	      animal.insert(string(name));
	    }
	  printf("%.7f\n", calculate(t, animal, 1.0));
	}
      deltree(t);
    }
  return 0;
}
