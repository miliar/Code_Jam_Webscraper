#include<iostream>
#include<string.h>
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
const int N = 1000005;

int a[1111];

inline int isok( int &tot , int k) {
       if( tot == 0 ) tot++;
       int min = 111111111 ,f = 0;
       for( int i = 0 ; i <= k;i++ ) {
            if( tot%a[i] != 0 ) {
                int tmp = ( a[i] - tot%a[i] );
                if( tmp < min ) min = tmp;
            }
       }
       tot += min;
       for( int i = 0 ; i <= k;i++ ) 
            if( tot%a[i] != 0 ) {
                return 0;
            }
       return 1;
}

inline int solve(int n){
       int  i , tot = 0 , res = 0;
       for( i = 0 ; i < n;i++ ) {
            if( tot == 0 || tot%a[i] ) {
                res ++;
                while( isok(tot , i) == 0 ) {
                       ;
                }
            }
       }
       printf("res = %d\n",res );
       return res;
}


inline int get( int n ) {
       for( int i = 0; i < n;i++ ) {
            a[i] = i + 1;   
       }
       int min  , max ;
       min = max = solve( n );
       while( next_permutation( a ,a + n ) ) {
              int ans = solve(n);
              if( ans > max ) max = ans;
              if( ans < min ) min = ans;
       }
       return max - min;
}

int p[50000] , cnt, vis[N];

void init() {
    int i ,  j ;
    cnt = 0;
    memset(vis, 0 , sizeof( vis ));
    for( i = 2; i < N;i++ ) {
         if( vis[i] == 0 ) p[cnt++] = i;
         else continue;
         if( N/i < i ) continue;
         j = i*i;
         while( j < N ) {
                vis[j] = 1; j += i;
         } 
    }
    memset( vis , 0 , sizeof( vis ));
    for( i = 0 ; i < cnt && p[i] * p[i] <= 1000 ;i++ ) {
         int t = p[i] * p[i] ;
         while( t < 1000 ) {
                vis[t] = 1; t *= p[i];
         }
    }
    a[1] = 0; a[2] = 1;
    for( i = 3; i <= 1000;i++ ) {
         a[i] = a[i-1] + vis[i];
    }
}

int main() {
    int test , i , j , n , m ,tc = 1;
    
    freopen("ss.in","r",stdin);
    freopen("s.out","w",stdout);
    init();
    scanf("%d",&test);
    while( test-- && scanf("%d",&n) != EOF ) {
           //n = tc;
           printf("Case #%d: ",tc++); 
           printf("%d\n",a[n]);
    }
    return 0;
}
