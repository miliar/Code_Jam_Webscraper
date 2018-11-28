/*
 * Author:  chlxyd
 * Created Time:  2013/4/13 17:09:08
 * File Name: A.cpp
 */
#include<iostream>
#include<sstream>
#include<fstream>
#include<vector>
#include<list>
#include<deque>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<bitset>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cctype>
#include<cmath>
#include<ctime>
using namespace std;
const double eps(1e-8);
typedef long long lint;
#define clr(x) memset( x , 0 , sizeof(x) )
#define sz(v) ((int)(v).size())
#define rep(i, n) for (int i = 0; i < (n); ++i)
#define repf(i, a, b) for (int i = (a); i <= (b); ++i)
#define repd(i, a, b) for (int i = (a); i >= (b); --i)
#define clrs( x , y ) memset( x , y , sizeof(x) )
int pas( char a , char b , char c , char d ) {
    int s[5] ;
    int x = 0 , y = 0 , z = 0 ;
    s[1] = a ; s[2] = b ; s[3] = c ; s[4] = d ;
    repf( i , 1 , 4 ) {
        if ( s[i] == 'O' ) x ++ ;
        if ( s[i] == 'X' ) y ++ ;
        if ( s[i] == 'T' ) z ++ ;
    }
    if ( x + z == 4 ) return 2 ;
    if ( y + z == 4 ) return 1 ;
    return 0 ;
}
char s[10][10] ;
string solve() {
    int empty = 0 ;
    repf( i , 1 , 4 )
        repf( j , 1 , 4 )
            if ( s[i][j] == '.' )
                empty ++ ;
    int d ;
    repf( i , 1 , 4 ) {
        d = pas( s[i][1] , s[i][2] , s[i][3] , s[i][4] ) ;
        if ( d == 1 )
            return "X won" ;
        if ( d == 2 ) 
            return "O won" ;
        d = pas( s[1][i] , s[2][i] , s[3][i] , s[4][i] ) ;
        if ( d == 1 )
            return "X won" ;
        if ( d == 2 ) 
            return "O won" ;
    }
    d = pas( s[1][1] , s[2][2] , s[3][3] , s[4][4] ) ;
    if ( d == 1 )
        return "X won" ;
    if ( d == 2 ) 
        return "O won" ;
    d = pas( s[1][4] , s[2][3] , s[3][2] , s[4][1] ) ;
    if ( d == 1 )
        return "X won" ;
    if ( d == 2 ) 
        return "O won" ;
    if ( !empty ) return "Draw" ;
    return "Game has not completed" ;
}
int main(){
    int T ;
    freopen("A.out","w",stdout) ;
    scanf("%d" ,&T ) ;
    repf( t , 1 , T ) {
        repf( i , 1 , 4 ) {
            scanf("%s" , s[i] + 1 ) ;
        }
        printf("Case #%d: %s\n" , t , solve().c_str() ) ;
    }
}

