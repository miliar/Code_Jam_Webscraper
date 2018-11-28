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
const int MAXN = 100;
char ori[MAXN][MAXN];
int n,k;
char rot[MAXN][MAXN];
int low[MAXN];
bool test( char ch ){
	bool res = false;
	// ---
	REP(i,0,n){
		REP(j,0,n-k+1){
			bool ok = true;
			REP(jj,j,j+k) if ( rot[i][jj] != ch ) ok = false;
			res |= ok;
		}
	}
	// |
	// |
	REP(i,0,n){
		REP(j,0,n-k+1){
			bool ok = true;
			REP(jj,j,j+k) if ( rot[jj][i] != ch ) ok = false;
			res |= ok;
		}
	}
	//  /
	REP(i,0,n)REP(j,0,n){
		bool ok = true, enough = false;
		REP(d,0,k){
			int ii = i + d, jj = j + d;
			if ( ii >= n || jj >= n ) break;
			if ( d == k-1 ) enough = true;
			if ( rot[ii][jj] != ch ) ok = false;
		}
		if ( enough ) res |= ok;
	}	
	//  
	REP(i,0,n)REP(j,0,n){
		bool ok = true, enough = false;
		REP(d,0,k){
			int ii = i + d, jj = j - d;
			if ( ii >= n || jj < 0 ) break;
			if ( d == k-1 ) enough = true;
			if ( rot[ii][jj] != ch ) ok = false;
		}
		if ( enough ) res |= ok;
	}
	return res;
}
int main(){
	int t;
	scanf("%d",&t);
	REP(Case,1,t+1){
		scanf("%d%d",&n,&k);
		REP(i,0,n)scanf("%s",ori[i]);
		memset(low,0,sizeof(low));
		memset(rot,'.',sizeof(rot));
		REP(i,0,n){
			for( int j = n-1; j >= 0; j-- ) if ( ori[i][j]!='.'){
				rot[i][ low[i]++ ] = ori[i][j];
			}
		}
/*
		printf("ori:\n");
		REP(i,0,n){
			REP(j,0,n)printf("%c",ori[i][j]);
			printf("\n");
		}
		printf("rot:\n");
		REP(i,0,n){
			REP(j,0,n)printf("%c",rot[i][j]);
			printf("\n");
		}
		printf("~~~~~~~~~~\n");
		continue;
*/

		bool rb,rr;
		rb = test('B');
		rr = test('R');
		printf("Case #%d: ",Case);
		if ( rb )
			if ( rr ) printf("Both");
			else printf("Blue");
		else
			if ( rr ) printf("Red");
			else printf("Neither");
		printf("\n");
	}
	return 0;
}
