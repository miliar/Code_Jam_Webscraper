#include<stdio.h>
int main()
{
 int t ;
 int g = 0 ;
 scanf("%d",&t);
 while( t > 0 ) 
 {
  t--;
  g++;
  printf("Case #%d: ",g);
 char str[ 101 ][ 101 ] ;
 int n; 
 int flagB = 0 ;
 int flagR = 0 ;
 int k ;
 int k1;
 int  j;
 int l ; 
 scanf("%d %d",&n,&k);
 int i ;
 char ch ;
 for( i = 0 ; i < n ; i++ )
 {
  scanf("%s",str[i]);
 }

 for( i = n - 1; i >= 0 ; i-- )
 {
  for( j = n-1 ; j >=0 ; j-- ) 
  {
   if( str[i][j] == 'B' || str[i][j] == 'R' )
   {
    for( k1 = j+1 ; k1 <  n ; k1++ )
    {
     if( str[i][k1] == '.' )
     {

     }
     else
     {
      k1--;
      break;
     }
    }
    if( k1 == n ) 
    {
     k1 = n-1 ;
    }
//    printf("%c %d %d %d %d\n",str[i][j], i,j,i,k1);

    ch  = str[i][j] ;
    str[i][j] = '.' ;
    str[i][k1] = ch ;
   }
  }

//  printf("\n");

 }
 
  
 for( i = 0 ; i < n ; i++ )
 {
  for( j = 0 ; j < n ; j++ )
  {
   for( l = 0 ; l < k ; l++ )
   {
    if(( i+l == n) || str[i+l][j] != 'B')
     break ;
   }
   if( l == k )
   {
    flagB = 1 ;
   }

   for( l = 0 ; l < k ; l++ )
   {
    if(( j+l == n ) || str[i][j+l] != 'B')
    {
     break;
    }
   }

   if( l == k )
   {
    flagB = 1 ;
   }

   for( l = 0 ; l  < k ; l++ )
   {
    if( str[i-l][j-l] != 'B' || ( i-l < 0 ) || ( j - l  < 0 ) )
    {
     break;
    }
   }
   if( l == k )
   {
    flagB = 1 ;
   }

   for( l = 0 ; l < k ; l++ )
   {
    if( str[i+l][j+l] != 'B' || ( i+l != n ) || ( j + l  != n ) )
    {
     break;
    }
   }
   if( l == k )
   {
    flagB = 1 ;
   }

   for( l = 0 ; l < k ; l++ )
   {
    if( str[i+l][j-l] != 'B' || ( i+l == n ) || ( j - l  < 0 ) )
    {
     break;
    }
   }
   if( l == k )
   {
    flagB = 1 ;
   }
     
   for( l = 0 ; l < k ; l++ )
   {
    if( str[i-l][j+l] != 'B' || ( i-l  < 0 ) || ( j + l  == n ) )
    {
     break;
    }
   }
   if( l == k )
   {
    flagB = 1 ;
   }

 
   for( l = 0 ; l < k ; l++ )
   {
    if(( i+l == n) || str[i+l][j] != 'R')
     break ;
   }
   if( l == k )
   {
    flagR = 1 ;
   }
   for( l = 0 ; l < k ; l++ )
   {
    if(( j+l == n ) || str[i][j+l] != 'R')
    {
     break;
    }
   }
   if( l == k )
   {
    flagR = 1 ;
   }

   for( l = 0 ; l  < k ; l++ )
   {
    if( str[i-l][j-l] != 'R' || ( i-l < 0 ) || ( j - l  < 0 ) )
    {
     break;
    }
   }

   if( l == k )
   {
    flagR = 1 ;
   }

   for( l = 0 ; l < k ; l++ )
   {
    if( str[i+l][j+l] != 'R' || ( i+l != n ) || ( j + l  == n ) )
    {
     break;
    }
   }

   if( l == k )
   {
    flagR = 1 ;
   }

   for( l = 0 ; l < k ; l++ )
   {
    if( str[i+l][j-l] != 'R' || ( i+l != n ) || ( j - l  < 0 ) )
    {
     break;
    }
   }
   if( l == k )
   {
    flagR = 1 ;
   }
     
   for( l = 0 ; l < k ; l++ )
   {
    if( str[i-l][j+l] != 'R' || ( i-l  < 0 ) || ( j + l  == n ) )
    {
     break;
    }
   }
   if( l == k )
   {
    flagR = 1 ;
   }

 
   for( l = 0 ; l < k ; l++ )
   {
    if(( i+l == n) || str[i+l][j] != 'R')
     break ;
   }
   if( l == k )
   {
    flagR = 1 ;
   } 
  }
 }
 if( flagB == 1 && flagR == 1 )
 {
  printf("Both\n");
 }
 else if( flagB == 1 )
 {
  printf("Blue\n");
 }
 else if( flagR == 1 )
 {
  printf("Red\n");
 }
 else 
 {
  printf("Neither\n");
 }
 }
}
