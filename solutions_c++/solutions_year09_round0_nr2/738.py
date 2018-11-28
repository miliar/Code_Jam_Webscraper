#include <queue>
#include <cstdio>

const int TRUE = 1;
const int FALSE = 0;

typedef struct {
	int x;
	int y;
} point;

int valid(point p, int m, int n) {
	int i = p.x;
	int j = p.y;
	if ( i < 0 ) {
		return FALSE;
	}
	if ( i >= m ) {
		return FALSE;
	}
	if ( j < 0 ) {
		return FALSE;
	}
	if ( j >= n ) {
		return FALSE;
	}
	return TRUE;
}

point north(point p) {
	point t = p;
	t.x--;
	return t;
}

point south(point p) {
	point t = p;
	t.x++;
	return t;
}

point east(point p) {
	point t = p;
	t.y++;
	return t;
}

point west(point p) {
	point t = p;
	t.y--;
	return t;
}

#define ALT(p) (alt[(p).x][(p).y])
int flow(int **alt, point p1, point p2, int m, int n) {
	point minp = p1;
	int h = ALT(p1);

	if ( valid(north(p1), m, n) && ALT(north(p1)) < h ) {
		minp = north(p1);
		h = ALT(north(p1));
	}

	if ( valid(west(p1), m, n) && ALT(west(p1)) < h ) {
		minp = west(p1);
		h = ALT(west(p1));
	}

	if ( valid(east(p1), m, n) && ALT(east(p1)) < h ) {
		minp = east(p1);
		h = ALT(east(p1));
	}

	if ( valid(south(p1), m, n) && ALT(south(p1)) < h ) {
		minp = south(p1);
		h = ALT(south(p1));
	}
	
	if ( minp.x == p2.x && minp.y == p2.y ) {
		return TRUE;
	}
	else {
		return FALSE;
	}
}

int connected(point p1, point p2, int **alt, int m, int n) {
	if ( !valid(p2, m, n) ) {
		return FALSE;
	}
	if ( flow(alt, p1, p2, m, n) ) {
		return TRUE;
	}
	if ( flow(alt, p2, p1, m, n) ) {
		return TRUE;
	}
	return FALSE;
}

#define WORLD(p) (world[(p).x][(p).y])
void bfs(int **alt, char **world, int m, int n, point p0, char code) {
	std::queue<point> q;
	
	q.push(p0);

	while ( !q.empty() ) {
		point p = q.front();
		
		q.pop();

		WORLD(p) = code;

		if ( connected(p, north(p), alt, m, n) ) {
			if ( !WORLD(north(p)) ) {
				q.push(north(p));
			}
			else {
				assert( WORLD(north(p)) == code );
			}
		}
		if ( connected(p, south(p), alt, m, n) ) {
			if ( !WORLD(south(p)) ) {
				q.push(south(p));
			}
			else {
				assert( WORLD(south(p)) == code );
			}
		}
		if ( connected(p, east(p), alt, m, n) ) {
			if ( !WORLD(east(p)) ) {
				q.push(east(p));
			}
			else {
				assert( WORLD(east(p)) == code );
			}
		}
		if ( connected(p, west(p), alt, m, n) ) {
			if ( !WORLD(west(p)) ) {
				q.push(west(p));
			}
			else {
				assert( WORLD(west(p)) == code );
			}
		}
	}
}

int main(void) {
	int T;
	scanf("%d", &T);

	for ( int test = 1; test <= T; test++ ) {

		int m;
		int n;

		scanf("%d %d", &m, &n);

		int *alt_buf = (int *) malloc(sizeof(int) * m * n);
		int **alt = (int **) malloc(sizeof(int *) * m);
		for ( int i = 0; i < m; i++ ) {
			alt[i] = &alt_buf[n * i];
		}

		for ( int i = 0; i < m; i++ ) {
			for ( int j = 0; j < n; j++ ) {
				scanf("%d", &alt[i][j]);
			}
		}
	

		char *world_buf = (char *) calloc(m * n, sizeof(char));
		char **world = (char **) malloc(sizeof(char *) * m);
		for ( int i = 0; i < m; i++ ) {
			world[i] = &world_buf[n * i];
		}

		char code = 'a';
		for ( int i = 0; i < m; i++ ) {
			for ( int j = 0; j < n; j++ ) {
				if ( !world[i][j] ) {
					point p;
					p.x = i;
					p.y = j;
					bfs(alt, world, m, n, p, code++);
				}
			}
		}


		printf("Case #%d:\n", test);
		for ( int i = 0; i < m; i++ ) {
			for ( int j = 0; j < n; j++ ) {
				printf("%c", world[i][j]);
				if ( j != (n - 1) ) {
					printf(" ");
				}
			}
			printf("\n");
		}
	}

	return 0;
}
