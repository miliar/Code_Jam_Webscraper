#include<cstdio>

#include<cstring>
#include<cmath>
#include<deque>
#include<vector>
#include<queue>
#include<string>
#include<set>
#include<map>
#include<algorithm>

#define MAXN 1001

#define ll long long
#define DIM int T , N , M , P , K ;
#define ITER int i , j , k  , l;
#define AUX int a , b , d , aux ;
#define MINIM 1000000000000000000LL
using namespace std;

DIM
AUX
ITER
/*
priority_queue <int , vector <int> , greater<int> > MaxHeap;
priority_queue <int> MinHeap;
deque <int> Deque;
//queue <int> Q;
vector <int > V;
*/

ll int A[MAXN] , number[MAXN] , coresp[MAXN] , base, distincte , next ;
ll int mins = 1000000000000LL ;
int len;
char s[MAXN] , c;

ll int convert ( ll int A[MAXN] , int base ) {
    ITER
    ll AUX
   ll int result = 0; 
      a = 1;
         
    for( i = N ; i >= 1 ;i --) {
           result += A[i] * a ;
           a *= base;
           }
           
    return result;
} 

int main ()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    
    scanf("%d\n",&T);
    
    for ( i = 1 ; i <= T ; ++i ) {
          
          for( k = 1 ; k <= MAXN ; ++k)
               coresp[k] = -1;
          
          int distincte = 0;
           c = '0';
          
          for( k = 1 ; k <= MAXN ; ++k)
               A[k] = 0;
          
          mins = MINIM;
          
          j = 0;
          
          while ( c != '\n' ) {
                scanf("%c",&c);
                s[j++] = c; 
                if ( c != '\n' ) 
                   if ( A[c] == 0 ) A[c] = 1 , distincte ++;
                
          }
    N = j - 1;
    base = distincte;
    if ( base == 1 ) base ++;
    next = 1;
    coresp[s[0]] = 1;
    next = 0;
    
    if ( i == 9 )
     a = b;
    
         
         for( l = 1 ; l <= N ; ++l ) {
         if ( coresp[s[l - 1]] == -1 ) coresp[s[l - 1]] = next , next ++; 
         if( next == 1 ) next = 2;
              number[l] = coresp[s[l - 1]];
         }
        
         printf("Case #%d: %lld\n",i,convert(number , base));
}
         
return 0;
}
