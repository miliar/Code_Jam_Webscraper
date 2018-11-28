#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;
const int maxn = 120;
const int mv[8][2]={ 0,1, 1,0, 0,-1, -1,0, 1,1, -1,-1, -1,1, 1,-1 };

char g[maxn][maxn];
int task, n, k, T=0;
bool ret1, ret2;

bool check( int x, int y ){
	for (int dir=0; dir<8; dir++){
		bool ok = true;
		int fx = x+mv[dir][0], fy = y+mv[dir][1];
		for (int i=1; i<=k-1; i++){
			if ( !( 0<=fx && fx<n && 0<=fy && fy<n && g[fx][fy]==g[x][y] ) ){
				ok = false; break;
			}
			fx += mv[dir][0];
			fy += mv[dir][1];
		}
		if ( ok ) return true;
	}
	return false;
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	for (scanf("%d", &task); task--;){
		scanf("%d%d", &n, &k);
		for (int i=0; i<n; i++){
			scanf("%s", g+i);
			int m=n-1;
			for (int j=n-1; j>=0; j--)
			if ( g[i][j]!='.' )
				g[i][m--] = g[i][j];
			for (int j=m; j>=0; j--)
				g[i][j] = '.';
		}
		ret1 = ret2 = false;
		for (int i=0; i<n; i++)
		for (int j=0; j<n; j++)
		if ( g[i][j]!='.' && check( i, j ) ){
			if ( g[i][j]=='R' ) ret1 = true;else ret2 = true;
		}

		if ( !ret1 && !ret2 ) 
			printf("Case #%d: Neither\n", ++T);else
		if ( ret1 && ret2 ) 
			printf("Case #%d: Both\n", ++T);else
		if ( ret1 ) 
			printf("Case #%d: Red\n", ++T);else
			printf("Case #%d: Blue\n", ++T);
	}
	return 0;
}
