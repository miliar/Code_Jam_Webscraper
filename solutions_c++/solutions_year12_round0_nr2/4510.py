#include<stdio.h>
#include<iostream>
#include<string.h>
#include<algorithm>
using namespace std;
int arr  ; 
int main ()
{
    int t,n,p,s,a,b,c,count,i,j,k,l,rem,div;
    scanf ("%d",&t);
    int test  = 1  ;
    while ( t -- )
    {
          count  = 0 ;
          scanf ("%d %d %d",&n, &s , &p ) ; 
          for ( i = 0 ; i < n ; i ++ ) 
          {
              cin >> arr;
              rem = arr % 3 ;
              div = arr / 3 ;  
              if ( rem == 2 ) 
              {
                   if ( (div + 1) < p && s > 0 )
                   {
                        if ( ( div + 2 ) >= p && ((3*div + 2) == arr) )
                        {
                             count ++ ; 
                             s--;
                        }
                   }
                   else if ( (div + 1)>=p && ((3*div + 2) == arr))
                   {
                        count ++ ;
                   }
              }
              else if ( rem == 1 )
              {
                   if ( (div+1) >= p && ((3*div + 1) == arr))
                   {
                        count ++ ;
                   }
              }
              else 
              {
                   if ( div >= p )
                      count ++  ;
                   else if ( (div +1 ) >= p && s > 0 && (arr>0 )   )
                   {
                        count ++ ; 
                        s -- ;
                   }
              }
              //cout << count << " " ; 
          }
          cout << "Case #"<<test<<": " << count << endl; 
          test ++ ;         
    }
    
}
