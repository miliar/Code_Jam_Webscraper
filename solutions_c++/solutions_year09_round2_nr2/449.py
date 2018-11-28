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


string next_int(string n)
{
  if(!next_permutation(ALL(n)))
    {
      sort(ALL(n));
      string N ="" ;
      if(n[0] == '0')
	for(int i = 1; i<n.size(); ++i)
	  if(n[i] != '0')
	    {
	      swap(n[0],n[i]);
	      break;
	    }
      //      D(n);
      //D(n[1]);
      N += n[0];
      N += "0";
      //D(N);
      //next_permutation(n.begin()+1,n.end());
      for(int i = 1; i<n.size();++i)
	N += n[i];//,D(N);
      return N;
    }
  return n;
}
int main()
{
  int t;
  cin >> t;
  string number;
  getline(cin,number);
  for(int o = 1; o<= t; ++o)
    {
      printf("Case #%d: ",o);
      getline(cin,number);
      cout<< next_int(number)<<endl;
    }

  return 0;
}
// g++  .cc -o  -O3
