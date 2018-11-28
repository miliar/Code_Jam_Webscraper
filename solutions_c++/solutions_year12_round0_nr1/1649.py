#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<iostream>

using namespace std;
#define MAX 100

int map[26] = { 24, 7, 4, 18, 14, 2, 21, 23, 3, 20, 8, 6, 11, 1, 10, 17, 25, 19, 13, 22, 9, 15, 5, 12, 0, 16 };
char input[MAX+5], output[MAX+5];

void performtest(){
	char c;
	int len = 0;
	while( ( c = getchar() ) != '\n' )
		input[len++] = c;
	for( int i=0; i<len; i++ )
		if( input[i] != ' ' )
			output[i] = map[ input[i] - 'a' ] + 'a';
		else
			output[i] = ' ';
	output[len] = 0;
	printf( "%s\n", output );
		
}

int main(){
	int tests;
	scanf( "%d", &tests );
	getchar();
	for( int i = 1; i<=tests; i++ ){
		printf( "Case #%d: ", i );
		performtest();
	}
	return 0;
}