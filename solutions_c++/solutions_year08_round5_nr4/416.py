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
#define MAX 10007

typedef long long ll;
typedef unsigned long long ull;

int board[500][500];
int dp[500][500];
int doit( int x, int y )
{
    //cout<<x<<" "<<y<<endl;
    if( dp[x][y] != - 1) return dp[x][y];
    if( board [x][y] == 1 ) return 0;
    if( x == 1 && y == 1 ) return 1;
    int ret = 0 ;
    
    if( x > 2 && y >1 ) ret += doit( x-2, y-1 );
    if( x > 1 && y > 2 ) ret += doit( x-1, y-2);
    ret %= MAX;
    return dp[x][y] = ret;    
}
int main ()
{
    int tc ; 
    cin>>tc;
    for( int cse = 1; cse <= tc; cse ++)
    {
         int H , W , R;
         memset( board, 0, sizeof board );
         memset( dp, -1, sizeof dp);
         cin>>H>>W>>R;
         for( int i =0 ; i< R; i++) 
          {
              int p , q;
              cin>>p>> q;
              board[p][q] = 1;
          }
         
          
          cout<<"Case #"<<cse<<": "<< doit( H, W ) <<endl;
    }
return 0;    
}
