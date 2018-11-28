// prob2.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <algorithm>
#include <Windows.h>
using namespace std;
#define MAXN 1000
int _tmain(int argc, _TCHAR* argv[])
{
	SetCurrentDirectoryA("I:\\WorkStation\\GoogleCodeJam\\2011\\round0\\Debug");
	FILE * fin = fopen( "in.txt" , "r" );
	FILE * fout = fopen( "out.txt" , "w" );
	int T;
	fscanf( fin , "%d" , &T ); 
	long double * E = new long double[MAXN+1];
	long double * L = new long double[MAXN+1];
	long double * p = new long double[MAXN+1];
	p[0] = p[1] = 1;
	for( int i = 2 ; i <= MAXN ; i++ ) p[i] = i*p[i-1];
	E[0] = E[1] = 0;
	L[0] = L[1] = 0;
	for( int i = 2 ; i <= MAXN ; i++ ) 
	{
		E[i] = 1;
		for( int j = 1 ; j < i ; j++ )
			E[i] += (L[i-j]+E[j])/i;
		E[i] *= (double)i/(double)(i-1);
		L[i] = 0;
		for( int j = 1 ; j <= i ; j++ ) 
			L[i] += (E[j]+L[i-j])/i;
	}

	for( int t = 1 ; t <= T ; t++ )
	{
		int N;
		fscanf(fin,"%d",&N);
		double ans = 0;
		int * a = new int[N+1];
		for( int i = 1 ; i <= N ; i++ )
			fscanf( fin , "%d" , a+i );
		bool * m = new bool[N+1];
		memset( m , 0 , sizeof(bool)*(N+1) );
		for( int i = 1 ; i <= N ; i++ )
		{
			if( !m[i] )
			{
				int c = 0;
				int p = a[i];
				m[i] = true;
				do
				{
					c++;
					p = a[p];
					m[p] = true;
				}while( p != a[i] );
				ans += E[c];
			}
		}
		fprintf(fout,"Case #%d: %.6lf\n",t,ans);
	}
	return 0;
}

