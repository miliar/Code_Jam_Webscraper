#include <cmath>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <vector>
using namespace std ;
int main ( )
{
 freopen ( "small.in" , "r" , stdin ) ;
 freopen ( "large.out" , "w" , stdout ) ;
  int t;
  cin>>t;
  for(int xx=1;xx<=t;xx++)
  {
      cout<<"Case #"<<xx<<": ";
      int n;
      cin>>n;
      int *ar=new int[n];
      int mis=0;
      for(int x=0;x<n;x++)
      {cin>>ar[x];if(x+1!=ar[x])mis++;}
      printf("%6lf\n",(double)mis);
  }
  return 0 ;
}
