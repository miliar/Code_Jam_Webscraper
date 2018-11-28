// prob3.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <Windows.h>


int _tmain(int argc, _TCHAR* argv[])
{
	SetCurrentDirectoryA("I:\\WorkStation\\GoogleCodeJam\\2011\\round0\\Debug");
	FILE * fin = fopen( "in.txt" , "r" );
	FILE * fout = fopen( "out.txt" , "w" );
	int T;
	fscanf( fin , "%d" , &T );
	for( int t = 1 ; t <= T ; t++ )
	{
		int N;
		fscanf(fin,"%d",&N);
		int min = 100000000;
		int sum = 0;
		int check = 0;
		for( int i = 1 ; i <= N ; i++ ) 
		{
			int temp;
			fscanf( fin , "%d" , &temp );
			sum += temp;
			check ^= temp;
			if( temp < min ) min = temp;
		}
		if( check ) 
			fprintf( fout , "Case #%d: NO\n" , t );
		else
			fprintf( fout , "Case #%d: %d\n" , t , sum-min );
	}
	return 0;
}

