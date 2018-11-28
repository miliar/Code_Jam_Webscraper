// B.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <time.h>
#include <cmath>

using namespace std;

#define MAXN 1010
#define SQR(a) ( (a)*(a) )

int n, W, L;
int r[ MAXN ], x[ MAXN ], y[ MAXN ];

void init(){
	cin >> n >> W >> L;
	for ( int i = 1; i <= n; i ++ ){
		cin >> r[i];
		x[i]=0;
		y[i]=0;
	}
}

double dis( int i, int j ){
	return( sqrt( (double)( SQR(x[i]-x[j]) + SQR(y[i]-y[j]) ) ) );
}

bool ok(){
	int i, j;
	for ( i = 1; i <= n; i ++ )
		for ( j = i+1; j <= n; j ++ )
			if ( (double)(r[i]+r[j]) > dis(i,j) )
				return false;
	return true;
}


void fix(){
	int i, j, pick, p1, p2, move_x_, move_y_, d, R;
	for ( i = 1; i <= n; i ++ )
		for ( j = i+1; j <= n; j ++ )
			if ( (double)(r[i]+r[j]) > dis(i,j) ){
				//pick = rand() % 2;
				pick = 0;
				if ( pick == 0 ){
					p1 = i;
					p2 = j;
				}
				else{
					p1 = j;
					p2 = i;
				}
				R = r[i]+r[j];
				d = rand() % 4;
				switch (d){
				case 0:
					move_x_ = x[p2]+R;
					move_y_ = y[p1];
					break;
				case 1:
					move_x_ = x[p2]-R;
					move_y_ = y[p1];
					break;
				case 2:
					move_x_ = x[p1];
					move_y_ = y[p2]+R;
					break;
				case 3:
					move_x_ = x[p1];
					move_y_ = y[p2]-R;
					break;
				}
				if ( move_x_ >= 0 && move_y_ >= 0 && (move_x_) <= W && (move_y_) <= L ){
					x[p1] = move_x_;
					y[p1] = move_y_;
				}
			}
}

void f(){
	/*
	int i;
	while ( true ){
		for ( i = 1; i <= n; i ++ ){
			x[ i ] = rand() % w;
			y[ i ] = rand() % l;
		}
		if ( ok() )
			return;
	}
	*/
	while ( !ok() ){
		fix();
		/*
		for ( int i = 1; i <= n; i ++ )
			cout << " " << x[i] << " " << y[i];
		cout << endl;
		*/
		
	}
}


void cal(){
	srand( time( NULL ) );
	f();
	int i;
	for ( i = 1; i <= n; i ++ )
		cout << " " << x[i] << " " << y[i];
	cout << endl;

}

int _tmain(int argc, _TCHAR* argv[])
{
	freopen( "B-large.in", "r", stdin );
	freopen( "out.txt", "w", stdout );
	
	int t, i;
	scanf( "%d\n", &t );
	for ( i = 1; i <= t; i ++ ){
		init();
		cout << "Case #" << i << ": ";
		cal();
	}
	return 0;
}

