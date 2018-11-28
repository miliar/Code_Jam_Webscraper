/*
  Sebastian Arcila Valenzuela
  sebastianarcila@gmail.com
  2010
  @(#)TEMPLATE.c.tpl
*/

/*#include <config.h>
  #include "picking.h"
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
int dp[55][55];
int main()
{
  int c;
  cin >> c;
  for(int C=1 ; C<=c ; ++C)
    {
      printf("Case #%d: ",C);
      int ans = 0;
      int n,K,b,t;
      cin >> n >> K >> b >> t;
      vector<int> x,v;
      for(int i = 0,temp; i<n; ++i)
        {
          cin >> temp;
          x.push_back(temp);
        }
      for(int i = 0,temp; i<n; ++i)
        {
          cin >> temp;
          v.push_back(temp);
        }


      vector<double> times;
      //D(t);
      for(int i = 0; i<n ; ++i)
        {
          double tt = (b-x[i]*1.0);
          tt = tt/(v[i]*1.0);
	  //D(tt);
          times.push_back(tt);
        }
      int swaps = 0, k = 0, rock = 0;
      for(int i = n-1; i>= 0 and k<K; --i)
	{
	  if(times[i] <= t)
	    {
	      ++k;
	      swaps += rock;
	    }
	  else
	    {
	      ++rock;
	    }
	}
      if(k!=K) puts("IMPOSSIBLE");
      else printf("%d\n",swaps);

      // memset(dp, 0, sizeof dp);
      // dp[0][0] = 0;
      // int k=0;
      // for(int i = 1; i<=n; ++i)
      //   {

      //     if(times[times.size()-1 - k] <= t)
      //       {
      // 	      k++;
      //         dp[i][k] = dp[i-1][k-1];
      //       }
      //     else
      //       {
      // 	      dp[i][k] = dp[i-1][k] + (n-k);
      //       }
      //     printf("    dp[%d][%d] = %d\n",i,k,dp[i][k]);
      // 	  if(k == K) D("OK");
      //   }


    }
  return 0;
}
//g++ picking.cc -O3 -o picking
