/* 
   Sebastian Arcila Valenzuela
   sebastianarcila@gmail.com
   2009
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>
#include <assert.h>
#include <stdarg.h>
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iterator>
#include <algorithm>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>

using namespace std;

/* DEBUG */
#define D(x) cerr<<__LINE__<<" "#x" "<<x<<endl
#define D_v(x) for(int i=0;i<x.size();cerr<<x[i++]<<" ")

#define ALL(x) x.begin(),x.end()

set<string> properties;
string tree;

double f(int i, int j)
{
  //printf("i = %d, j = %d\n", i, j);
  // printf("tree[i, j) = '%s'\n", tree.substr(i, j-i).c_str());
  assert(tree[i] == '(' && tree[j-1] == ')');
  stringstream sin(tree.substr(i+1, j-i-2));
  //  D(sin.str());
  double ans=1.0;
  sin >> ans;
  string property;
  if (sin >> property && property[0] != ')'){

    pair<int, int> left(-1, -1), right(-1, -1);

    int k = i+1;

    while (tree[k] != '(') k++;
    left.first = k++;
    for (int balance=1; balance != 0; k++){
      if (tree[k] == '(') balance++;
      if (tree[k] == ')') balance--;
    }
    left.second = k;

    while (tree[k] != '(') k++;
    right.first = k++;
    for (int balance=1; balance != 0; k++){
      if (tree[k] == '(') balance++;
      if (tree[k] == ')') balance--;
    }
    right.second = k;

    //    printf("property = %s\n", property.c_str());
    if (properties.count(property)){
      ans *= f(left.first, left.second);
    }else{
      ans *= f(right.first, right.second);
    }
  }
  return ans;
}

int main()
{
  int T;
  scanf("%d",&T);
  for(int t = 1; t<=T; ++t)
    {
      printf("Case #%d:\n",t);
      tree = "";
      int lines;
      scanf("%d",&lines);
      string line;
      getline(cin,line);
      while(lines--)
	{
	  getline(cin,line);
	  tree+=" "+line;
	  //	  D(tree);
	}

      while (tree[tree.size()-1] == ' ') tree.resize(tree.size()-1);
      int k = 0;
      while (tree[k] == ' ') k++;
      tree = tree.substr(k, tree.size());

      int animals;
      scanf("%d",&animals);

      while (animals--)
	{
	  string name;
	  cin >> name;
	  
	  int np;
	  cin >>np;
	  properties.clear();
	  string property;
	  while(np--)
	    {
	      cin >> property;
	      properties.insert(property);
	    }
	    
	  

	  
	  printf("%.7lf\n",f(0,tree.size()));
	}
    }
  return 0;
}
// g++  .cc -o  -O3
