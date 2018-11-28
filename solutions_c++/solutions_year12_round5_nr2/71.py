#include <iostream>
#include <sstream>

#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cstdio>

#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>

using namespace std;

struct Move {
	int x, y;
	Move ( int xx, int yy ) : x(xx-1), y(yy-1) {}
};

int S, M ;
vector<Move> moves; 

int EDGE = (2*S-1) ;
int MXUSE = EDGE*EDGE+EDGE ;

void input() 
{
	scanf ( "%d%d", &S, &M ) ;
	EDGE = (2*S-1) ;
	MXUSE = EDGE*EDGE+EDGE ;

	moves.clear();
	for ( int i=0;i<M;++i ) {
		int x, y ;
		scanf("%d%d", &x, &y ) ;
		moves.push_back(Move(x,y));
	}
}

#define MAX (3000*3000*2*2) 

#define EDGE1 1
#define EDGE2 2
#define EDGE3 4
#define EDGE4 8
#define EDGE5 16
#define EDGE6 32

#define CORNOR1 64
#define CORNOR2 128
#define CORNOR3 256
#define CORNOR4 512
#define CORNOR5 1024
#define CORNOR6 2048

#define PIECE 4096

struct state
{
	int parent ;
	int s ;
	int vid ;
};

int nBits[64];
int moveid ;
int nxid ;
state UF[MAX] ;

int dx[] = {1,1,0,0,-1,-1}, dy[] = {1,0,1,-1,-1,0} ;

int Find ( int a ) {
	if ( UF[a].parent < 0 ) return a ;
	else return UF[a].parent = Find(UF[a].parent);
}

bool Union ( int a, int b ) {
	int rt1 = Find(a), rt2 = Find(b) ;
	if ( rt1 != rt2 ) {
		int st = UF[rt1].s | UF[rt2].s ;
		UF[rt1].parent = rt2;
		UF[rt2].s = st ;
		return true;
	}
	return false;
}

int midx ( int x, int y ) { return (EDGE*x)+y ; }

int bitCount ( int bits ) {
	return nBits[bits&63];
}

int mvidx[10001];
int mvsz = 0;

int stid ;
int bound = 0 ;
int tryid ;
int visitcnt;

bool dfs ( int x, int y ) 
{
	if ( x >= 0 && y >= 0 && x < EDGE && y < EDGE ) {
		// printf ( "try %d %d\n", x, y ) ;
		int id = midx(x,y);
		if ( UF[id].s & PIECE ) return true;
		if ( UF[id].vid == tryid ) return true; // visited this times
		if ( UF[id].vid > stid ) return false; // visit bad node
		
		UF[id].vid = tryid ;
		++ visitcnt ;
		if ( visitcnt > bound ) return false;
		
		for ( int d=0;d<6;++d ) {
			int xx = x+dx[d], yy = y+dy[d] ;
			if ( !dfs ( xx, yy ) ) return false;
		}
	} else {
		return false; // touch outside
	}
	return true;
}



bool ringTest ( int g ) {
	mvsz = 0;
	for ( int i=0;i<moveid;++i ) {
		int id = midx(moves[i].x, moves[i].y);
		if ( Find(id) == g ) mvidx[mvsz++] = i;
	}
	stid = nxid ;
	bound = mvsz - 5 ;

	// printf ( "Move %d\n", moveid ) ;
	
	for ( int i=0;i<mvsz;++i ) {
		int x = moves[mvidx[i]].x, y = moves[mvidx[i]].y;
		for ( int d=0;d<6;++d ) {
			int xx = x+dx[d], yy = y+dy[d] ;
			if ( xx >= 0 && yy >= 0 && xx < EDGE && yy < EDGE ) {
				int id = midx(xx,yy) ;
				if ( Find(id) != g && UF[id].vid < stid ) {
					tryid = nxid ++ ;
					visitcnt = 0 ;
					if ( dfs(xx,yy) ) return true;
				}
			}
		}
	}
	return false;
}

bool test ( int mv ) {

	int st = UF[Find(mv)].s ;
	
	bool isFork = (bitCount(st&63)>=3), isBridge = (bitCount((st>>6)&63)>=2);
	bool isRing = ringTest(Find(mv)) ;
	
	if ( isRing && isBridge && isFork ) { printf( "bridge-fork-ring in move " ); return true; }
	if ( isRing && isBridge ) { printf( "bridge-ring in move " ); return true; }
	if ( isRing && isFork ) { printf( "fork-ring in move " ); return true; }
	if ( isBridge && isFork ) { printf( "bridge-fork in move " ); return true; }
	if ( isRing ) { printf( "ring in move " ); return true; }
	if ( isBridge ) { printf( "bridge in move " ); return true; }
	if ( isFork ) { printf( "fork in move " ); return true; }
	
	return false;
}

bool insertMove ( int x, int y ) {
	bool update = false ;
	UF[midx(x,y)].s |= PIECE ;
	for ( int d=0;d<6;++d ) {
		int xx = x+dx[d], yy = y+dy[d] ;
		if ( xx >= 0 && yy >= 0 && xx < EDGE && yy < EDGE ) {
			if ( !(UF[midx(xx,yy)].s & PIECE) ) continue ;
			int g1 = Find(midx(x,y)), g2 = Find(midx(xx,yy)) ;
			update |= Union(g1, g2);
		}
	}
	if ( update ) {
		return test ( Find(midx(x,y)) ) ;
	}
	return false;
}

void solv() 
{
	nxid = 1 ;
	for ( int i=0;i<MXUSE;++i ) UF[i].parent = -1, UF[i].s = 0, UF[i].vid = 0 ;

	UF[midx(0,0)].s = CORNOR1;
	UF[midx(0,S-1)].s = CORNOR2;
	UF[midx(S-1,0)].s = CORNOR3;
	UF[midx(EDGE-1,S-1)].s = CORNOR4;
	UF[midx(S-1,EDGE-1)].s = CORNOR5;
	UF[midx(EDGE-1,EDGE-1)].s = CORNOR6;
	
	for ( int i=1;i<=S-2;++i ) {
		UF[midx(0, 0+i)].s = EDGE1 ;
		UF[midx(0+i, 0)].s = EDGE6 ;
		UF[midx(0+i, S-1+i)].s = EDGE2 ;
		UF[midx(S-1+i, 0+i)].s = EDGE5 ;
		UF[midx(S-1+i, EDGE-1)].s = EDGE3 ;
		UF[midx(EDGE-1, S-1+i)].s = EDGE4 ;
	}
/*
	for ( int i=0;i<MXUSE;++i ) {
		if ( UF[i].s & EDGE1 ) printf("(%d, %d) EDGE1\n", i/EDGE+1, i%EDGE+1 ) ;
		if ( UF[i].s & EDGE2 ) printf("(%d, %d) EDGE2\n", i/EDGE+1, i%EDGE+1 ) ;
		if ( UF[i].s & EDGE3 ) printf("(%d, %d) EDGE3\n", i/EDGE+1, i%EDGE+1 ) ;
		if ( UF[i].s & EDGE4 ) printf("(%d, %d) EDGE4\n", i/EDGE+1, i%EDGE+1 ) ;
		if ( UF[i].s & EDGE5 ) printf("(%d, %d) EDGE5\n", i/EDGE+1, i%EDGE+1 ) ;
		if ( UF[i].s & EDGE6 ) printf("(%d, %d) EDGE6\n", i/EDGE+1, i%EDGE+1 ) ;
		if ( UF[i].s & CORNOR1 ) printf("(%d, %d) CORNOR1\n", i/EDGE+1, i%EDGE+1 ) ;
		if ( UF[i].s & CORNOR2 ) printf("(%d, %d) CORNOR2\n", i/EDGE+1, i%EDGE+1 ) ;
		if ( UF[i].s & CORNOR3 ) printf("(%d, %d) CORNOR3\n", i/EDGE+1, i%EDGE+1 ) ;
		if ( UF[i].s & CORNOR4 ) printf("(%d, %d) CORNOR4\n", i/EDGE+1, i%EDGE+1 ) ;
		if ( UF[i].s & CORNOR5 ) printf("(%d, %d) CORNOR5\n", i/EDGE+1, i%EDGE+1 ) ;
		if ( UF[i].s & CORNOR6 ) printf("(%d, %d) CORNOR6\n", i/EDGE+1, i%EDGE+1 ) ;
	}
//*/
	for ( int i=0;i<moves.size();++i ) {
		moveid = i+1 ;
		if ( insertMove(moves[i].x, moves[i].y) ) {
			printf("%d\n", i+1 );
			return ;
		}
	}
	printf("none\n");
}

void bitTable() {
	for ( int i=0;i<64;++i ) {
		int cnt = 0;
		for ( int b=1;b<64;b<<=1 ) {
			if ( i&b ) ++cnt ;
		}
		nBits[i] = cnt ;
	}
}

int main()
{
	bitTable();
	int nCase=1, T;
	
	cin >> T;
	while ( T-- ) {
		input();
		printf ( "Case #%d: ", nCase++ ) ;
		solv() ;
	}
	
	return 0;
}
