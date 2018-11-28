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
int board [ 110 ] [ 110 ];
int mov [][2] = { -1,0 , 0,-1 , 0,1 , 1,0 };
char tmp [ 110 ] [ 110 ];
int tmp1 [ 110 ] [ 110 ];
bool issink [ 110 ] [110 ];
bool isval ( int H , int W , int x ,int y )
{
     if ( x < 0 || y < 0 || x >= H || y >= W ) return false;
     return true;
}
void ident_sink (int H , int W)
{
     int i ,j,k ,dx,dy;
     bool fg = true;
     memset ( issink , false, sizeof ( issink ) ) ;
     for ( i = 0 ; i < H ; i++ ) for ( j = 0 ; j < W ;j++ )
     {
         fg = true;
         for ( k =0  ; k < 4 ;k++)
         {
             dx = i + mov [k][0] , dy = j + mov [k][1];
             if ( isval ( H ,W ,dx ,dy )  && board [ dx ] [dy] < board [i][j]) fg = false;
             
         }
         if ( fg ) issink [i][j] = true ;// cout << i << " "<<j<<"\n";
     }
     return ;
}
void assign_basin ( int H , int W )                  
{
      int i,j,k = 1; 
      for ( i = 0 ; i < 110 ; i++ ) for ( j = 0 ;j < 110 ; j++ ) tmp [i][j] =  tmp1 [i][j] = 0 ;
      char last = 'a';
      for ( i = 0 ;i < W ; i++ ) for ( j = 0 ; j < H ;j++ ) if ( issink [j][i] ) 
      { tmp [j][i] = last;last++;  tmp1 [j][i] =  k ;k++;}
      //for ( i = 0 ; i < H ; i++ ,cout <<"\n") for ( j = 0 ; j < W ;j++ ) cout << tmp1 [i][j]<<" ";
      return ;
}
int run ( int H , int W , int x , int y )
{
     int i ,j,k ,dx ,dy;
     k = 1<<29;
     if ( tmp1 [x][y] != 0 ) return tmp1 [x][y];
     for (i  =0 ; i < 4 ; i++ ) 
     {
         dx = x + mov [i][0] , dy = y + mov [i][1];
         if ( isval ( H ,W ,dx ,dy ) )
         {
              k = min ( k , board [dx][dy] );
         }
     }
     for ( i= 0 ; i < 4 ; i++ ) 
     {
         dx = x + mov [i][0] , dy = y + mov [i][1];
         if ( isval ( H ,W ,dx ,dy )  && board [dx][dy] == k )  return tmp1 [x][y] = run ( H ,W ,dx,dy ) ;
     }
}
void find_ans ( int H , int W ) 
{
     int i ,j,k;
     for ( i = 0 ; i < H ;i++ ) for ( j = 0 ; j < W ;j++ ) if ( tmp1 [i][j] == 0 )
         run ( H,W,i ,j );
     //for ( i = 0 ; i < H ; i++ ,cout <<"\n") for ( j = 0 ; j < W ;j++ ) cout << tmp1 [i][j]<<" ";
     map < int , char > used ; used.clear();
     char last = 'a';
     for ( i =0 ; i < H ;i++ ) for ( j = 0 ; j < W ;j++ ) 
     {
         k = tmp1 [i][j];
         if ( used.count( k ) )tmp [i][j] = used [k];
         else 
         {
              used [k] = last;
              tmp [i][j] = last;
              last++;
         }
     } 
     return ;
}
void output (int kase)
{
     cout << "Case #"<<kase<<":\n";
     return ;
}
int main ()
{
    int T, kase = 0; cin >> T;
    while ( T-- )
    {
          memset ( board , 0 ,sizeof ( board ) );
          int H , W ,i ,j ,k;
          cin >> H >> W;
          for ( i = 0 ; i < H ; i++ ) for ( j = 0 ;j < W ;j++ ) cin >> board [i][j];
          ident_sink ( H ,W );
          assign_basin ( H ,W );
          find_ans ( H ,W );
          output ( ++kase );
          for ( i = 0 ; i < H ;i++ ) 
          {
              cout << tmp [i][0];
              for ( j = 1 ; j < W ;j++ ) cout << " "<<tmp [i][j]; cout <<"\n";
          }
    }
    return 0;
}
          
          
