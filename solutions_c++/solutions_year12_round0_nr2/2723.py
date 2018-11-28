#include<iostream>
#include<cstdlib>
#include<cstdio>
#define MAXN 102
#define MAXP 35
using namespace std;

const int mp[ MAXP ] = 
  { 0 ,1 ,2 ,2 ,2 ,3 ,3 ,3 ,3 ,4 ,4 ,5 ,5 ,5 ,6 ,6 ,6 ,7 ,7 ,7 ,8 ,8 ,8 ,9 ,9 ,9 ,10 ,10 ,10 ,11 ,11 };
const int mt[ MAXP ] = 
  { 0 ,1 ,1 ,1 ,2 ,2 ,2 ,3 ,3 ,3 ,4 ,4 ,4 ,5 ,5 ,5 ,6 ,6 ,6 ,7 ,7 ,7 ,8 ,8 ,8 ,9 ,9 ,9 ,10 ,10 ,10 };
int n , s , p , ans;
int a[ MAXN ];
 
void count()
{
  for( int i = 1 ; i <= n ; ++ i )
    if( mt[ a[ i ] ] >= p )
      ++ ans;
    else if( mp[ a[ i ] ] >= p and s )
      { ++ ans; -- s; }

  return ;
}
/*
void init()
{
  int tmp , div;
  for( int i = 0 ; i <= 30 ; ++ i )
    {
      tmp = i;
      div = tmp / 3;
      
    }

  return ;
} 
*/
int main()
{
  int t , cnt , i;
  
  //init();
  
  cin>>t;
  cnt = 1;
  while( cnt <= t )
    {
      cin>>n>>s>>p;
      for( i = 1 ; i <= n ; ++ i )
        cin>>a[ i ];
      ans = 0;
      count();
      cout<<"Case #"<<cnt<<": "<<ans<<"\n";
      ++ cnt;
    }

  return 0;
}
