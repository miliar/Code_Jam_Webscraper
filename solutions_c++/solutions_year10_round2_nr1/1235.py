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


string names[100000] ;
vector<int> children[100000] ;
bool occ[100000] ;
int nxt ;


int add(string str)
{
   int st = 1 ;
   int en = -1 ;
   int ptr = 0 ;
   int out = 0 ;
   while(st<str.length())
   {
      en = str.find('/',st) ;
      if(en == string::npos) en = str.length() ;
      string toadd = str.substr(st,en-st) ;
      int f = 0 ;
      int sz = children[ptr].size() ;
      for(;f<children[ptr].size();++f)
      {
         if(occ[children[ptr][f]] && names[children[ptr][f]] == toadd)
         {
            ptr = children[ptr][f] ;
            break ;
         }
      }
      if(f >= sz)
      {
         ++out ;
         occ[nxt] = true ;
         names[nxt] = toadd ;
         children[ptr].push_back(nxt) ;
         ptr = nxt ;
         ++nxt ;
      }
      st = en + 1 ;
   }
   return out ;
}

int main()
{
   freopen("A-large.in","r",stdin) ;
   freopen("out.txt","w",stdout) ;
   int T ;
   scanf("%d",&T) ;
   for(int run=1;run<=T;++run)
   {
      int N , M ;
      scanf("%d%d",&N,&M) ;
      for(int i=0;i<100000;++i) { occ[i] = false ; children[i].clear() ; names[i] = "" ; }
      occ[0] = true ;
      names[0] = "" ;
      children[0].clear() ;
      nxt = 1 ;
      for(int i=0;i<N;++i)
      {
         string str ;
         cin >> str ;
         add(str) ;
      }
      int out = 0 ;
      for(int i=0;i<M;++i)
      {
         string str ;
         cin >> str ;
         out += add(str) ; 
      }
      printf("Case #%d: %d\n",run,out) ;
   }
   return 0 ;
}
