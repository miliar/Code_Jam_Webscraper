#include <queue>
#include <stdio.h>

using namespace std;

int main() {

	int t;
	int r, k, n;
	int g;
	int c, turn;
	scanf( "%d", &t);
	for( int i = 0; i < t; i++) {
		scanf( "%d %d %d", &r, &k, &n);

		queue <int> fila;
	
		for( int j = 0; j < n; j++) {
			scanf( "%d", &g);
			fila.push(g);
		}


		c = 0;
		turn = 0;

		for( int j = 0; j < r; j++) {
			int p = 0;
			while( turn + fila.front() <= k && p < n ) {
				turn += fila.front();
				c += fila.front();	
				fila.push(fila.front());
				fila.pop();
				p++;
			}
			turn = 0;
		}
		printf( "Case #%d: %d\n", i + 1 , c);
	}
	return 0;
}
	

