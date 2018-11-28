#include<vector>
#include<cstdio>
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

int L , D , N ;

string words[5001] ;
int ep[30] ;


int main()
{
   freopen("A-large.in","r",stdin) ;
   freopen("out.txt","w",stdout) ;
   scanf("%d%d%d",&L,&D,&N) ;
   for(int i=0;i<D;++i) cin >> words[i] ;
   for(int i=1;i<=N;++i)
   {
      string pat = "" ;
      cin >> pat ;
      int nep = 0 ;
      for(int i=0;i<pat.size();++i)
      {
         ep[nep] = 0 ;
         if(pat[i] == '(')
         {
            ++i ;
            while(pat[i] >= 'a' && pat[i] <= 'z') { ep[nep] |= (1<<(pat[i]-'a')) ; ++i ; }
         }
         else if(pat[i] >= 'a' && pat[i] <= 'z') ep[nep] |= (1<<(pat[i]-'a')) ;
         ++nep ;
      }
      int out = 0 ;
      for(int i=0;i<D;++i)
      {
         int j = 0 ;
         for(j=0;j<words[i].size();++j)
            if(!( ep[j] & ( 1<<( words[i][j]-'a' ) ) )) break ;
         if(j >= words[i].size()) ++out ;
      }
      printf("Case #%d: %d\n",i,out) ;
   }
   return 0 ;
}
