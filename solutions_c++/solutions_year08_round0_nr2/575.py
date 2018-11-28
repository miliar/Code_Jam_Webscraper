#include<iostream>
#include<algorithm>
#include<string.h>

using namespace std;

#define maxn 1000100
#define maxm 30002
#define inf 1<<29
#define Max( a , b ) ((a) > (b)) ? a : b
#define Min( a , b ) ((a) < (b)) ? a : b

int na , nb , T;
int ea[200] , eb[200] , sa[200] , sb[200];
struct Node {
       int s , t;
       }A[200] , B[200];

int ch( char * x )
{
    int i = 0;
    i = ( (x[0] - '0' )*10 + x[1] - '0' )*60 + ( (x[3] - '0' )*10 + x[4] - '0' );
    return i;
}

void solve()
{
     int i , j , ta , tb;
     char s1[100] , s2[200];
     scanf("%d %d %d" , &T , &na , &nb );
     for( i = 0;i < na;i++ )
     {
          scanf("%s %s" , s1 , s2 );
          A[i].s = ch( s1 );
          A[i].t = ch( s2 );
          ea[i] = A[i].t;
          sa[i] = A[i].s;
     }
     for( i = 0;i < nb;i++ )
     {
          scanf("%s %s" , s1 , s2 );
          B[i].s = ch( s1 );
          B[i].t = ch( s2 );
          eb[i] = B[i].t;
          sb[i] = B[i].s;
     }  
     sort( sa , sa+na );
     sort( sb , sb+nb ); 
     sort( ea , ea+na );
     sort( eb , eb+nb ); 
     for( i = 0 , j = 0 , ta = 0;i < na;i++ )
     {
          if( j < nb && eb[j] + T <= sa[i] ){
              j++;continue;
          }
          ta++;
     }
     for( i = 0 , j = 0 , tb = 0;i < nb;i++ )
     {
          if( j < na && ea[j] + T <= sb[i] ){
              j++;continue;
          }
          tb++;
     }
     printf("%d %d\n" , ta , tb );
}

int main()
{
    int cas , i;
    scanf("%d" , &cas);
    for( i = 1;i <= cas;i++ )
    {
         printf("Case #%d: " , i );
         solve();
    }
    
    
    return 0;
}
