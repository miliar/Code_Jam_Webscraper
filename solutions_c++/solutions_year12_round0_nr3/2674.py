#include <cstdio>
#include <vector>
#include <set>
#include <unordered_map>
#include <algorithm>

using namespace std ;

set<pair<int,int> > recy[10] ;
  int A,B;

void recycle( int n)
{
  int p = 1,res=0 ;
  while( n >= p*10 )
    {
      res++;
      p *= 10 ;
    }
  int m = n ;
  for( int i = 0 ; i < res ; i++ )
    {
      const int c = n % 10 ;
      n = n/10 + c*p ;
      if( n < m && A<= n && n<= B )
	recy[res].insert(make_pair(n,m));
    }
}

void algo()
{
  for( int i = 0 ; i < 10 ; i++ )
    recy[i].clear();
  scanf("%d %d",&A,&B);
  for( int n = A ; n <= B ; n++ )
    recycle(n) ;
  size_t tot = 0 ;
  for( int i = 0 ; i < 10 ; i++ )
    tot += recy[i].size();
  printf("%d",tot);
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
