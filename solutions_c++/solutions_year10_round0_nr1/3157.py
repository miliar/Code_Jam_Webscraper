#include<cstdio>

using namespace std ;

int main()
{
   int T ;
   freopen("A-large.in","r",stdin) ;
   freopen("out.txt","w",stdout) ;
   scanf("%d",&T) ;
   for(int run=1;run<=T;++run)
   {
      int N , K ;
      scanf("%d%d",&N,&K) ;
      ++K ;
      int p = 1<<N ;
      if((K/p)*p == K) printf("Case #%d: %s\n",run,"ON") ;
      else printf("Case #%d: %s\n",run,"OFF") ;
   }
   return 0 ;
}
