#include <stdio.h>
#include <algorithm>
#include <cstring>
#include <stdlib.h>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <functional>
#include <numeric>
#include <utility>
#include <deque>
#include <stack>
#include <bitset>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <queue>
#include <limits>
#include <fstream>
#include <list>
#include <sstream>
#include <iostream>
#include <iomanip>

using namespace std;
#define MAX 5
char ady[ MAX ][ MAX ];

bool vict( char c ){
    int i , j;

    for( i = 0 ; i < 4 ; ++i )
        for( j = 0 ; j < 4 ; ++j ){
            if( ady[ i ][ j ] != c && ady[ i ][ j ] != 'T' ) break;
            if( j == 3 ) return 1;
        }

    for( i = 0 ; i < 4 ; ++i )
        for( j = 0 ; j < 4 ; ++j ){
            if( ady[ j ][ i ] != c && ady[ j ][ i ] != 'T' ) break;
            if( j == 3 ) return 1;
        }

    for( i = 0 ; i < 4 ; ++i ){
        if( ady[ i ][ i ] != c && ady[ i ][ i ] != 'T' ) break;
        if( i == 3 ) return 1;
    }

    for( i = 0 ; i < 4 ; ++i ){
        if( ady[ i ][ 3 - i ] != c && ady[ i ][ 3 - i ] != 'T' ) break;
        if( i == 3 ) return 1;
    }
    return 0;
}

bool complete(){
    int i , j;
    for( i = 0 ; i < 4 ; ++i ){
        for( j = 0 ; j < 4 ; ++j ){
            if( ady[ i ][ j ] == '.' ) return false;
        }
    }
    return true;
}



void solve(){
    bool winX = vict('X') , winO = vict('O');
    if( winX ) puts("X won");
    else if( winO ) puts("O won");
    else if( !complete() ) puts("Game has not completed");
    else puts("Draw");
}

int main(){
    int t, q , i,  j;
    freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
    scanf("%d" , &t );
    for( q = 1 ; q <= t ; ++q ){
        for( i = 0 ; i < 4 && scanf("%s" , ady[ i ] ) ; ++i );
        printf("Case #%d: " , q  );
        solve();
    }
    return 0;
}
