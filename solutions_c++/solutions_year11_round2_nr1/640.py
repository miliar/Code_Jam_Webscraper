#include <cstdio>
using namespace std;

char A[111][111];
int W[111], P[111];
double WP[111], OWP[111], OOWP[111];
int N;

void solve(int test) {
    printf("Case #%d:\n", test);
    scanf("%d", &N);
    for(int i = 0; i < N; ++i) {
	scanf("%s", A[i]);
	W[i] = P[i] = 0;
	for(int j = 0; j < N; ++j) {
	    if(A[i][j] == '1') {
		W[i]++;
	    }
	    if(A[i][j] != '.') {
		P[i]++;
	    }
	}
	WP[i] = 1.0 * W[i] / P[i];
    }
    for(int i = 0; i < N; ++i) {
	OWP[i] = 0.0;
	for(int j = 0; j < N; ++j) {
	    if(A[i][j] != '.') {
		int w = W[j], p = P[j] - 1;
		if(A[j][i] == '1') {
		    w--;
		}
		OWP[i] += 1.0 * w / p;
	    }
	}
	OWP[i] /= P[i];
    }
    for(int i = 0; i < N; ++i) {
	OOWP[i] = 0.0;
	for(int j = 0; j < N; ++j) {
	    if(A[i][j] != '.') {
		OOWP[i] += OWP[j];
	    }
	}
	OOWP[i] /= P[i];
	printf("%.9lf\n", 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i]);
    }
}


int main() {
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; ++i) {
	solve(i);
    }
    return 0;
}
