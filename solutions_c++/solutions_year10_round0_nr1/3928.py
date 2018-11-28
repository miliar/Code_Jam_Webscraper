/* 
   Sebastian Arcila Valenzuela
   sebastianarcila@gmail.com
   2010
   @(#)TEMPLATE.c.tpl
 */

/*#include <config.h>
#include "snapper.h"
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
  int T;
  scanf("%d",&T);
  for(int i = 1,n,k; i<=T and scanf("%d%d",&n,&k) == 2; ++i)
    {
      int mask = 1<<n;
      mask--;
      printf("Case #%d: ",i);
      if( (k&mask) == mask)
	puts("ON");
      else
	puts("OFF");
	
    }
  return 0;
}
