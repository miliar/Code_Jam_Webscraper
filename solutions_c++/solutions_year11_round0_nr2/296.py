#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std ;
int res[26][26],bad[26][26] ;

int main()
{
 int runs ;
 cin >> runs ;
 for(int t = 1;t <= runs;t++)
 {
  memset(res,255,sizeof res) ;
  memset(bad,0,sizeof bad) ;
  int C,D ;
  cin >> C ;
  while(C--)
  {
   string S ;
   cin >> S ;
   res[S[0] - 'A'][S[1] - 'A'] = S[2] - 'A' ;
   res[S[1] - 'A'][S[0] - 'A'] = S[2] - 'A' ;
  }
  cin >> D ;
  while(D--)
  {
   string S ;
   cin >> S ;
   bad[S[0] - 'A'][S[1] - 'A'] = 1 ;
   bad[S[1] - 'A'][S[0] - 'A'] = 1 ;
  }
  
  int n ;
  cin >> n ;
  string s,ret ;
  cin >> s ;
  
  for(int i = 0;i < n;i++)
  {
   ret.push_back(s[i]) ;

   int sz = ret.size() ;
   while(sz > 1 && res[ret[sz - 1] - 'A'][ret[sz - 2] - 'A'] != -1)
   {
    int nchar = res[ret[sz - 1] - 'A'][ret[sz - 2] - 'A'] + 'A' ;
    ret.resize(ret.size() - 2) ;
    ret.push_back(nchar) ;
    sz = ret.size() ;
   }
   
   for(int i = 0;i + 1 < sz;i++)
    if(bad[ret[sz - 1] - 'A'][ret[i] - 'A'])
    {
     ret.clear() ;
     break ;
    }
  }
  
  printf("Case #%d: [",t) ;
  for(int i = 0;i < ret.size();i++)
  {
   if(i > 0) printf(", ") ;
   printf("%c",ret[i]) ;
  }
  printf("]\n") ;
 }
 return 0 ;
}
