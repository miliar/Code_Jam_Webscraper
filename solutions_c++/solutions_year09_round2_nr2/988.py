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


int main()
{
   freopen("B-large.in","r",stdin) ;
   freopen("out.txt","w",stdout) ;
   int T ;
   scanf("%d",&T) ;
   for(int run=1;run<=T;++run)
   {
      string str ;
      string out = "" ;
      cin >> str ;
      int arr[10] ;
      for(int i=0;i<10;++i) arr[i] = 0 ;
      for(int i=0;i<str.size();++i) ++arr[str[i]-'0'] ;
      int i = str.size()-1 ;
      
      for(;i>=0;--i)
      {
         int where = -1 ;
         int j = str[i]-'0'+1 ;
         for(;j<10;++j) if(arr[j] > 0)
         {
            char temp = str[i] ;
            int k = i+1 ;
            for(k=i+1;k<str.size();++k) if(str[k] == j+'0')
            {
               str[k] = temp ;
               str[i] = j+'0' ;
               where = i+1 ;
               break ;
            }
            if(k < str.size())
            {
               for(int m=where;m<str.size();++m) for(int n=where;n<str.size()-1;++n)
                  if(str[n] > str[n+1]) swap(str[n],str[n+1]) ;
               break ;
            }
         }
         if(j<10) break ;
      }
      if(i<0)
      {
         string out = "" ;
         for(int k=0;k<10;++k) if(arr[k] > 0)
         {
            for(int m=0;m<arr[k];++m) out.push_back(k+'0') ;
         }
         char fst ;
         for(int k=0;k<out.size();++k) if(out[k] > '0') { fst = out[k] ; out[k] = '0' ; break ; }
         out = fst + out ;
         str = out ;
      }
      cout << "Case #" << run << ": " << str << endl ;
   }
   
   return 0 ;
}
