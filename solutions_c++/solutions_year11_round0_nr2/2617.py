#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
using namespace std;

char cmb[30][30];
bool ops[30][30];
int tot;
char list[100];

void init() {
	memset( cmb, '\0', sizeof(cmb) );
	memset( ops, false, sizeof(ops) );
	tot = 0;	
	
	int c;
	scanf( "%d ", &c );
	for ( int i=1; i<=c; i++ ) {
		char c1,c2,c3;
		scanf( "%c%c%c ", &c1, &c2, &c3 );
		cmb[c1-'A'][c2-'A'] = c3;
		cmb[c2-'A'][c1-'A'] = c3;
	}
	
	int d;
	scanf( "%d ", &d );
	for ( int i=1; i<=d; i++ ) {
		char c1,c2;
		scanf( "%c%c ", &c1, &c2 );
		ops[c1-'A'][c2-'A'] = true;
		ops[c2-'A'][c1-'A'] = true;
	}
}

void work() {
	int n;
	scanf( "%d ", &n );
	
	for ( int i=1; i<=n; i++ ) {
		tot++;
		scanf( "%c", &list[tot] );
		
		while ( tot>1 && cmb[list[tot]-'A'][list[tot-1]-'A']!='\0' ) {
			char c = cmb[list[tot]-'A'][list[tot-1]-'A'];
			tot--;
			list[tot] = c;
		}
		
		for ( int j=1; j<tot; j++ )
		if ( ops[list[j]-'A'][list[tot]-'A'] ) tot = 0;
	}
}

void print( int t ) {
	printf( "Case #%d: [", t );
	for ( int i=1; i<=tot; i++ ) {
		printf( "%c", list[i] );
		if ( i!=tot ) printf( ", " );
	}
	printf( "]\n" );
}

int main() {
	freopen( "b.in", "r", stdin );
	freopen( "b.out", "w", stdout );
	
	int T;
	scanf( "%d", &T );
	
	for ( int i=1; i<=T; i++ ) {
		init();
		work();
		print( i );
	}
	
	return 0;
}
