// C.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

struct ways{
	int b, e, w;
};

#define MAXN 2000
ways way[ MAXN ];
int  x, s, r, n,ti, l;
double t;
double time;

bool cmp( ways way1, ways way2 ){
	return ( way1.w < way2. w );
}

void init(){
	cin >> x >> s >> r >> ti >> n;
	t = ti;
	int i;
	l = 0;
	for ( i = 1; i <= n; i ++ ){
		cin >> way[ i ].b >> way[ i ].e >> way[ i ].w;
		l += way[ i ].e - way[ i ].b;
	}
	sort( way+1, way+n+1, cmp );
}

void cal(){
	double run = (x-l)*1.0/r;
	time = 0;
	if ( run <= t ){
		time += run;
		t -= run;
	}
	else{
		time += t;
		time += (x-l-t*r)*1.0/s;
		t = 0;
	}
	int i, li, wi;
	for ( i = 1; i <= n; i ++ ){
		li = way[ i ].e - way[ i ].b;
		wi = way[ i ].w;
		run = li*1.0/(r+wi);
		if ( t > 0 ){
			if ( run <= t ){
				time += run;
				t -= run;
			}
			else{
				time += t;
				time += (li-t*(r+wi))*1.0/(s+wi);
				t = 0;
			}
		}
		else{
			time += (li)*1.0/(s+wi);
		}
	}
}

void print_(){
	printf( "%.10lf\n", time );
}

int _tmain(int argc, _TCHAR* argv[])
{
	freopen( "A-large.in", "r", stdin );
	freopen( "out.txt", "w", stdout );
	int c, i;
	cin >> c;
	for ( i = 1; i <= c; i ++ ){
		init();
		cal();
		cout << "Case #" << i << ": ";
		print_();
	}
	return 0;
}

