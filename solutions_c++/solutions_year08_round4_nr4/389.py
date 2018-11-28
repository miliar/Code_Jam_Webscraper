#include<iostream>
#include<vector>
#include<algorithm>
using namespace std ;
int n,k ;
string s ;

int get(string &ss)
{
 int i,ret = 1 ;
 for(i=1;i<ss.size();i++) if(ss[i] != ss[i-1]) ret ++ ;
 return ret ;   
}

main()
{
 freopen("a.in","r",stdin) ;
 freopen("out.txt","w",stdout) ;

 int i,j,runs ;
 
 cin >> runs ;
 for(int t=1;t<=runs;t++)
 {
  cin >> k ;
  cin >> s ;
  n = s.size() ;
  
  int ret = n ;
  vector<int> temp ;
  for(i=0;i<k;i++) temp.push_back(i) ;
  do
  {
   string next ;
   
   for(i=0;i<n;i+=k)
    for(j=0;j<k;j++) 
     next.push_back(s[i+temp[j]]) ;                
   ret <?= get(next) ;                
  }
  while(next_permutation(temp.begin(),temp.end())) ;
  
  printf("Case #%d: %d\n",t,ret) ;
 }
// while(1) ;     
}
