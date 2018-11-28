#include <cstdio>
#include <vector>
#include <map>
#include <algorithm>

const int INF = 1000*1000*1000 ;
using namespace std ;

int v[1000] ;

int main()
{
  int nb_t ;
  scanf("%d",&nb_t);
  for(int t = 0 ;t<nb_t;++t)
    {
      int n ;
      int nb = 0;
      scanf("%d",&n);
      for(int  i= 0 ; i < n ; i++ )
        {
          scanf("%d",v+i);
          nb += v[i]==(i+1) ;
        }
      printf("Case #%d: %lf\n",t+1,double(n-nb));
    }
  return 0 ;
}
  
