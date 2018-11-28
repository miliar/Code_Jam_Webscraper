#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <map>
#include <algorithm>
#include <vector>
using namespace std;

int nCase=1, T, N;

double WP[100], OWP[100], OOWP[100];
int W[100];
int P[100];

int res[100][100];


void input() {
	char s[101];
	for(int i=0;i<N;++i) {
		scanf("%s", &s);
		for(int j=0;j<N;++j) {
			if ( s[j] == '.' ) res[i][j] = 0;
			else {
				res[i][j] = (s[j]=='1'?1:-1);
			}
		}
	}
}

void calc() {
	for(int i=0;i<N;++i) {
		int pc = 0, wc = 0;
		for(int j=0;j<N;++j) {
			if( res[i][j] != 0 ) ++pc;
			if( res[i][j] == 1 ) ++wc;
		}
		WP[i] = (double)wc/(double)pc;
		P[i] = pc;
		W[i] = wc;
	}
	for(int i=0;i<N;++i) {
		OWP[i] = 0;
		for(int j=0;j<N;++j) {
			if( res[i][j] != 0 ) {
				int win = (res[i][j]==1?0:1);
				OWP[i] += (double)(W[j]-win)/(double)(P[j]-1);
			}
		}
		OWP[i] /= (double)(P[i]);
	}
	for(int i=0;i<N;++i) {
		OOWP[i] = 0;
		for(int j=0;j<N;++j) {
			if( res[i][j] != 0 ) {
				OOWP[i] += OWP[j];
			}
		}
		OOWP[i] /= (double)P[i];
	}
}

void output() {
	for(int i=0;i<N;++i) {
//		printf("(%d, %d) (%.2f, %.2f, %.2f) \t", W[i], P[i], WP[i], OWP[i], OOWP[i]);
		printf("%.7f\n", (0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]));
	}
}

int main()
{
	scanf("%d", &T);
	while(T-->0) {
		scanf("%d", &N);
	    input();
	    calc();
	
		printf( "Case #%d:\n", nCase++);
		output();
	}
	return 0;
}
