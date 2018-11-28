#include<vector>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<set>
#include<algorithm>
#include<sstream>
#include<queue>
#include<stack>
#include<string>
#include<cmath>
#include<map>
#include<fstream>

#define all(c) c.begin(), c.end()
#define allr(c) c.rbegin(), c.rend()
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define INF (int)1e9

using namespace std ;


double A[1004] , B[1004] ;
int N ;

int main()
{
   freopen("A-large.in","r",stdin) ;
   freopen("out.txt","w",stdout) ;
   int T ;
   scanf("%d",&T) ;
   for(int run=1;run<=T;++run)
   {
      cin >> N ;
      for(int i=0;i<N;++i) cin >> A[i] >> B[i] ;
      int out = 0 ;
      for(int i=0;i<N;++i) for(int j=i+1;j<N;++j)
      {
         double t = (A[i]-A[j])/(B[j]-B[i]+A[i]-A[j]) ;
         if(0 <= t && t <= 1) ++out ;
      }
      printf("Case #%d: %d\n",run,out) ;
   }
   return 0 ;
}
