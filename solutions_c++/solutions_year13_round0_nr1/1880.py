#include<iostream>
#include<fstream>
#include<algorithm>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<list>
#include<cstdio>
#include<cstring>
#include<string>
#include<cmath>
#include<cstdlib>
#include<vector>
#include<climits>
#include<ctime>
#include<sstream>
#define mp       	make_pair
#define pb       	push_back
#define st       	first
#define nd       	second
#define wait     	getchar();getchar();
#define lint     	long long
#define KARE(a)	 	( (a)*(a) )
#define MAX(a,b) 	( (a)>(b) ? (a) : (b) )
#define MIN(a,b) 	( (a)<(b) ? (a) : (b) )
#define MAX3(a,b,c)	( MAX( a,MAX(b,c) ) )
#define oo	 		1e9
#define pii       	pair<int,int>
#define pll			pair<lint,lint>
#define pdd			pair<double,double>
#define y1			yy1
#define eps      	(1e-9)
#define esit(a,b)  	( abs( (a)-(b) ) < eps )
#define sol(a)		( (a)<<1 )
#define sag(a)		( sol(a)|1 )
#define orta(a,b)	( ( (a)+(b) )>>1 )
#define FILL(a,b)	( memset( a,b,sizeof a ) )
#define mxn       	1005
#define kontrol( x,y,c )		( mat[x][y]==c || mat[x][y]=='T' )
using namespace std;

int id,test;
int yon[4][2] = { {0,1},{0,1},{1,1},{1,-1} };
char mat[7][7];

void read(){
//	freopen( ".in" , "r" , stdin );
//	freopen( ".out" , "w" , stdout );
	for( int i=1 ; i<=4 ; i++ )		scanf( "%s" , mat[i]+1 );
	return;
}

bool check( char c ){

	int i,j,syc,syc2,syc3;

	syc2 = syc3 = 0;

	for( i=1 ; i<=4 ; i++ ){

		syc = 0;
		for( j=1 ; j<=4 ; j++ )		syc += kontrol( i,j,c );
		if( syc==4 )	return 1;

		syc2 += kontrol( i,i,c );
		syc3 += kontrol( i,4-i+1,c );
	}

	for( j=1 ; j<=4 ; j++ ){

		syc = 0;
		for( i=1 ; i<=4 ; i++ )		syc += kontrol( i,j,c );
		if( syc==4 )	return 1;

	}

	return syc2==4 || syc3==4;

}

void solve(){

	int i,j,f;

	scanf( "%d" , &test );

	for( id=1 ; id<=test ; id++ ){

		read();

		printf( "Case #%d: " , id );

		if( check( 'X' ) )	puts( "X won" );
		else
		if( check( 'O' ) )	puts( "O won" );
		else{

			f = 0;
			for( i=1 ; i<=4 ; i++ )
			for( j=1 ; j<=4 ; j++ )
				if( mat[i][j]=='.' )	f=1;

			if( f )		puts( "Game has not completed" );
			else		puts( "Draw" );

		}

	}

	return;
}

int main(){
	solve();
	return 0;
}
