#include <iostream>
#include <stdio.h>
#include <string>
#include <algorithm>

using namespace std;

string line ;

int list[101] ;
int per[101] ;
int q, p ;

int val()
{
      int sum = 0 ;
      int locks[10000] = {} ;
      for(int i=0;i<q;i++)
      {
	  int place = list[per[i]] ;
	  locks[place] = 1 ;
	  int j = place+1 ;
	  while(locks[j]==0 && j<= p)
	  {
		sum++ ;
		j++ ;
	  }
	  j = place -1 ;
	  while(locks[j] == 0 && j > 0)
	  {
		sum++ ;
		j-- ;
	  }

      }
      return sum ;
    
}

int main()
{
  int n ;

  scanf("%d\n", &n) ;
  

  for(int i=1;i<=n;i++)
  {
 
      scanf("%d %d\n", &p, &q) ;

      for(int j=0;j<q;j++)
	  scanf("%d", &list[j]) ;

      
      for(int j=0;j<q;j++)
	per[j] = j ;
      
      int cur = p*p ;
      do 
      {
	int v = val() ;
	if(v < cur )
	    cur = v ;
      } while( next_permutation(per, per+q) );
     
      cout << "Case #" << i << ": " << cur << endl ;


      
  }

  return 0;
}
