// round0.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <algorithm>
#include <Windows.h>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	SetCurrentDirectoryA("I:\\WorkStation\\GoogleCodeJam\\2011\\round0\\Debug");
	FILE * fin = fopen( "in.txt" , "r" );
	FILE * fout = fopen( "out.txt" , "w" );
	int T;
	fscanf( fin , "%d" , &T );
	for( int t = 1 ; t <= T ; t++ )
	{
		int N;fscanf( fin , "%d" , &N );
		int pO = 1 , pB = 1 , wO = 0 , wB = 0;
		int ans = 0;
		for( int i = 0 ; i < N ; i++ )
		{
			char s,e;
			int p;
			fscanf( fin , " %c %d" , &s , &p );
			if( s == 'O' )
			{
				int r = abs(p-pO) - wO;
				pO = p;
				wO = 0;
				if( r < 0 ) r = 0;
				r++;
				ans += r;
				wB += r;
			}else if( s == 'B' )
			{
				int r = abs(p-pB) - wB;
				pB = p;
				wB = 0;
				if( r < 0 ) r = 0;
				r++;
				ans += r;
				wO += r;
			}else __asm int 3;
		}
		fprintf( fout , "Case #%d: %d\n" , t , ans );
	}
	return 0;
}

