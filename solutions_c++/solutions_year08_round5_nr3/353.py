#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
#include<queue>
#include<cmath>
#include<cstdio>
#include<sstream>
#include<algorithm>
using namespace std;


#define zz(a) ((int)(a.size()))
#define all(a) a.begin(),a.end()
#define MAX 10005

typedef long long ll;
typedef unsigned long long ull;
char a [100][100]; int N ,  M;
ll dp [1<<11][11];
int getbit( int mask , int pos ) 
{
    return (mask & (1<<pos)) > 0;    
}
ll bitcnt( int x ) 
{
    if(x==0 ) return 0;
    return 1 + bitcnt( x & ( x-1));     
}
int check ( int mask , int row )
{
              for( int j =0 ; j<M ; j++) 
              {  
                   if( getbit( mask , j ) && a[row][j] == 'x') return 0;    
                   if( j< M-1 && getbit( mask , j ) && getbit( mask , j + 1 ) ) return 0;
              }
                  return 1;
}

int doit( int mask , int row ) 
{
   
    if ( row == N ) return 0;
    if ( dp[mask][row] != - 1) return dp[mask][row];
    // cout<<N<<" "<<M<<" "<<row<<endl;
    ll ret = 0 ; 
    for ( int i =0  ; i<( 1<<M ) ; i++) 
     {
         if( !check ( i, row ) ) continue;
         int ok = 1;
         for( int j =0 ; j< M ; j++) 
          if( getbit( i, j ) )
          {
               if( j > 0  && getbit ( mask, j-1 ) ) ok = 0;
               if( j < M-1 && getbit ( mask, j+1 ) ) ok = 0;
          } 
         if( !ok ) continue;
         ret = max( ret,  bitcnt(i) +  doit( i, row + 1 ));
     }    
     return dp[mask][row]=ret;
}
int main ()
{
    int tc ; 
    cin>>tc;
    for( int cse = 1; cse <= tc; cse ++)
    {
        for( int i=0 ; i<( 1<<11 ) ; i++) 
         for( int j =0 ;j <11; j++) dp[i][j] = -1;
          cin>>N>>M;
          for( int i =0 ; i<N ;i++)
           for ( int j =0 ; j<M ; j++) 
            cin>>a[i][j];
            
          ll val = 0;
          for( int i =0 ; i< ( 1<< M ) ; i++) 
           {
               if( !check( i, 0 ) ) continue;
               val = max( val, bitcnt(i) + doit( i , 1) );
           }
          cout<<"Case #"<<cse<<": "<<val<<endl;
    }
return 0;    
}
