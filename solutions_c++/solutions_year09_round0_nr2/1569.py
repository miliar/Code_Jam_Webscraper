/* 
   Sebastian Arcila Valenzuela
   sebastianarcila@gmail.com
   2009
   @(#)TEMPLATE.c.tpl
 */

/*#include <config.h>
#include "water.h"
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

const int MAXH=101,MAXW=101;
int m[MAXH][MAXW];
int ans[MAXH][MAXW], actual;
int W,H;
void dfs(int i, int j)
{
  
  int minn = m[i][j];
  if(i>0 && m[i-1][j]<minn)
    minn = m[i-1][j];

  if(i<H-1 && m[i+1][j]<minn)//S
    minn = m[i+1][j];

  if(j>0 && m[i][j-1]<minn)
    minn = m[i][j-1];

  if(j<W-1 && m[i][j+1]<minn)
    minn = m[i][j+1];

  //  puts("ENTRE");
  //  D(ans[i][j]),D(i),D(j);
  if(minn == m[i][j])
    {
      if(ans[i][j]==0)
	{
	 
	  ans[i][j] = actual;
	  actual++;
	}
      return;
    }
  if(i>0 &&  minn == m[i-1][j])
    {
      if(ans[i-1][j]==0)
	dfs(i-1,j);
      ans[i][j] = ans[i-1][j];
    }
  else if(j>0 &&  minn == m[i][j-1])
    {
      if(ans[i][j-1]==0)
	dfs(i,j-1);
      ans[i][j] = ans[i][j-1];
    }
  else if(j<W-1 &&  minn == m[i][j+1])
    {
      if(ans[i][j+1]==0)
	dfs(i,j+1);
      ans[i][j] = ans[i][j+1];
    }
  
  else if(i<H-1 &&  minn == m[i+1][j])
    {
      if(ans[i+1][j]==0)
	dfs(i+1,j);
      ans[i][j] = ans[i+1][j];
    }
  
}
int main()
{
  int T;
  cin >> T;
  for(int t = 1; t<=T; ++t)
    {
      printf("Case #%d:\n",t);
      cin >> H >> W;
      memset(m , 0, sizeof m);
      memset(ans, 0, sizeof ans);

      actual = 'a';
      for(int i = 0; i<H;++i)
	for(int j = 0; j<W; ++j)
	  cin >> m[i][j];
	

      for(int i = 0; i<H;++i)
	{
	  for(int j = 0; j<W; ++j)
	    {
	      if(ans[i][j]==0)
		dfs(i,j);
	      
	      if(j!=0)
		printf(" ");
	      printf("%c",ans[i][j]);
	    }
	  puts("");
	}
    }
  return 0;
}
