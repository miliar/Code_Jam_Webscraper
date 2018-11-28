#include<cstdio>
#include<algorithm>
using namespace std;

int D[ 31];

int main( void) {

	D[ 1] = 1;
	for ( int i = 2; i <= 30; i++)
		D[ i] = D[ i - 1] * 2 + 1;

	FILE *fin = fopen( "input.txt", "rt");
	FILE *fout = fopen ( "output.txt", "wt");
	int testnum;
	fscanf(  fin, "%d", &testnum);
	for ( int testcase = 1; testcase <= testnum; testcase++) {
		int N, K;
		fscanf ( fin, "%d %d", &N, &K);
		int r;
		r = (K + 1) % (D[ N] + 1);
		if ( r == 0)
			fprintf ( fout, "Case #%d: ON\n", testcase);
		else 
			fprintf ( fout, "Case #%d: OFF\n", testcase);
	}

	return 0;
}