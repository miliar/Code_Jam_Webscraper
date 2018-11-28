#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#include <vector>
#include <set>
#include <map>
using namespace std;


long long trees_x[105];
long long trees_y[105];

int case_nr;
int cases;

long long n,A,B,C,D,xi,yi,M;

void make_trees(void) {
	long long x,y,i;

	x = xi;
	y = yi;

	trees_x[0] = x;
	trees_y[0] = y;

	for (i=1; i<n; i++) {
		x = (A * x + B) % M;
		y = (C * y + D) % M;
		trees_x[i] = x;
		trees_y[i] = y;
	}
/*
	for (i=0; i<n; i++) {
		printf("Tree %d: %d %d\n", i, trees_x[i], trees_y[i] );
	}
*/
}


int main ( int argc, char ** argv ) {
	int a,b,c;

	int mx,my;
	scanf("%d", &cases);

	for (case_nr=0; case_nr<cases; case_nr++) {
		scanf("%lld %lld %lld %lld %lld %lld %lld %lld", &n, &A, &B, &C, &D, &xi, &yi, &M);

		make_trees();

		int cnt = 0;
		for (a=0; a<n; a++) {
			for (b=a+1; b<n; b++) {
				for (c=b+1; c<n; c++) {
					mx = trees_x[a] + trees_x[b] + trees_x[c];
					my = trees_y[a] + trees_y[b] + trees_y[c];

					if ( mx % 3 ) continue;
					if ( my % 3 ) continue;

					//printf("%d %d %d is valid\n", a,b,c);
					cnt++;
				}
			}
		}
		printf("Case #%d: %d\n", case_nr+1, cnt);
	}
	return 0;
}
