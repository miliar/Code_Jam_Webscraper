#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
using namespace std;

int N, K;
char Board[ 51][ 51];
bool red_flag = 0, blue_flag = 0;
char color;
bool flag;

void Check( void) {
	for ( int i = 0; i < N; i++) {
		for ( int j = 0; j < N; j++) {
			color = Board[ i][ j];
			if ( color == '.')
				continue;

			// vertical
			if ( i + K - 1 < N) {
				flag = 1;
				for ( int k = 0; k < K; k++)
					if ( color != Board[ i + k][ j]) flag = 0;
				if ( flag) {
					if ( color == 'R') red_flag = 1;
					else blue_flag = 1;
				}
			}

			// horizontal
			if ( j + K - 1 < N) {
				flag = 1;
				for ( int k = 0; k < K; k++)
					if ( color != Board[ i][ j + k]) flag = 0;
				if ( flag) {
					if ( color == 'R') red_flag = 1;
					else blue_flag = 1;
				}
			}

			// diagonal1
			if ( i + K - 1 < N && j + K - 1 < N) {
				flag = 1;
				for ( int k = 0; k < K; k++)
					if ( color != Board[ i + k][ j + k]) flag = 0;
				if ( flag) {
					if ( color == 'R') red_flag = 1;
					else blue_flag = 1;
				}
			}
			
			// diagonal2
			if ( i + K - 1 < N && j - K + 1 >= 0) {
				flag = 1;
				for ( int k = 0; k < K; k++)
					if ( color != Board[ i + k][ j - k]) flag = 0;
				if ( flag) {
					if ( color == 'R') red_flag = 1;
					else blue_flag = 1;
				}
			}
		}
	}
}

void Flip( void) {
	for ( int i = 0; i < N; i++) {
		for ( int j = N - 1 ; j >= 0; j--) {
			if ( Board[ i][ j] == '.') {
				for ( int k = j - 1; k >= 0; k--) {
					if ( Board[ i][ k]  != '.') {
						swap( Board[ i][ j], Board[ i][ k]);
						break;
					}
				}
			}
		}
	}
}

int main( void) {

	FILE *fin = fopen ( "input.txt", "rt");
	FILE *fout = fopen ( "output.txt", "wt");

	int tn;
	fscanf ( fin, "%d", &tn);

	for ( int ti = 1; ti <= tn; ti++) {
		fscanf ( fin, "%d %d", &N, &K);
		for ( int i = 0; i < N; i++) {
			fscanf ( fin, "%s", Board[ i]);
		}

		red_flag = blue_flag = 0;

		Check();
		Flip();
		Check();
		
		if ( red_flag && blue_flag) 
			fprintf ( fout, "Case #%d: Both\n", ti);
		else if ( !red_flag && !blue_flag) 
			fprintf ( fout, "Case #%d: Neither\n", ti);
		else if ( red_flag && !blue_flag) 
			fprintf ( fout, "Case #%d: Red\n", ti);
		else if ( !red_flag && blue_flag) 
			fprintf ( fout, "Case #%d: Blue\n", ti);

	}

	fclose( fin);
	fclose( fout);

	return 0;
}