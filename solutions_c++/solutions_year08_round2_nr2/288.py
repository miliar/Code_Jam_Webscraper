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

bool np[10010] ;

int prs[10010] ;
int ptr ;
int pre[1000001] ;

void gtpr()
{
   int i , j ;
   for(i=2;i<=10010;++i) if(!np[i])
   {
      prs[ptr++] = i ;
      for(j=i+i;j<=10010;j+=i) np[j] = true ;
   }
}

int gp(int node)
{
   return pre[node]==node ? node : pre[node] = gp(pre[node]) ;
}


int main()
{
   int N ;
   int i , j , k , m , out ;
   int A , B , P ;
   gtpr() ;
   ifstream fin("B-small-attempt0.in") ;
   ofstream fout("output.txt") ;
   fin >> N ;
   for(k=1;k<=N;++k)
   {
      fin >> A >> B >> P ;
      out = 0 ;
      for(i=A;i<=B;++i) pre[i] = i ;
      for(i=A;i<=B;++i) for(j=i+1;j<=B;++j) if(pre[i] != pre[j])
      {
         int tp = min(i,j) ;
         int tp2 = -1 ;
         for(m=0;m<ptr && prs[m]<=tp;++m) if( (i%prs[m]==0) && (j%prs[m]==0) ) tp2 = prs[m] ;
         if(tp2 >= P)
         {
            int pi = gp(i) ;
            int pj = gp(j) ;
            pre[pi] = pj ;
         }
      }
      for(i=A;i<=B;++i) if(pre[i] == i) ++out ;
      
      fout << "Case #" << k << ": " << out << endl ;
      
   }
   
   
   getchar() ;
   getchar() ;
   return 0 ;
}
