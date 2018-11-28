#include<cassert>
#include<set>
#include<math.h>
#include<stack>
#include<limits.h>
#include<map>
#include<iostream>
#include<cstdio>
#include<cstring>
#include<vector>
#include<queue>
#include<utility>
#include<algorithm>
#define REP(i,n) for(i=0;i<n;i++)
#define si(n) scanf("%d",&n)
#define sll(n) scanf("%lld",&n) 
#define sd(n) scanf("%lf",&n)
#define pll(n) printf("%l64d",n) 
#define ss(str) scanf("%s",str)
#define sf(n) scanf("%lf",&n)
#define pb push_back
#define LL long long int 
#define pi pair<int,int> 
#define fi first
#define se second
#define FOR(i,a,b) for(i = a ; i < b ; i++ )
using namespace std ;
int D[ 500 ][ 500 ] ;
char C[ 500 ][ 500 ] ;
int main(int argc, char *argv[])
{
 int t ;
 int l1 = 0 ;
 si(t);
 while( t -- > 0 ) 
 {
  l1++;
  int i ;
  int j ;
  REP(i,100 ) 
  {
   REP(j,100)
   {
    C[i][j] = 0 ;
    D[i][j] = -1 ;
   }
  }
  int c ;
  si(c);
  string str ;
  REP(i,c)
  {
   cin>>str;
   C[ str[0 ] ] [ str[1] ] = str[2] ; 
   C[ str[1] ] [ str[0] ] = str[2] ;
  }
  int d ;
  si(d);
  REP(i,d)
  {
   cin>> str;
   D[ str[0]  ] [ str[1] ] = 1 ;
   D[ str[1]  ] [ str[0] ] = 1 ;
  }
  int n ;
  si(n);
  cin>>str;
  stack<char> s ;
  FOR(i,0,str.size())
  {
   stack<char> s1 ;
   s.push(str[i]);
   if( s.size() == 1 ) continue ;
   char chA = s.top() ;
   s.pop();
   char chB = s.top() ;
   s.pop() ;
   if( C[ chA ][ chB ] != 0 ) 
   {
    s.push( C[ chA ][ chB ] ) ;
    continue ;
   }
   else
   {
    s.push( chB ) ;
    s.push( chA ) ;
   }
   s1.push( s.top() ) ;
   s.pop() ;
   while( !s.empty() ) 
   {
    if( D[ s.top() ] [ str[i] ] == 1 ) 
    {
 //    printf("XXXXXX:%d,%c\n",i,str[i]);
 //    cout<<str<<endl;
     break ;
    }
    s1.push( s.top() ) ;
    s.pop() ;
   }
   if( !s.empty() ) 
   {
    while( !s.empty() ) s.pop() ;
   }
   else
   {
    while( !s1.empty() ) 
    {
     s.push( s1.top() ) ;
     s1.pop() ;
    }
   }
  }
  vector<char> out ;
  while( !s.empty()) 
  {
   out.pb( s.top() ) ;
   s.pop() ;
  }
  reverse( out.begin() , out.end() ) ;
  printf("Case #%d: ",l1);
  printf("[");
  if( out.size() != 0 )
  {
   printf("%c",out[0] ) ;
   for( i = 1 ; i < out.size() ; i++ )
   {
    printf(", %c",out[i]);
   }
  }
  printf("]\n"); 
 }
}
