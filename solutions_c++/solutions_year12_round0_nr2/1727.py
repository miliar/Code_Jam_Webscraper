#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<iostream>

using namespace std;
#define MAX 100

int check( int score, int &S, int P ){
	int k;
	if( score % 6 == 0 ){
		if( score/3 >= P )
			return 1;
		if( score != 0 && score/3 + 1 >= P && S > 0 ){
			S--;
			return 1;
		}
		return 0;
	}
	if( score % 6 == 4 ){
		k = (score + 2)/6;
		if( 2*k >= P )
			return 1;
		return 0;
	}
	if( score % 6 == 2 ){
		k = (score - 2)/6;
		if( 2*k + 1 >= P )
			return 1;
		if( 2*k + 2 >= P && S > 0 ){
			S--;
			return 1;
		}
		return 0;
	}
	if( score % 6 == 3 ){
		if( score/3 >= P )
			return 1;
		if( score/3 + 1 >= P && S > 0 ){
			S--;
			return 1;
		}
		return 0;
	}
	if( score % 6 == 1 ){
		k = (score - 1)/6;
		if( 2*k + 1 >= P )
			return 1;
		return 0;
	}
	if( score % 6 == 5 ){
		k = (score + 1)/6;
		if( 2*k >= P )
			return 1;
		if( 2*k + 1 >= P && S > 0 ){
			S--;
			return 1;
		}
		return 0;
	}
}

void performtest(){
	int i, N, S, P, result = 0, score;
	scanf( "%d %d %d", &N, &S, &P );
	for( i=0; i<N; i++ ){
		scanf( "%d", &score );
		result += check( score, S, P );
	}
	printf( "%d\n", result );
}

int main(){
	int tests;
	scanf( "%d", &tests );
	for( int i=1; i<=tests; i++ ){
		printf( "Case #%d: ", i );
		performtest();
	}
	return 0;
}