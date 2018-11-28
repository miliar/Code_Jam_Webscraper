// Q1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define INFILE "data.in"
#define OUTFILE "data.out"

using namespace std;

int p[100] = {2};
int k = 1;

int go( int a , int b ){
	for( int i = 0 ; i < k ; i++ ){
		while( ( a % p[i] ) == 0 && ( b % p[i] ) == 0 ){
			a /= p[i];
			b /= p[i];
		}
	}
	return b;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream inFile( INFILE );
	ofstream outFile( OUTFILE );
	int t, d, g;
	long long n;
	int a , b;
	int i, j;
	for( i = 3 ; i < 100 ; i++ ){
		for( j = 2 ; j < i ; j++ )
			if( !(i % j) ) break;
		if( !(i % j) ) p[k++] = i;
	}
	inFile >> t;
	for( int z = 0 ; z < t ; z++ ){
		inFile >> n >> d >> g;
		a = go( d , 100 );
		b = go( g , 100 );
		if( a > n || ( d < 100 && g == 100 ) || ( d > 0 && g == 0 ) ){
			outFile << "Case #" << z+1 << ": Broken" << endl;
		}else{
			outFile << "Case #" << z+1 << ": Possible" << endl;
		}
	}
	inFile.close();
	outFile.close();
	return 0;
}

