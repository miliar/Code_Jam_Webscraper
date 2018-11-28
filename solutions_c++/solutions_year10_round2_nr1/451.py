/* 
   Sebastian Arcila Valenzuela
   sebastianarcila@gmail.com
   2010
   @(#)TEMPLATE.c.tpl
 */

/*#include <config.h>
#include "file.h"
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

int main()
{
  int t;
  cin >> t;
  for( int i = 1; i<=t; ++i)
    {
      int ans = 0;
      set<string> ready;
      set<string> createme;
      int n,m;
      cin >> n >> m;
      string dum;
      for(int k = 0; k<n; ++k)
	{
	  cin >> dum;
	  int pos = 1;
	  while(pos >= 0)
	    {
	      ready.insert(dum.substr(0,pos));
	      pos = dum.find("/",pos+1);
	    }
	  ready.insert(dum);
	}
      string temp;
      for(int k = 0; k<m; ++k)
	{
	  cin >> dum;
	  int pos = dum.size();
	  while(pos > 0)
	    {
	      temp = dum.substr(0,pos);
	      if(ready.count(temp))
		break;
	      createme.insert(temp);
	      pos = dum.rfind("/",pos-1);
	    }
	  ready.insert(dum);
	}
      ans = createme.size();
      printf("Case #%d: %d\n",i,ans);
    }
  return 0;
}
//g++ file.cc -O3 -o file
