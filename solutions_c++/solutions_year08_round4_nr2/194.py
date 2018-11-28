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

int DET(int a, int b, int c, int d) {
	return a*d - b*c;
}

int main() {
	int tc;
	scanf("%d", &tc);
	for (int scen=1; scen<=tc; ++scen) {
		printf("Case #%d: ", scen);
		int n, m, a;
		scanf("%d %d %d", &n, &m, &a);
		for (int x2=0; x2<=n; ++x2)
			for (int y2=0; y2<=m; ++y2)
				for (int x3=0; x3<=n; ++x3)
					for (int y3=0; y3<=m; ++y3) {
						int area = abs(DET(x2, x3, y2, y3));
						if (area == a) {
							printf("0 0 %d %d %d %d\n", x2,y2,x3,y3);
							goto done;
						}
					}
		puts("IMPOSSIBLE");
		done:;
	}
	return 0;
}
