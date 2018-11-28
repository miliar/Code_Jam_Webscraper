#include <bits/stdc++.h>
using namespace std;

#define fr(a,b,c) for( int a = b ; a < c ; ++a )
#define db(x) cerr << #x " == " << x << endl
#define _ << ", " <<

typedef long long ll;

char mapa[10][10];
int dir[4][2] = {{0,1},{1,1},{1,0},{-1,1}};

int doit(int x,int y, int d) {
	char tmp[4];
	int k = 0;
	while( x < 4 && y < 4 && x >= 0 && y >= 0 ) {
		tmp[k++] = mapa[x][y];
		x += dir[d][0];
		y += dir[d][1];
	}
	if( k < 4 ) return 0;
	fr(i,0,k) if( tmp[i] != 'X' && tmp[i] != 'T' ) goto outro;
	return 1;
	outro:;
	fr(i,0,k) if( tmp[i] != 'O' && tmp[i] != 'T' ) return 0;
	return 2;
}

int main() {
	int t, caso = 1;
	scanf("%d", &t);
	while( t-- ) {
		fr(i,0,4) scanf("%s", mapa[i]);
		printf("Case #%d: ", caso++);
		
		fr(k,0,4) fr(i,0,4) fr(j,0,4) {
			int x = doit(i,j,k);
			if( x == 1 ) {
				puts("X won");
				goto fim;
			} else if( x== 2 ) {
				puts("O won");
				goto fim;
			}
		}
		fr(i,0,4) fr(j,0,4) if( mapa[i][j] == '.') {
			puts("Game has not completed");
			goto fim;
		}
		puts("Draw");
		fim:;
	}
	return 0;
}
