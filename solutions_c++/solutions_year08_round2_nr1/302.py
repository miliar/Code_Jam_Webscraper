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


int main()
{
   ifstream fin("A-large.in") ;
   ofstream fout("output.txt") ;
   int N ;
   long long n , A , B , C , D , xo , yo , M , i , k ;
   long long out ;
   fin >> N ;
   for(k=1;k<=N;++k)
   {
      fin >> n >> A >> B >> C >> D >> xo >> yo >> M ;
      out = 0 ; 
      vector<long long> tp(9,0LL) ;
      ++tp[ ((xo%3)*3) + (yo%3) ] ;
      for(i=1;i<n;++i)
      {      
         xo = ((A*xo) + B)%M ;
         yo = ((C*yo) + D)%M ;
         ++tp[ ((xo%3)*3) + (yo%3) ] ;
      }
      for(i=0;i<9;++i) out += (tp[i]*(tp[i]-1)*(tp[i]-2))/6 ;
      
      
      out += tp[0]*tp[1]*tp[2] ;
      out += tp[3]*tp[4]*tp[5] ;
      out += tp[6]*tp[7]*tp[8] ;
      
      out += tp[0]*tp[3]*tp[6] ;
      out += tp[1]*tp[4]*tp[7] ;
      out += tp[2]*tp[5]*tp[8] ;
      
      out += tp[0]*tp[4]*tp[8] ;
      out += tp[1]*tp[5]*tp[6] ;
      out += tp[2]*tp[3]*tp[7] ;
      
      out += tp[0]*tp[5]*tp[7] ;
      out += tp[1]*tp[3]*tp[8] ;
      out += tp[2]*tp[4]*tp[6] ;
      
      fout << "Case #" << k << ": " << out << endl ;

   }
   getchar() ;
   getchar() ;
   return 0 ;
}
