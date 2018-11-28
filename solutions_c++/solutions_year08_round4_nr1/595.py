#include<vector>
#include<stdio.h>
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

int nd[10005][2] ;
int val[10005] ;
int M , V ;
int memo[10005][2] ;


int cal(int cur,int req)
{
   if(val[cur] == req) return 0 ;
   if(cur > M/2) return INF ;
   int out = INF ;
   if(nd[cur][1] == 0)
   {
      if(req == 0)
      {
         if(nd[cur][0] == 1)
         {
            out = min(cal(2*cur,0),cal(2*cur+1,0)) ;
         }
         else
         {
            out = cal(2*cur,0) + cal(2*cur+1,0) ;
         }
      }
      else
      {
         if(nd[cur][0] == 1)
         {
            out = cal(2*cur,1) + cal(2*cur+1,1) ;
         }
         else
         {
            out = min(cal(2*cur,1),cal(2*cur+1,1)) ;
         }
      }
   }
   else
   {
      if(req == 0)
      {
         if(nd[cur][0] == 1)
         {
            out = min(cal(2*cur,0),cal(2*cur+1,0)) ;
         }
         else
         {
            if(val[2*cur] != val[2*cur+1]) out = 1 ;
            else
            {
               out = 1 + min(cal(2*cur,0),cal(2*cur+1,0)) ;
            }
         }
      }
      else
      {
         if(nd[cur][0] == 1)
         {
            if(val[2*cur] != val[2*cur+1]) out =  1 ;
            else
            {
               out = 1 + min(cal(2*cur,1),cal(2*cur+1,1)) ;
            }
         }
         else
         {
            out = min(cal(2*cur,1),cal(2*cur+1,1)) ;
         }
      }
   }
   return memo[cur][req] = out ;
}



int main()
{
   int N ;
   int r ;
   int i ;
   int out ;
   ifstream fin("A-large.in") ;
   ofstream fout("output.txt") ;
   fin >> N ;
   for(r=1;r<=N;++r)
   {
      fin >> M >> V ;
      int tp = (M-1)/2 ;
      for(i=1;i<=tp;++i) fin >> nd[i][0] >> nd[i][1] ;
      for(;i<=M;++i) fin >> val[i] ;
      for(i=(M-1)/2;i>0;--i)
      {
         if(nd[i][0] == 0) val[i] = (val[2*i] | val[2*i+1]) ;
         else val[i] = (val[2*i] & val[2*i+1]) ;
      }
      memset(memo,-1,sizeof memo) ;
      out = cal(1,V) ;
      if(out >= INF) fout << "Case #" << r << ": IMPOSSIBLE" << endl ;
      else fout << "Case #" << r << ": " << out << endl ;
   }
   getchar() ;
   getchar() ;
   return 0 ;
}
