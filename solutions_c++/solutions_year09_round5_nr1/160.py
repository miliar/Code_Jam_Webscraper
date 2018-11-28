#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<string>
#define P 7529536
using namespace std;

FILE *fin, *fout;

int r, c;
int n;

char Initial[ 15][ 15];
int Target[ 5][ 2];
int Start[ 5][ 2];
int Queue[ P][ 5][ 2];
int Cnt[ P];

int dy[ 4] = { 0, 0, -1, 1}, dx[ 4] = { -1, 1, 0, 0};

bool is_stable( int A[ 5][ 2]) {

	if ( n == 1)
		return 1;

	for ( int i = 0; i < 4; i++) {
		if ( A[ 0][ 0] + dy[ i] == A[ 1][ 0]
		&& A[ 0][ 1] + dx[ i] == A[ 1][ 1])
			return 1;
	}
	return 0;
}

int prs( void) {
	/* input */

	fscanf( fin, "%d %d", &r, &c);
	n = 0;
	int m = 0;

	for ( int i = 0; i < r; i++) {
		fscanf ( fin, "%s", Initial[ i]);
		for ( int j = 0; j < c; j++) {
			if ( Initial[ i][ j] == 'o' || Initial[ i][ j] == 'w') {
				Start[ n][ 0] = i;
				Start[ n][ 1] = j;
				n++;
			}
			if ( Initial[ i][ j] == 'w' || Initial[ i][ j] == 'x') {
				Target[ m][ 0] = i;
				Target[ m][ 1] = j;
				m++;
			}
		}
	}
	
	for ( int i = 0; i < P; i++)
		Cnt[ i] = -1;
	int p = 1, state = 0;
	for ( int i = 0; i < n; i++) {
		Queue[ 0][ i][ 0] = Start[ i][ 0];
		Queue[ 0][ i][ 1] = Start[ i][ 1];
		state += Start[ i][ 0] * p;
		p *= 12;
		state += Start[ i][ 1] * p;
		p *= 12;
	}
	Cnt[ state] = 0;

	int head, tail, ret = -1;
	head = -1;
	tail = 0;

	while ( head < tail) {
		head++;
		int State[ 5][ 2], New_State[ 5][ 2];
		int init_state = 0;
		
		p = 1;

		for ( int i = 0; i < n; i++) {
			State[ i][ 0] = Queue[ head][ i][ 0];
			State[ i][ 1] = Queue[ head][ i][ 1];
			init_state += State[ i][ 0] * p;
			p *= 12;
			init_state += State[ i][ 1] * p;
			p *= 12;
		}
		bool is_init_stable = is_stable( State );

		if ( State[ 0][ 0] == 1 && State[ 0][ 1] == 2
			&& State[ 1][ 0] == 2 && State[ 1][ 1] == 1) {
				p = p;
		}

		int is_end = 0;
		for ( int i = 0; i < n; i++) {
			for ( int j = 0; j < n; j++) {
				if ( State[ i][ 0] == Target[ j][ 0] &&
					State[ i][ 1] == Target[ j][ 1])
					is_end++;
			}
		}

		if ( is_end == n) {
			ret = Cnt[ init_state];
			break;
		}

		for ( int i = 0; i < n; i++) { // Move 1
			int x = State[ i][ 1], y = State[ i][ 0];
			for ( int j = 0; j < n; j++) {
				New_State[ j][ 0] = State[ j][ 0];
				New_State[ j][ 1] = State[ j][ 1];
			}

			for ( int j = 0; j < 4; j++) {				
				int wy = y + dy[ j], wx = x + dx[ j];
				bool is_ok = 1;
				if ( !( 0 <= wy && 0 <= wx && wy < r && wx < c)) continue;
				if ( Initial[ wy][ wx] == '#') continue;
				for ( int k = 0; k < n; k++) {
					if ( wy == State[ k][ 0] && wx == State[ k][ 1])
						is_ok = 0;
				}
				if ( !is_ok) continue;

				wy = y - dy[ j], wx = x - dx[ j];
				if ( !( 0 <= wy && 0 <= wx && wy < r && wx < c)) continue;
				if ( Initial[ wy][ wx] == '#') continue;
				for ( int k = 0; k < n; k++) {
					if ( wy == State[ k][ 0] && wx == State[ k][ 1])
						is_ok = 0;
				}
				if ( !is_ok) continue;


				New_State[ i][ 0] = wy;
				New_State[ i][ 1] = wx;
				bool is_new_stable = is_stable( New_State );
				if ( !is_new_stable && ! is_init_stable) continue;

				p = 1;
				state = 0;
				for ( int k = 0; k < n; k++) {
					state += New_State[ k][ 0] * p;
					p *= 12;
					state += New_State[ k][ 1] * p;
					p *= 12;
				}

				if ( Cnt[ state] == -1) {
					tail++;
					for ( int k = 0; k < n; k++) {
						Queue[ tail][ k][ 0] = New_State[ k][ 0];
						Queue[ tail][ k][ 1] = New_State[ k][ 1];
					}
					Cnt[ state] = Cnt[ init_state] + 1;
				}
			}
		}
	}

	return ret;
}

int main( void) {
	fin = fopen( "input.txt", "rt");
	fout = fopen( "output.txt", "wt");
	
	int testcase;
	fscanf( fin, "%d", &testcase);


	/* process */
	for ( int i = 1; i <= testcase; i++)
		fprintf( fout, "Case #%d: %d\n", i, prs());


	fclose( fin);
	fclose( fout);

	return 0;
}