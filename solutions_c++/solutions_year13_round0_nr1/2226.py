/*
 * By Duck
 */

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>

char mp[4][5];

int win(char c) {
	int tx=-1, ty=-1, res = 0;
	for( int i=0; i<4; i++ ) for( int j=0; j<4; j++ ) if( mp[i][j]=='T' ) ty=i, tx=j;
	mp[ty][tx] = c;
	for( int i=0; i<4; i++ ) {
		if ( mp[i][0]==c&&mp[i][1]==c&&mp[i][2]==c&&mp[i][3]==c 
		  || mp[0][i]==c&&mp[1][i]==c&&mp[2][i]==c&&mp[3][i]==c )
		  	res = 1;
	}
	if ( mp[0][0]==c&&mp[1][1]==c&&mp[2][2]==c&&mp[3][3]==c 
	 ||  mp[3][0]==c&&mp[2][1]==c&&mp[1][2]==c&&mp[0][3]==c )
	 	res = 1;
	if( tx!=-1 ) mp[ty][tx] = 'T';
	return res;
}
int gameend() {
	for( int i=0; i<4; i++ ) for( int j=0; j<4; j++ ) if( mp[i][j]=='.' ) return 0;
	return 1;
}

int main(){
	int t;
	scanf("%d", &t);
	for( int r=1; r<=t; r++ ) {
		for( int i=0; i<4; i++ ) 
			scanf("%s", mp[i]);
		printf("Case #%d: ",r);
		if( win('X') )
			printf("X won");
		else if( win('O') )
			printf("O won");
		else if( gameend() )
			printf("Draw");
		else
			printf("Game has not completed");
		puts("");
	}
}

