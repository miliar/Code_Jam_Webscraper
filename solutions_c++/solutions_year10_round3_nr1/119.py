#include<iostream>
#include<set>
#include<map>
#include<string>
#include<stdio.h>
#include<sstream>
#include<algorithm>
#include<sstream>
#include<queue>
#include<string.h>
using namespace std ;
int n,tree[100000] ; 
vector<int> g[10002] ;

void update(int k)
{
 while(k <= 10002)
 {
  tree[k] ++ ;
  k += k & - k ;       
 }
}

int query(int k)
{
 int ret = 0 ;
 while(k)
 {
  ret += tree[k] ;
  k -= k & -k ;        
 }
 return ret ;
}

main()
{
 int i,j,k,a,b,runs ;
 cin >> runs ;
 
 int test = 1 ;
 while(1)
 {
  cin >> n ;
  for(i=0;i<n;i++)
  {
   cin >> a >> b ;
   g[a].push_back(b) ;
  }
  memset(tree,0,sizeof tree) ;
  int ret = 0 ;
  for(i=1;i<=10000;i++)
  {
   for(j=0;j<g[i].size();j++)
    ret += query(10000 - g[i][j]) ;
   for(j=0;j<g[i].size();j++)
    update(10000 + 1 - g[i][j]) ;
  }
  printf("Case #%d: %d\n",test,ret) ;
  for(i=1;i<=10000;i++) g[i].clear() ;
  test ++ ;
  if(test > runs) break ;
 }
}
