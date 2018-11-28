#include <iostream>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdarg>
#include <cassert>
#include <vector>
#include <queue>
#include <deque>
#include <algorithm>
#include <set>
#include <list>
#include <algorithm>
#include <utility>
#include <unistd.h>
#include <cstdlib>
#include <map>
#include <sstream>
using namespace std;

#define REP(i,N) for(int i = 0;i < (N); ++i )
#define REPV(i,ar) for(int i = 0;i < (ar).sz; ++i )
#define EACH(it,mp) for( __typeof(mp.begin()) it(mp.begin()); it != mp.end(); ++it )
#define FOR(i,a,b) for(int i = (a); i <= (b); ++i )
#define sz size()
#define pb push_back
#define mkp make_pair
#define INF (int(1e9))
#define GI ({int t;scanf("%d",&t);t;})
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef long long int LL;

char Map[128][128];
int A[128][128], Seen[128][128];
int N,M;

#define ok(a,b) ( (a) >= 0 && (b) >= 0 && (a) < N && (b) < M )

int dx[] = { -1, 0 , 0 , 1 };
int dy[] = { 0 , -1 , 1 , 0 };


bool is_basin( int x , int y ) {
	REP(d,4) {
		int a = x+dx[d], b = y+dy[d];
		if( !ok(a,b) ) continue;
		if( A[a][b] < A[x][y] ) return false;
	}
	return true;
}

bool flows( int a1 , int b1 , int a2 , int b2 ) {
	int smallest = INT_MAX, dir = -1;
	REP(d,4) {
		int x = a1 + dx[d], y = b1 + dy[d];
		if( !ok(x,y) ) continue;
		if( A[x][y] < smallest && A[x][y] < A[a1][b1] ) smallest = A[x][y], dir = d;	
	}
	if( dir == -1 || !( a2 == a1+dx[dir] && b2 == b1+dy[dir] ) ) return false;
	return true;
}


void fill( int i , int j , char c ) {
	if( Seen[i][j] ) {
		assert( Map[i][j] = c );
		return;
	}
	Seen[i][j] = 1,Map[i][j] = c;
	
	REP(d,4) {
		int x = i+dx[d], y = j+dy[d];
		if( !ok(x,y) ) continue;
		if( flows( x , y , i , j ) ) fill( x , y , c );
	}
}


int main(){
	int T = GI;
	freopen("temp.cpp.out" , "w", stdout );
	REP(tt,T){
		memset( Seen, 0 , sizeof( Seen ) );
		N = GI, M = GI;	
		REP(i,N) REP(j,M) A[i][j] = GI;
		char c = 'a';
		REP(i,N) REP(j,M) if( is_basin(i,j) ) fill(i,j,c++);
		printf("Case #%d:\n", tt+1 );
		
		c = 'a';
		map<char,char> mp;
		REP(i,N) REP(j,M) {
			if( mp.count( Map[i][j] ) ) Map[i][j] = mp[ Map[i][j] ];
			else mp[ Map[i][j] ] = c++ , Map[i][j] = mp[ Map[i][j] ];		
		}		
		REP(i,N) {
			REP(j,M) printf("%c ", Map[i][j]);
			puts("");
		}
	}
	return 0;
}

