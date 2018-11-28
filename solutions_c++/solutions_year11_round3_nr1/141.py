#include <stdio.h>
#include <functional>
#include <bitset>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <string.h>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<string> vs;
typedef long long int64;

#define forit(a,b) for(typeof((b).end()) a=(b).begin();a!=(b).end();a++)
#define clr(a,b) memset(a,b,sizeof a)
#define all(a) a.begin(),a.end()
#define sorta(a) sort(all(a))

int N , M; 
char grid[ 55 ][ 55 ];
int mov[ 4 ][ 2 ] = { {0 , 0} , {1 , 0} , {0 , 1} , {1 , 1} };
string S = "/\\\\/";

bool color( int x , int y ){
	for( int d = 0 ; d < 4 ; d++ ){
		int dx = x + mov[ d ][ 0 ] , dy = y + mov[ d ][ 1 ];
		if( dx >= N || dy >= M || grid[ dx ][ dy ] != '#' ) return 0;
		grid[ dx ][ dy ] = S[ d ];
	}
	return 1;
}

int main(){

	int test;
	scanf( "%d" ,&test );
	for( int ttest = 1 ; ttest <= test ; ttest++ ){
		scanf( "%d%d\n" ,&N ,&M );
		for( int q = 0 ; q < N ; q++ ){
			scanf( "%s" ,grid[ q ] );
			for( int w = 0 ; w < M ; w++ ){
			}
		}
		bool good = 1;
		for( int q = 0 ; q < N ; q++ ){
			for( int w = 0 ; w < M ; w++ ){
				if( grid[ q ][ w ] == '#' ){
					bool can = color( q , w );
					if( can == 0 ){
						good = 0;
						goto end;
					}
				}
			}
		}
		end:;
		printf( "Case #%d:\n" ,ttest );
		if( good ){
			for( int q = 0 ; q < N ; q++ ){
				printf( "%s\n" ,grid[ q ] );
			}
		}
		else{
			printf( "Impossible\n" );
		}
	}
	return 0;
}
