#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<queue>
#include<cmath>
#include<cstdio>
#include<sstream>
#include<algorithm>
using namespace std;

#define MAX 10005
int dp[MAX][2];

int M, V, a[MAX], c[MAX];
int getmin( int pos, int R )
{
   if( 2 * pos > M ) return a[pos] == R ? 0 : -2;
   
   if( dp[pos][R] != -1 ) return dp[pos][R];
   int ret = -2;
   int gg[2][2];
   for ( int req = 0 ; req <=1 ; req ++)
    for ( int side = 0; side <= 1 ; side ++)
        {
              int nside = 2*pos; 
              if( side == 1 ) nside ++;
              gg[side][req] = getmin( nside , req );           
        }
   
   #define update(b,c,add) {if((gg[0][b]!=-2&&gg[1][c]!=-2)&&(ret==-2||ret>gg[0][b]+gg[1][c]+add))ret=gg[0][b]+gg[1][c]+add;}  
   if( a[pos] == 1 ) // and 
   {
           if( R == 1 ) update( 1, 1, 0)  
           else {
                    update(1, 0, 0);
                    update(0, 1, 0);
                    update(0, 0, 0);
                }
   }
   else
   {
           if( R == 0 ) update ( 0, 0, 0)     
           else {
                    update(1, 0, 0);
                    update(0, 1, 0);
                    update(1, 1, 0);
                }
   }
   
   if( c[pos] )
   {
            if( a[pos] == 0 ) // and 
           {
                   if( R == 1 ) update ( 1, 1 , 1)     
                   else {
                            update(1, 0, 1);
                            update(0, 1, 1);
                            update(0, 0, 1);
                        }
           }
           else
           {
                   if( R == 0 ) update ( 0, 0, 1)     
                   else {
                            update(1, 0, 1);
                            update(0, 1, 1);
                            update(1, 1, 1);
                        }
           }       
   }
   
   return dp[pos][R]=ret; 
}
int main ()
{
    int tc ; 
    cin>>tc;
    for( int cse = 1; cse <= tc; cse ++)
    {
         for( int i =0 ; i<MAX; i++)
          for (int j =0 ;j<2; j++)
           dp[i][j] = -1;
          cin>>M>>V;
          for( int i = 1; i<= M; i++)
          {
           cin>>a[i];
           if(2*i <= M) cin>>c[i];
          }
          int val = getmin( 1, V );
          cout<<"Case #"<<cse<<": ";
          if( val == -2 ) cout<<"IMPOSSIBLE"<<endl;
          else cout<<val<<endl;
    }
return 0;    
}
