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


int L , P , C ;

int memo[1002][1002][12] ;

bool vis[12] ;

int main()
{
   freopen("B-small-attempt0.in","r",stdin) ;
   freopen("out.txt","w",stdout) ;
   int T ;
   scanf("%d",&T) ;
   for(int i=0;i<12;++i) vis[i]=false ;
   for(int run=1;run<=T;++run)
   {
      cin >> L >> P >> C ;
      if(!vis[C])
      {
         for(int g=1;g<=1000;++g) for(int s=1;s<=1000;++s)
         {
            if(s+g > 1001) continue ;
            if(s*C >= s+g-1) memo[s][s+g-1][C] = 0 ;
            else 
            {
               int & t = memo[s][s+g-1][C] ;
               t = (int)(1e9) ;
               for(int k=s+1;k<s+g-1;k+=2)
               {
                  int lf = memo[s][k][C] ;
                  int hf = memo[k][s+g-1][C] ;
                  if(lf < hf) lf = hf ;
                  ++lf ;
                  if(t > lf) t = lf ;
               }
               for(int k=s+2;k<s+g-1;k+=2)
               {
                  int lf = memo[s][k][C] ;
                  int hf = memo[k][s+g-1][C] ;
                  if(lf < hf) lf = hf ;
                  ++lf ;
                  if(t > lf) t = lf ;
               } 
            }
         }
         vis[C] = true ;
      }
      printf("Case #%d: %d\n",run,memo[L][P][C]) ;
   }  
   return 0 ;
}
