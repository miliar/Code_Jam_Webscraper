#include<cstdio>
#include<iostream>
#include<string.h>
#include<math.h>
#include<map>
#include<vector>
#include<vector>
#include<queue>
#include<utility>
#include<ctype.h>
#include<stdlib.h>
#define REP(i,n) for( i = 0 ; i < n ; i++ )
using namespace std ;
int main()
{
 int r ; 
 int c ;
 scanf("%d",&c);
 int l = 0 ; 
 while( c > 0 )
 {
  c--;
  l++;
 int x1 ;
 int x2 ;
 int y1 ;
 int y2 ;
 int j ;
 int k ;
 int i ;
 int x[201][201];
 int toBekilled[ 201][ 201] ;
 int toBeborn[201][201];
 REP(i,201)
 {
  REP(j,201)
  {
   x[i][j] = 0 ;
   toBekilled[i][j] = 0 ;
   toBeborn[i][j] = 0 ;
  }
 }
  scanf("%d",&r);
 REP(i,r)
 {
  scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
  for( j = y1 ; j <= y2 ; j++)
  {
   for( k = x1 ; k <= x2 ; k++ )
   {
    x[j+100][k+100] = 1 ;
   }
  }
 }
 int t = 0 ;
 int bact = 0 ;

 while(1)
 {
  bact = 0 ;
  for( i = 1 ; i <= 200 ; i++ )
  {
   for( j = 1 ; j <= 200 ; j++ )
   {

    if(x[i][j] == 1 && x[i-1][j] == 0 && x[i][j-1] == 0 )
    {
     toBekilled[i][j] = 1 ;
    }
    else if( x[i][j] == 0 && x[i-1][j] == 1 && x[i][j-1] == 1 )
    {
     toBeborn[i][j] = 1 ;
    }
   }
  }
  for( i = 1 ; i <= 200 ; i++ )
  {  
   for( j = 1 ; j <= 200 ; j++ )
   {
    if( toBekilled[i][j] == 1 )
    {
     x[i][j] = 0;
     toBekilled[i][j] = 0 ;
    }
    if( toBeborn[i][j] == 1 )
    {
     x[i][j] = 1;
     toBeborn[i][j] = 0 ;
    }

    if( x[i][j] == 1 )
    {
     bact++;
    }
   }
  }
  t++;
  if( bact == 0 )
  {
   break ;
  }
 }
 printf("Case #%d: %d\n",l,t);
 }
}
