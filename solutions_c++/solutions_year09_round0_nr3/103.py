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

int memo[25][502] ;



string def = "welcome to code jam" ;
string inp = "" ;

int cal(int x,int y)
{
   if(x >= def.size()) return 1 ;
   if(y >= inp.size()) return 0 ;
   if(memo[x][y] != -1) return memo[x][y] ;
   int out = cal(x,y+1) ;
   if(def[x] == inp[y]) out = (out + cal(x+1,y+1)) % 10000 ;
   return memo[x][y] = out ;
}

int main()
{
   freopen("C-large.in","r",stdin) ;
   freopen("out.txt","w",stdout) ;
   int N = 0 ;
   scanf("%d\n",&N) ;
   for(int runs=1;runs<=N;++runs)
   {
      char in2[1002] ;
      gets(in2) ;
      inp.assign(in2) ;
      memset(memo,-1,sizeof memo) ;
      printf("Case #%d: %04d\n",runs,cal(0,0)) ;
   }
   return 0 ;
}
