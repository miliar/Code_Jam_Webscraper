/*
  Sebastian Arcila Valenzuela
  sebastianarcila@gmail.com
  2010
  @(#)TEMPLATE.c.tpl
*/

/*#include <config.h>
  #include "p2.h"
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
  int s[30];
  s[2]= 1;
  s[3]= 2;
  s[4]= 3;
  s[5]= 5;
  s[6]= 8;
  s[7]= 14;
  s[8]= 24;
  s[9]= 43;
  s[10]= 77;
  s[11]= 140;
  s[12]= 256;
  s[13]= 472;
  s[14]= 874;
  s[15]= 1628;
  s[16]= 3045;
  s[17]= 5719;
  s[18]= 10780;
  s[19]= 20388;
  s[20]= 38674;
  s[21]= 73562;
  s[22]= 40265;
  s[23]= 68060;
  s[24]= 13335;
  s[25]= 84884;
  int t;
  cin >> t;
  for(int i = 1; i<= t;++i)
    {
      int n; 
      cin >> n;
      printf("Case #%d: %d\n",i,s[n]);
    }
  return 0;
}
//g++ p2.cc -O3 -o p2
