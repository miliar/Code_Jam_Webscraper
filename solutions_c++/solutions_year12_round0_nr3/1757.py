#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<iostream>

using namespace std;

int arr[10];

int length( int A ){
	int len = 0;
	while( A > 0 ){
		A /= 10;
		len++;
	}
	return len;
}

bool check( int temp, int *arr, int head ){
	for( int i=0; i<head; i++ )
		if( arr[i] == temp )
			return false;
	return true;
}

void performtest(){
	int i, j, A, B, temp, head = 0;
	long long result = 0;
	scanf( "%d %d", &A, &B );
	int len = length( A );
	int multi = pow( 10, len - 1 );
	for( i=A; i<B; i++ ){
		temp = i;
		head = 0;
		for( j=1; j<len; j++ ){
			temp = (temp%10)*multi + temp/10;
			if( temp > i && temp <= B && check( temp, arr, head ) ){
				arr[head++] = temp;
				result++;
			}
		}
	}
	printf( "%lld\n", result );
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