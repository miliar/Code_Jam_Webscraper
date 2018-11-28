#include<cstdio>
#include<algorithm>
#define N 500
#define D 5000
#define L 15
using namespace std;

int n, d, l;
char Dic[ D][ L + 2];
char Pattern[ N][ 600];
bool hasLetter[ N][ L][ 30];

int main( void) {

	FILE *fin = fopen ( "input.txt", "rt");

	fscanf ( fin, "%d %d %d", &l, &d, &n);

	for ( int i = 0; i < d; i++) {
		fscanf ( fin, "%s", Dic[ i]);
		for ( int j = 0; j < l; j++)
			Dic[ i][ j] -= 'a';
	}
	for ( int i = 0; i < n; i++) {
		fscanf( fin, "%s", Pattern[ i]);
		for ( int j = 0; j < l; j++)
			for ( int k = 0; k < 28; k++)
				hasLetter[ i][ j][ k] = 0;
	}

	fclose( fin);

	for ( int i = 0; i < n; i++) {
		int index = 0;
		for ( int j = 0; j < l; j++) {
			if ( Pattern[ i][ index] == '(') {
				index++;
				for ( ;;) {
					if ( Pattern[ i][ index] == ')') {
						index++;
						break;
					}
					hasLetter[ i][ j][ (int)( Pattern[ i][ index] - 'a')] = 1;
					index++;
				}
			} else {
				hasLetter[ i][ j][ (int)( Pattern[ i][ index] - 'a')] = 1;
				index++;
			}
		}
	}

	FILE *fout = fopen( "output.txt", "wt");

	for ( int i = 0; i < n; i++) {
		int cnt = 0;
		for ( int j = 0; j < d; j++) {
			bool is_ok = 1;
			for ( int k = 0; k < l; k++)
				is_ok = is_ok && hasLetter[ i][ k][ Dic[ j][ k]];
			if ( is_ok)
				cnt++;
		}
		fprintf( fout, "Case #%d: %d\n", i + 1, cnt);
	}
	fclose( fout);
			

	return 0;
}
