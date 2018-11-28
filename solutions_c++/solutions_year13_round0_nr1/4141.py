/*-------------------------------------------*/
//Author      : Mir Riyanul Islam (Riyan)  
//University  : AIUB                       
//E-mail      : mir_riyan@yahoo.com        
//Problem ID  : A                      
//Problem Name: Tic-Tac-Toe-Tomek
//Algorithm   : 
/*-------------------------------------------*/
#pragma comment( linker , "/STACK:16777216" )
#pragma warning( disable : 4786 )
#include <set>
#include <map>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>

//#define deBug
#define inOut

#define MS 100005
#define pnl puts( "" )
#define psp cout << " "
#define prnt( a ) cout << a
#define phl cout << "Hello World!!!"
#define prntln( a ) cout << a << endl
#define prntD( a ) printf( "%.3lf" , a )

using namespace std;

const int INF = 1 << 30;
const double EPS = 1e-11;
const double PI = 2 * acos( 0.0 );

int MAX( int a , int b ) { return a > b ? a : b;  }
int MIN( int a , int b ) { return a < b ? a : b;  }
void SWAP( int &a , int &b ) { int t = a; a = b; b = t; }
int GCD( int a , int b ) { while( b ) { b ^= a ^= b ^= a %= b; } return a; }

char grid[10][10];
bool flgDot , flgX , flgO;

bool isWin( int x , int y , char c ) {
	bool flg = true;
	int i , j;
	for( i = 0 ; i < 4 ; i++ ) {
		if( grid[x][i] == c || grid[x][i] == 'T' ) continue;
		else {
			flg = false;
			break;
		}
	}
	if( !flg ) {
		flg = true;
		for( i = 0 ; i < 4 ; i++ ) {
			if( grid[i][y] == c || grid[i][y] == 'T' ) continue;
			else {
				flg = false;
				break;
			}
		}
	}
	if( ( x == 1 || x == 2 ) && ( y == 1 || y == 2 ) && !flg ) {
		flg = true;
		if( x == y ) {
			for( i = 0 ; i < 4 ; i++ ) {
				if( grid[i][i] == c || grid[i][i] == 'T' ) continue;
				else {
					flg = false;
					break;
				}
			}
		}
		else {
			for( i = 0 , j = 3 ; i < 4 ; i++ , j-- ) {
				if( grid[i][j] == c || grid[i][j] == 'T' ) continue;
				else {
					flg = false;
					break;
				}
			}
		}
	}
	return flg;
}

bool isDot() {
	int i , j;
	for( i = 0 ; i < 4 ; i++ ) {
		for( j = 0 ; j < 4 ; j++ ) {
			if( grid[i][j] == '.' ) return true;
		}
	}
	return false;
}


bool isChk( char c ) {
	int i , j;
	bool flg = false;
	for( i = 0 ; i < 4 ; i++ ) {
			for( j = 0 ; j < 4 ; j++ ) {
				if( grid[i][j] == c ) {
					flg = isWin( i , j , c );
					if( flg == true ) return flg;
				}
			}
		}
	return flg;
}
int main() {

#ifdef inOut
	freopen( "A-large.in" , "r" , stdin );
	freopen( "A-large.out" , "w" , stdout );
#endif

	int tc , cn = 0 , i , j;
	scanf( "%d" , &tc );
	while( tc-- ) {
		for( i = 0 ; i < 4 ; i++ ) {
			scanf( "%s" , &grid[i] );
		}

#ifdef deBug
		for( i = 0 ; i < 4 ; i++ ) {
			prntln( grid[i] );
		}
		pnl;
#endif
		printf( "Case #%d: " , ++cn );
		flgDot = isDot();
		flgX = isChk( 'X' );
		if( flgX ) {
			prntln( "X won" );
		}
		else {
			flgO = isChk( 'O' );
			if( flgO ) {
				prntln( "O won" );
			}
			else if( flgDot ) {
				prntln( "Game has not completed" );
			}
			else {
				prntln( "Draw" );
			}
		}
	}

	return 0;

}

