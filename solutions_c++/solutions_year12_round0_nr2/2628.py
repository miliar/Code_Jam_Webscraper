#include <cstdio>
#include <vector>
#include <map>
#include <unordered_map>
#include <algorithm>
#include <queue>

using namespace std ;

void algo()
{
  int n,s,p ;
  scanf("%d %d %d",&n,&s,&p);
  int val, res = 0 ;
  vector<int> scores ;
  for( int i = 0 ; i < n ; i++ )
    {
      scanf("%d",&val);
      scores.push_back(val);
    }
  for( int sc : scores )
    {
      if( p*3-2 <= sc )
	res++ ;
      else
	if( s && p*3 <= sc + min(4,sc) )
	  {    
	    s-- ;
	    res++ ;
	  }
    }
  printf("%d",res);
}


int main()
{
  int t;
  scanf("%d",&t);
  for(int i = 1 ; i <= t ; i++ )
    {
      printf("Case #%d: ",i);
      algo();
      printf("\n");
    }
  return 0;
}
