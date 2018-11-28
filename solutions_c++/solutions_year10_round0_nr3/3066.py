#include<cstdio>


int q[12] ;
int qptr ;

int main()
{
   int T ;
   freopen("C-small-attempt0.in","r",stdin) ;
   freopen("out.txt","w",stdout) ;
   scanf("%d",&T) ;
   for(int run=1;run<=T;++run)
   {
      int R , K , N ;
      scanf("%d%d%d",&R,&K,&N) ;
      for(int i=0;i<N;++i) scanf("%d",&q[i]) ;
      qptr = 0 ;
      int out = 0 ;
      for(int i=0;i<R;++i)
      {
         int t = K ;
         int no = 0 ;
         while(no<N && t-q[qptr]>=0)
         {
            ++no ;
            t -= q[qptr] ;
            out += q[qptr] ;
            ++qptr ;
            if(qptr >= N) qptr = 0 ;
         }
      }
      printf("Case #%d: %d\n",run,out) ;
   }
   return 0 ;
}
