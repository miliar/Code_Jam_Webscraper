/* 
   Sebastian Arcila Valenzuela
   sebastianarcila@gmail.com
   2009
   @(#)TEMPLATE.c.tpl
 */

/*#include <config.h>
#include "alien.h"
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


set<string> dic;
void generate(const string & pattern, set<string> & macths)
{

  //  D(pattern);
  int i = pattern.find("(", 0 );
  if( i == string::npos ) 
    {
      macths.insert(pattern);
      return;
    }
  else
    {
      //      for(int i = 0; i< pattern.size(); ++i)
      //{
      //if(pattern[i] =='(')
      //{
      int j = pattern.find(")", 0 );
      //      string sub="";
      
      //for(j = i+1; j<pattern.size() && pattern[j]!=')';++j)
      //sub+=pattern[j];
      
      string newp =pattern.substr(0,i), end ="";
      //      D(newp);
      if(dic.count(newp)==0)
	return;
      if(j<pattern.size()-1)
	end=pattern.substr(j+1);
      
      for(int k = i+1; k<j;++k)
	generate(newp+pattern[k]+end, macths);
      //  i=j;
      //}
    }


}

int main()
{
  int L,D,N;
  scanf("%d %d %d",&L,&D,&N);
  dic.insert("");
  string temp;
  for(int i = 0; i<D;++i)
    {
      cin >> temp;
      dic.insert(temp);

      for(int j = 1; j<temp.size();++j)
	{
	  dic.insert(temp.substr(0,j));
	  //	  D((temp.substr(0,j)));
	}

    }
  string what;
  int ans;
  for(int i = 1; i<=N ; ++i)
    {
      cin>>what;
      set<string> all;
      generate(what,all);
      ans = 0;
      for(set<string>::iterator k=all.begin();
	  k!=all.end(); k++)
	if(dic.count((*k)))
	  ++ans;
	
      printf("Case #%d: %d\n",i,ans);      
    }
  return 0;
}
