#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <string>
#include <cstdio>
#include <cctype>
#include <vector>
#include <cassert>
#include <iomanip>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long LL;
typedef pair<int,int> PI;
#define dbg(x) cout << #x << " -> " << (x) << "\t";
#define dbge(x) cout << #x << " -> " << (x) << "\n";

struct Circle
{
	int x,y,R;
};

int N;
Circle inp[3];

double getit ( Circle A , Circle B )
{
	LL dist = ( A.x - B.x )*( A.x - B.x ) + ( A.y - B.y )*( A.y - B.y );
	/*
	dbg(A.x) ; dbg(A.y) ; dbge(A.R);
	dbg(B.x) ; dbg(B.y) ; dbge(B.R);
	cout << (sqrt(dist) +A.R + B.R) << endl;
	*/
	return sqrt(dist) +A.R + B.R;
}

double check ( int mask )
{
	double res = 0;
	for ( int i=0;i<N;i++ ) if ( mask&(1<<i) )
	for ( int j=0;j<N;j++ ) if ( mask&(1<<j) )
		res = max ( res , getit ( inp[i] , inp[j] ) );
	return res;
}

int main()
{
	int kase_;
	cin >> kase_;
	for ( int kase=1;kase<=kase_;kase++ )
	{
		cin>> N;
		for ( int i=0;i<N;i++ )
			cin >> inp[i].x >> inp[i].y >> inp[i].R;
			
		double result = 1e20;
		for ( int mask=0;mask<(1<<N);mask++ ) 
			result = min ( result , max ( check ( mask ) , check (((1<<N)-1)^mask) ) );
		printf ( "Case #%d: %0.6lf\n" , kase , result/2 );
	}
	return 0;
}
