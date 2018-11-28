// Adrian Kügel
#include <stdio.h>
#include <vector>
#include <set>
#include <queue>
#include <math.h>
#include <stdlib.h>
#include <map>
#include <assert.h>
#include <limits.h>
#include <complex>
#include <algorithm>
#include <ctype.h>
#include <string>
using namespace std;

typedef set<int> SI;
typedef vector<int> VI;
typedef vector<string> VS;
typedef complex<double> tComp;

int main() {
	int tc;
	scanf("%d", &tc);
	for (int scen=1; scen<=tc; ++scen) {
		printf("Case #%d: ", scen);
		long long n, A, B, C, D, x0, y0, M;
		scanf("%lld %lld %lld %lld %lld %lld %lld %lld", &n, &A, &B, &C, &D, &x0, &y0, &M);
		long long X = x0;
		long long Y = y0;
		long long c[3][3] = {{0}};
		++c[X%3][Y%3];
		for (int i=1; i<n; ++i) {
			X = (A*X + B) % M;
			Y = (C*Y + D) % M;
			++c[X%3][Y%3];
		}
		long long cnt = 0;
		for (int i=0; i<3; ++i)
			for (int j=0; j<3; ++j)
				for (int k=0; k<3; ++k) {
					if ((i + j + k) % 3)
						continue;
					for (int ii=0; ii<3; ++ii)
						for (int jj=0; jj<3; ++jj)
							for (int kk=0; kk<3; ++kk) {
								if ((ii + jj + kk)%3)
									continue;
								long long c1 = c[i][ii];
								long long c2 = c[j][jj];
								if (i == j && ii == jj)
									--c2;
								long long c3 = c[k][kk];
								if (i == k && ii == kk)
									--c3;
								if (j == k && jj == kk)
									--c3;
								cnt += c1 * c2 * c3;
							}
				}
		printf("%lld\n", cnt / 6);
	}
	return 0;
}
