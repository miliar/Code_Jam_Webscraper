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

int main()
{
   freopen("A-large.in","r",stdin) ;
   freopen("out.txt","w",stdout) ;
   int T ;
   scanf("%d",&T) ;
   for(int run=1;run<=T;++run)
   {
      string str = "" ;
      cin >> str ;
      int ct = 0 ;
      vector<char> fnd ;
      for(int i=0;i<str.size();++i) if( find(all(fnd),str[i]) == fnd.end())
      {
         fnd.push_back(str[i]) ;
         ++ct ;
      }
      if(ct <= 1) ct = 2 ;
      int cur = 0 ;
      vector<bool> vis(str.size(),false) ;
      vector<int> out(str.size(),-1) ;
      vis[0] = true ;
      out[0] = 1 ;
      for(int j=1;j<str.size();++j) if(str[j] == str[0])
      {
         vis[j] = true ;
         out[j] = 1 ;
      }
      cur = 0 ;
      for(int i=0;i<str.size();++i) if(!vis[i])
      {
         vis[i] = true ;
         out[i] = cur ;
         for(int j=i+1;j<str.size();++j) if(str[j] == str[i])
         {
            vis[j] = true ;
            out[j] = cur ;
         }
         ++cur ;
         if(cur == 1) ++cur ;
      }
      
      /*
      for(int i=str.size()-1;i>=0;--i) if(!vis[i])
      {
         vis[i] = true ;
         out[i] = cur ;
         for(int j=i-1;j>=0;--j) if(str[j] == str[i])
         {
            vis[j] = true ;
            out[j] = cur ;
         }
         --cur ;
      }
      */
      long long outn = 0 ;
      for(int i=0;i<out.size();++i) outn = outn*ct + out[i] ;
      cout << "Case #" << run << ": " << outn << endl ;
   }
   //while(1) ;
   return 0 ;
}
