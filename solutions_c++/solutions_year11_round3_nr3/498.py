#include<stdio.h>
#include<stdlib.h>
#include<string.h>

char map[200][200];
int S[200];


int main() {
	int i, j;
	int N, M;
	int L, H;
	int T;
	scanf("%d", &T);
	for ( int t = 1 ; t <= T ; t++ ) {
		scanf("%d %d %d", &N, &L, &H);
		for ( i = 0 ; i < N ; i++ ) {
			scanf("%d", &S[i]);
		}
		int key = 0;
		for ( i = L ; i <= H ; i++ ) {
			for ( j = 0 ; j < N ; j++ ) {
				if ( S[j] > i && S[j]%i == 0 ) {
					continue;
				}
				else if ( S[j] <= i && i%S[j] == 0 ) {
					continue;
				}
				else {
					break;
				}
			}
			if ( j == N ) {
				key = 1;
				break;
			}
		}
		
		if ( key ) {
			printf("Case #%d: %d\n", t, i);
		}
		else {
			printf("Case #%d: NO\n", t);
		}
			
	}
	
	return 0;
}