/* 
   Sebastian Arcila Valenzuela
   sebastianarcila@gmail.com
   2009
   @(#)TEMPLATE.c.tpl
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

const string w = "welcome to code jam";
const int MOD = 10000;
int main()
{
  int N;
  cin >> N;
  string line;
  getline(cin,line);
  for(int n = 1; n<=N; ++n)
    {
      getline(cin,line);
      int dp[w.size()+1][line.size()+1];
      memset(dp,0,sizeof dp);
      for(int j = 0; j<=line.size();++j)
	dp[0][j] = 1;
      for(int i = 1; i<=w.size();++i)
	{
	  for(int j = 1; j<=line.size();++j)
	    {
	      dp[i][j] = dp[i][j-1];
	      if(w[i-1] == line[j-1])
		dp[i][j] =(dp[i][j] + dp[i-1][j-1]) % MOD;
	    }
	}
      char buff[4];
      sprintf(buff,"%4d",dp[w.size()][line.size()]);
      for(int i = 0; i<4 && buff[i]==' ';++i)
	buff[i] = '0';
      printf("Case #%d: %s\n",n,buff);
    }
  return 0;
}
