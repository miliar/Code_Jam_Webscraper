// File Name   : a.cpp
// Development : Saturday 13 April 2013 06:38:18 PM IST
// Author      : Xeronix

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <bitset>
#include <sstream>
#include <stack>
#include <queue>
#include <numeric>
#include <utility>
#include <cctype>
#include <list>
#include <valarray>
#include <sstream>
#include <complex>
#include <deque>
#include <new>
#include <map>
#include <set>

#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <signal.h>
#include <time.h>
#include <float.h>

#define TR(c,i) for ( typeof((c).begin()) i = (c).begin(); i != (c).end(); i++ ) 
#define SWAP(a,b) {typeof(a) T; T=a; a=b; b=T;}
#define FOR(i,a,b) for( i = a; i <= b; i++ )
#define ROF(i,a,b) for( i = a; i >= b; i-- )
#define MEM(t,n) ( t * )malloc( (n)*sizeof( t ) )
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define ALL(v) (v).begin(), (v).end()
#define SORT(v) sort( ALL(v) )
#define SET(x,a) memset(x,a,sizeof(x))
#define IN(x,a) (x.find(a) != x.end()) 

#define DIST(x1,y1,x2,y2) SQ(x1-x2)+SQ(y1-y2)
#define DISTS(p,q) SQ(p.x-q.x)+SQ(p.y-q.y)
#define SQ(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define F first
#define S second

#define DEB(x) cout << #x << " = " << x << endl;
#define DEBA(x,n) { int i; cout << "{\n"; FOR(i,0,n-1)cout << i << " " << x[i] << endl; cout << "}\n"; }
#define DEBT(x) { cout << "{\n"; TR( x,it ) cout << *it << "\n" ; cout << "}\n"; }
#define DEBM(x) { cout << "{\n"; TR( x,it ) cout << it->F << " : " << it->S << "\n"; cout << "}\n"; }

#define SYNC ios_base::sync_with_stdio(false);
#define C(format,n) scanf( "%"#format, &n )
#define P(format,n) printf( "%"#format, n )

//#define LIM
#ifdef LIM
	int S, D, Y, O;
	char *inp, *out, *ipos, *opos, DIG[30];
	#define FRMI inp=( char * )malloc( LIM*sizeof( char ) );fread_unlocked( inp,1,LIM,stdin );ipos=inp;
	#define FWM out=( char * )malloc( LIM*sizeof( char ) );opos=out;
	#define FWO fwrite_unlocked( out,opos-out,1,stdout );
	#define GETI(n) n=0;while(*ipos<33){ipos++;}if(*ipos=='-'){S=-1;ipos++;}else{S=1;}while(*ipos>='0'){n=10*n+(*ipos-'0');ipos++;}n*=S;
	#define PUTI(n) O=n;D=0;if(O<0){*opos++='-';O*=-1;}if(!O)*opos++='0';else{while(O){Y=O/10;DIG[D++]=O-Y*10+'0';O=Y;}\
	while(D--)*opos++=DIG[D];}
	#define PUTC(c) *opos++=c;
#endif

using namespace std;

template<class T> inline string tostring( T n ){ stringstream ss; ss << n; ss.flush(); return ss.str(); }
template<class T> inline string tobinary( T n ){ string s = n ? "" : "0"; while( n ) { s += ( ( n & 1 ) + '0' ); n >>= 1; } return s; }
template<class T> inline int digits( T n ){ int cnt = n ? 0 : 1; while( n ){ n /= 10; cnt++; } return cnt; }
template<class T1, class T2> inline T2 gcd( T1 a, T2 b ){ return !b ? a : gcd( b, a%b ); }
template<class T> inline T abs( T a ){ return a < 0 ? -a : a; }

string solve() {
	string s[4];
	int i, j;

	FOR( i,0,3 ) {
		cin >> s[i];
	}

	int cor, cxr, ctr;
	int coc, cxc, ctc;
	int cod, cxd, ctd;
	int codr, cxdr, ctdr;
	int dc = 0;

	cod = cxd = ctd = 0;
	codr = cxdr = ctdr = 0;
	
	FOR( i,0,3 ) {
		cod += s[i][i] == 'O';
		cxd += s[i][i] == 'X';
		ctd += s[i][i] == 'T';
		
		codr += s[i][3-i] == 'O';
		cxdr += s[i][3-i] == 'X';
		ctdr += s[i][3-i] == 'T';
		
		cor = cxr = ctr = 0;
		coc = cxc = ctc = 0;
			
		FOR( j,0,3 ) {
			dc += s[i][j] == '.';
			cor += s[i][j] == 'O';
			cxr += s[i][j] == 'X';
			ctr += s[i][j] == 'T';
		
			coc += s[j][i] == 'O';
			cxc += s[j][i] == 'X';
			ctc += s[j][i] == 'T';
		}

		if( cor+ctr == 4 || coc+ctc == 4 ) {
			return "O won";
		} else if( cxr+ctr == 4 || cxc+ctc == 4 ) {
			return "X won";
		}	
	}

	if( cod+ctd == 4 || codr+ctdr == 4 ) {
		return "O won";
	} else if( cxd+ctd == 4 || cxdr+ctdr == 4 ) {
		return "X won";
	}

	return !dc ? "Draw" : "Game has not completed";
}

int main() {
	int t, i;

	for( C(d,t), i = 1; i <= t; i++ ) {
		printf( "Case #%d: %s\n", i, solve().c_str() );
	}

	return 0;
}
