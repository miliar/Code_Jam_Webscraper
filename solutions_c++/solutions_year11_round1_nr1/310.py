#include<iostream> 
#include<stdio.h> 
#include<set> 
#include<vector> 
#include<map> 
#include<string> 
#include<algorithm> 
#include<sstream> 
#include<string.h> 
#include<stdlib.h> 
#include<cmath> 
using namespace std ;
#define INF (int)1e9

int gcd(int a,int b) { return b ? gcd(b,a % b) : a ; }
bool solve(long long n,int pd,int pg)
{
 if(pg == 100 && pd != 100) return false ;
 if(pg == 0 && pd != 0) return false ;
 if(100 / gcd(pd,100) <= n) return true ;
 return false ;
}

int main()
{
 int runs ;
 cin >> runs ;
 for(int t = 1;t <= runs;t++)
 {
  long long n ;
  int pd,pg ;
  cin >> n >> pd >> pg ;
   
  if(solve(n,pd,pg)) printf("Case #%d: Possible\n",t) ;
  else printf("Case #%d: Broken\n",t) ; 
 }
 return 0 ;
}
