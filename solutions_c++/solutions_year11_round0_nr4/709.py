#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

#define ABS(x) ( (x)<0.0 ? -(x) : (x) )
#define EPS 1E-9

typedef double tint;

#define MAXN 1024

tint p[MAXN][MAXN], a[MAXN][MAXN];

void gaussjordan(tint **A, int M, int N) {
	int i, j, k, maxi;

	for (i=0; i<M; i++) {
		maxi = i;
		for (k=i+1; k<M; k++) {
			if (ABS(A[k][i]) > ABS(A[maxi][i])) maxi = k;
		}

		for (j=0; j<N; j++) swap(A[i][j], A[maxi][j]);

		if (A[i][i] < EPS) cout << "ERROR" << endl;

		for (j=0; j<N; j++) {
			if (j != i) A[i][j] /= A[i][i];
		}
		A[i][i] = 1;

		for (k=0; k<M; k++) {
			if (k != i) {
				for (j=i+1; j<N; j++)
					A[k][j] -= A[k][i]*A[i][j];
				A[k][i] = 0;
			}
		}
	}
}

int main() {

freopen("in.txt", "r", stdin);

int i, j, N, C, t, T;
tint tmp, *aa[MAXN];

for (i=0; i<MAXN; i++) aa[i] = a[i];

p[0][0] = 1.0;
for (i=1; i<MAXN; i++) {
	p[i][0] = 1.0;

	tmp = 1.0;
	for (j=1; j<=i; j++) {
		tmp /= j;
		p[i][j] = tmp*p[i-j][0];
		p[i][0] -= p[i][j];
	}
}

cin >> T;

for (t=1; t<=T; t++) {

cin >> N;

C = 0;
for (i=1; i<=N; i++) {
	cin >> j;
	if (i==j) C++;
}

for (i=0; i<=N; i++) {
	for (j=0; j<i; j++) a[i][j] = 0.0;
	a[i][i] = 1.0 - p[N-i][0];
	for (j=i+1; j<=N; j++) a[i][j] = -p[N-i][j-i];
}
a[N][N] = 1.0;

for (i=0; i<N; i++) a[i][N+1] = 1;
a[N][N+1] = 0;

gaussjordan(aa, N+1, N+2);

printf("Case #%d: %.6lf\n", t, a[C][N+1]);

}

return 0;
}
