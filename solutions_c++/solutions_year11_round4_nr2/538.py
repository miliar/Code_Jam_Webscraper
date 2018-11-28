#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <climits>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>

#define FOR(i,N) for(int i=0;i<(N);i++)
#define REP(i,a,b) for(int i=(a);i<=(b);i++)
#define MP make_pair
#define SIZE(X) ((int)(X.size()))

using namespace std;

typedef long long LL;
typedef unsigned long long LLU;

template<class T> void checkmin(T& a,T b){if(a>b)a=b;}
template<class T> void checkmax(T& a,T b){if(a<b)a=b;}
template<class T> T gcd(T a,T b){return b?gcd(b,a%b):a;}

const double eps=(1e-8);
const int MAXN = 500+10 ;

int dcmp( double x ){
	return x < -eps ? -1 : x > eps ? 1 : 0; 
}



string maze[ MAXN ] ;
int R , C, D;

LL sum[ MAXN ][ MAXN ] ;
LL sumx[ MAXN ][ MAXN ] ; 
LL sumy[ MAXN ][ MAXN ] ; 
/*
1
3 3 7
123
234
345
*/
void init(){
	memset(sumx , 0 , sizeof(sumx) );
	memset(sumy , 0 , sizeof(sumy) ) ;
	memset(sum , 0 , sizeof(sum) ) ;
	FOR( i , R )FOR( j ,C ){
		LL d =  ( maze[i][j] - '0' + D ) ;
		sum[i+1][j+1] = sum[i][j+1] + sum[i+1][j] + d - sum[i][j];
		sumx[i+1][j+1] = sumx[i][j+1] + sumx[i+1][j] + d*( 2*i + 1 ) - sumx[i][j];
		sumy[i+1][j+1] = sumy[i][j+1] + sumy[i+1][j] + d*( 2*j + 1 ) - sumy[i][j];
	}
}

LL S( LL s[][MAXN], int x1,int y1,int x2,int y2){
	return s[x2+1][y2+1] - s[x2+1][y1] - s[x1][y2+1] + s[x1][y1] ;
}
LL Gao( LL s[][MAXN] , int x , int y , int k ){
	return S(s,x,y,x+k-1,y+k-1) - S(s,x,y,x,y)-S(s,x+k-1,y,x+k-1,y)-S(s,x,y+k-1,x,y+k-1)-S(s,x+k-1,y+k-1,x+k-1,y+k-1);
}
int ok( int k ){
	FOR( i , R-k+1 )FOR( j , C-k+1 ){
		int x = i , y = j ;
		
		LL sx = Gao( sumx , x , y , k ) ;
		LL sy = Gao( sumy , x , y , k ) ;
		LL sm = Gao( sum  , x , y , k ) ;
		//cout << sx << " " << sy << " " << sm << endl;
		/*
		FOR( dx , k )FOR( dy , k ){
			if( dx + dy == 0  ) continue;
			if( dx == 0 && dy == k-1 ) continue;
			if( dx == k-1 && dy == 0 ) continue;
			if( dx == k-1 && dy == k-1 )continue;
			int d = D + maze[x+dx][y+dy] - '0';
			sumx += d * (2*x+2*dx+1) ;
			sumy += d * (2*y+2*dy+1) ;
			sum  += d;
		}*/
		//cout << 1.0*sx / sm / 2 << " " << 1.0*sy/sm/2 << endl;
		if( sx == sm * (2*x + k  ) && sy == sm*(  2*y + k ) ) return 1;
	}	
	return 0 ;
}

//#define __FILE_IO__
int main(){

	#ifdef __FILE_IO__
		freopen("B-small-attempt.in","r",stdin);
		freopen("out.out","w",stdout);
	#endif

	int testcase ;
	cin >> testcase ;
	FOR( tc ,testcase ){
		cout << "Case #" << tc + 1 << ": ";
		cin >> R >> C >> D ;
		FOR( i, R ) cin >> maze[i] ;
		FOR( i , R/2 ) swap( maze[i] , maze[R-i-1]);
		init();
		//int x1,y1,x2,y2;
		//while( cin >> x1 >> y1 >> x2 >> y2 ) cout << S(sum,x1,y1,x2,y2) << endl;
		int ret = -1 ;
		for( int size = min(C,R) ; size >= 3 ; size -- )if( ok ( size ) ){ ret = size ; break;}
		if( ret == -1 ){
			puts("IMPOSSIBLE");
		}else{
			printf("%d\n",ret);
		}
	}
}
