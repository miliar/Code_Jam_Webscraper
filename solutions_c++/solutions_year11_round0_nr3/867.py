#include <cstdio>
#include <vector>
#include <map>
#include <algorithm>

const int INF = 1000*1000*1000 ;
using namespace std ;

int main()
{
  int nb_t ;
  scanf("%d",&nb_t);
  for(int t = 0 ;t<nb_t;++t)
    {
      int nb_bb;
      scanf("%d",&nb_bb);
      int sum =0,mini=INF,sum2=0;
      for(int i = 0 ; i < nb_bb; i++)
        {
          int v ;
          scanf("%d",&v);
          sum+=v;
          sum2 ^= v;
          mini = min(mini,v);
        }
      printf("Case #%d: ",t+1);
      if(sum2)
        printf("NO\n");
      else
        printf("%d\n",sum-mini);
    }
  return 0 ;
}
  
