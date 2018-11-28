/* C Libs */
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <climits>
#include <ctime>
/* IOstream Libs */
#include <iostream>
#include <fstream>
#include <sstream>
/* String Libs */
#include <string>
/* STL Containers */
#include <bitset>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>
/* STL Algorithm */
#include <algorithm>
/* Miscellaneous */
#include <complex>
#include <functional>
#include <iterator>
//#include <limits>
#include <numeric>
#include <typeinfo>
#include <utility>
#include <valarray>

using namespace std;

#define REP(i,s,t) for(int _t=t,i=s;i<_t;i++ )
#define REPP(i,s,t) for(int _t=t,i=s;i<=_t;i++)

template<class T>
void check_max( T&a, T b ){
	if ( a <  b ) a = b;
}
template<class T>
void check_min( T&a, T b ){
	if ( a > b ) a = b;
}

//#define debug
const int MAXN = 60*2;
int n;
int v[MAXN][MAXN];

int center( int x, int y ){
//	printf("(%d,%d):\n",x,y);
	for( int i = 0; i <= 2*n-2; i++ )
		for( int j = 0; j <= 2*n-2; j++ )if(v[i][j]!=-1){
			int ii,jj;
			ii = x*2-i, jj = j;//y*2-j;
			if (!( ii < 0 || jj < 0 || ii > 2*n-2 || jj > 2*n-2 )
					&&v[ii][jj] != -1){
				//continue;
			//	printf("(%d,%d)(%d)  <-> (%d,%d):%d\n",i,j,v[i][j],ii,jj,v[ii][jj]);
				if ( v[i][j] != v[ii][jj] )
					return 100000;
			}
			ii = i, jj = y*2-j;
			if (!( ii < 0 || jj < 0 || ii > 2*n-2 || jj > 2*n-2 )
					&&v[ii][jj] != -1){
				//continue;
				//printf("(%d,%d)(%d)  <-> (%d,%d):%d\n",i,j,v[i][j],ii,jj,v[ii][jj]);
				if ( v[i][j] != v[ii][jj] )
					return 100000;
			}
	}
	int d = max( abs( (x-y) - ( (n-1)-(n-1) ) ) , abs( (x+y) - (n-1+n-1)) );
	int nn;
	if ( n % 2 == 0 ){
		if( d % 2 == 0 )
			nn = (n/2 + d/2 )*2;
		else
			nn = (n/2 + d/2)*2+1;
	}else
		if ( d % 2 == 0 )
			nn = (n/2 + d/2)*2+1;
		else
			nn = (n/2 + d/2)*2+2;
//	printf("(%d,%d):\n",x,y);
//	printf("n=%d  d=%d  nn=%d\n",n,d,nn);
	return nn*nn-n*n;
}
int main(){
	int T;cin>>T;
	REP(Case,1,T+1){
		cin >> n;
		memset(v,0xff,sizeof(v));
		for( int i = 0; i <=2*n-2;i++ ){
			int cj = 0,start = 0;
			if ( i <= n-1 ) cj = i+1; else cj = n-(i-(n-1));
			if ( i <= n-1 ) start = (n-1)-i;else start=i-(n-1);
			for( int j = 0; j < cj; j++ ){
				cin >> v[i][start];
				start += 2;
			}
		}
/*
		for( int i = 0; i <= 2*n-2; i++ ){
			for( int j = 0; j <= 2*n-2; j++ )
				printf("%4d",v[i][j]);
			printf("\n");
		}
		puts("~~~~~~~~`");
		continue;
*/
		int ans = 100000;
		for( int i = 0; i <= 2*n-2; i++ ){
			for( int j = 0; j <= 2*n-2; j++ ){
				int tans = center(i,j);
				if ( tans < ans ){
					ans = tans;
	//				printf("(%d,%d) : %d\n",i,j,tans);
				}
			}
		}
		printf("Case #%d: %d\n",Case,ans);
	//	puts("~~~~~~~");
	}
	return 0;
}
