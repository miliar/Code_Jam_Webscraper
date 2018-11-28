#include  <cstdio>
#include  <cstdlib>
#include  <string>
#include  <cmath>
#include  <inttypes.h>
#include  <ctype.h>
#include <algorithm>
#include <utility>
#include <iostream>
#include <vector>

using namespace std;

#define TRACE(x...)
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x" = " << x << "\n")

#define tr(it,s) for(typeof(s.begin())it=s.begin();it!=s.end();++it)
#define rep(i,n) for(int i=0; i<n; ++i)

const int INF = 0x3F3F3F3F;
const int NULO = -1;
const double EPS = 1e-10;

const int TAM = 41;
long long Co[TAM][TAM];

inline int cmp(double x, double y = 0, double tol = EPS) {
  return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1; }
  
//Binomial coefficient C[n][k] = n! / ( k! * (n-k)! )
void calc_pascal() {
  rep(i, TAM) rep(j, TAM) Co[i][j] = 0;
  for (int i = 0; i < TAM; i++) {
    Co[i][0] = Co[i][i] = 1;
    for (int j = 1; j < i; j++)
      Co[i][j] = Co[i-1][j-1] + Co[i-1][j];
  }
}

double f[TAM];
int C, N;

double alpha(int i, int k) {
	if ((C >= k) && (N >= i) && (k >= i) && (C-k >= N-i))
		return (double(Co[k][i]) / double(Co[C][N]))*double(Co[C-k][N-i]);
	else
		return 0;
}

main() {
	calc_pascal();

	int testcases, tcase;
	scanf("%d", &testcases);
	rep(tcase, testcases) {
		scanf("%d %d", &C, &N);
		f[0] = 0;
		for (int k = 1; k <= C; ++k) {
				f[k] = 1.0;
				for (int i = 1; i <= min(N,k); ++i) {
					f[k] += alpha(i,k) * f[k-i];
				}
				f[k] /= (1 - alpha(0,k));
		}
		
		//cout << "f = "; rep(i,C+1) cout << f[i] << " "; cout << endl;
		printf("Case #%d: %lf\n", tcase+1, f[C]);
	}
}
