#include<cstdio>
#include<cmath>
#include<algorithm>
using namespace std;

#define N 100
#define M 25

int n, m;
int P[ N][ M];
bool G[ N][ N];
int ngroup, ng[ N], gmember[ N][ N];
int ans;

void Grouping( int x) {

	if ( ans <= ngroup) return;

	if ( x == n) {
		ans =  ngroup;
		return;
	}

	for ( int i = 0; i < ngroup; i++) {

		bool is_ok = 1;
		for ( int j = 0; j < ng[ i]; j++) {
			if ( G[ x][ gmember[ i][ j]])
				is_ok = 0;
		}

		if ( is_ok) {
			gmember[ i][ ng[ i]++] = x;
			Grouping( x + 1);
			ng[ i]--;
		}

	}

	ng[ ngroup] = 1;
	gmember[ ngroup][ 0] = x;
	ngroup++;
	Grouping( x + 1);
	ngroup--;
}

int prs( void) {

	ans = n;

	for ( int i = 0; i < n; i++) {
		for ( int j = 0; j < n; j++) {
			bool is_cross = 0;
			for ( int k = 0; k < m - 1; k++) {
				if ( (long long)( P[ i][ k] - P[ j][ k]) * ( P[ i][ k + 1] - P[ j][ k + 1]) <= 0) {
					is_cross = 1;
				}
			}
			G[ i][ j] = is_cross;
		}
	}

	ngroup = 0;
	Grouping( 0);

	return ans;

}

int main( void) {

	int testnum;
	FILE *fin = fopen ( "input.txt", "rt");
	FILE *fout = fopen ( "output.txt", "wt");

	fscanf( fin, "%d", &testnum);

	for ( int testcase = 1; testcase <= testnum; testcase++) {
		
		fscanf( fin, "%d %d", &n, &m);
		for ( int i = 0; i < n; i++) {
			for ( int j = 0; j < m; j++) {
				fscanf ( fin, "%d", &P[ i][ j]);
			}			
		}			

		fprintf( fout, "Case #%d: %d\n", testcase, prs());

	}
	return 0;
}