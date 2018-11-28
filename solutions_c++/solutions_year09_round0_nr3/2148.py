#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<sstream>
#include<set>
#include<map>

using namespace std;
void output (int kase)
{
     cout << "Case #"<<kase<<": ";
     return ;
}
char in [ 550 ] ,wel[] = "welcome to code jam";
int  mod = 10000 , memo [ 550 ] [ 20 ];
int recurse ( int pos , int idx  )
{
    if ( idx >= strlen ( wel ) || pos >= strlen ( in ) ) return 0;
    if ( memo [ pos ] [idx ] != -1 ) return memo [ pos ] [idx]%mod;
    if ( idx == strlen ( wel ) -1 ) 
    {
         if ( in [ pos ] == wel [ idx ] ) return memo [pos][idx] = 1 + recurse ( pos+1 , idx )%mod ;
         return memo [ pos ] [ idx ] = recurse ( pos+1 , idx  ) %mod;
    }
    int ans = 0;
    if ( wel [ idx ] ==  in [ pos ] ) 
         ans = recurse (pos+1 ,idx+1 )%mod;  
    ans += recurse ( pos+1, idx )%mod;
    return memo [ pos ] [ idx ] = ans%mod;
}

int main ()
{
    int T , kase = 0;
    cin >> T; 
    getchar();
    while ( T-- )
    {
          gets( in );
          int i ,j,k;
          output (++kase );
          memset ( memo , -1 ,sizeof ( memo ) ) ;
          k = recurse ( 0 , 0 );
          if ( k < 10 ) cout <<"000";
          else if ( k < 100 ) cout <<"00";
          else if ( k < 1000 ) cout <<"0";
          cout <<k<<"\n";
          //cout << recurse ( 0 ,0 ) <<"\n";
    }
    return 0;
}
