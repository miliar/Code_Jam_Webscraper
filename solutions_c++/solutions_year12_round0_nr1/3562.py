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
char MAP[ 256 ] ;
int main(int argc, char *argv[])
{
 string tr[ 4 ] ;
 tr[0] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
 tr[1] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
 tr[2] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
 tr[3] = "y qee" ;
 string rs[ 4 ] ;
 rs[0] = "our language is impossible to understand";
 rs[1] = "there are twenty six factorial possibilities";
 rs[2] = "so it is okay if you want to just give up";
 rs[3] = "a zoo" ;
 for( int i = 0 ; i < 4 ; i++ ){
   for( int j = 0 ; j < tr[i].size() ; j++ ){
      if( MAP[ tr[i][j] ] == 0){
	 MAP[ tr[i][j] ] = rs[i][j] ;
      }
      else if(( MAP[ tr[i][j] ] != rs[i][j] )){
	 cout << " Error !! \n" ;
      }
   }
 }
 MAP[ 'z' ] = 'q' ;
 MAP[ ' ' ] = ' ' ;
 int n = 0 ;
 si(n);
 getchar();
 for( int i = 0 ; i < n ; i++ ){
  string str ;
  getline( cin, str ); 
  cout << "Case #"<<i+1<<": ";
  for( int i = 0 ; i < str.size() ; i++ ) cout << MAP[ str[i] ] ;
  cout << endl ;
 }
 return 0 ;


}
