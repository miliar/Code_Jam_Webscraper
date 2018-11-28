#include<stdio.h>
#include<stdlib.h>
#include<string.h>

char map[200][200];

int main() {
	int i, j;
	int N, M;
	int T;
	scanf("%d", &T);
	for ( int t = 1 ; t <= T ; t++ ) {
		scanf("%d %d", &N, &M);
		memset(map,0,sizeof(map));
		for ( i = 0 ; i < N ; i++ ) {
			scanf("%s", map[i]);
		}
		for ( i = 0 ; i+1 < N ; i++ ) {
			for ( j = 0 ; j+1 < M ; j++ ) {
				if ( map[i][j] == '#' && map[i+1][j] == '#' && map[i][j+1] == '#' && map[i+1][j+1] == '#' ) {
					map[i][j] = '/';
					map[i][j+1] = '\\';
					map[i+1][j] = '\\';
					map[i+1][j+1] = '/';
				}
			}
		}
		int key = 1;
		for ( i = 0 ; i < N ; i++ ) {
			for ( j = 0 ; j < M ; j++ ) {
				if ( map[i][j] == '#' ) {
					key = 0;
					break;
				}
			}
			if ( !key )
				break;
		}
		printf("Case #%d:\n", t);
		if ( key ) {
			for ( i = 0 ; i < N ; i++ ) {
				printf("%s\n", map[i]);
			}
		}
		else {
			printf("Impossible\n");
		}
		
		
	}
	
	return 0;
}
	