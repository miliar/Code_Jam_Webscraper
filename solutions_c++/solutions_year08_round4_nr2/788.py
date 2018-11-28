#include <cstdio>
#include <cstring>
#include <iostream>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>

using namespace std;

#define EPS 1e-8

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef vector<double> VD;
typedef pair<int, int> PII;
typedef set<int> SI;
typedef map<int, int> MII;

int m, n;
double A;
int p[4][2];

double getarea() {
	double area = 0.0;
	for(int i = 1; i+1<3; i++){
	    int x1 = p[i][0] - p[0][0];
	    int y1 = p[i][1] - p[0][1];
	    int x2 = p[i+1][0] - p[0][0];
	    int y2 = p[i+1][1] - p[0][1];
	    int cross = x1*y2 - x2*y1;
	    area += cross;
	}
	double ret = abs(area / 2.0);
	return ret;
}

int main() {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int cases;
	scanf("%d", &cases);
	for (int cc = 1; cc <= cases; ++cc) {
		printf("Case #%d: ", cc);
		int tt;
		cin >> m >> n >> tt;
		int ok = 0;
		A = (double)tt * 0.5;
		for (int a = 0; a <= m && !ok; ++a)
			for (int b = 0; b <= n && !ok; ++b)
				for (int c = 0; c <= m && !ok; ++c)
					for (int d = 0; d <= n && !ok; ++d)	{
						if ((a == 0 && b == 0) || (c == 0 && d == 0)) continue;
						p[0][0] = a, p[0][1] = b;
						p[1][0] = c, p[1][1] = d;						
						p[2][0] = 0, p[2][1] = 0;												
						double tmp = getarea();
						if (fabs(tmp - A) <= EPS) {
							printf("%d %d %d %d %d %d\n", a, b, c, d, 0, 0);
							ok = 1;
							break;
						}
					}
				
		if (!ok) puts("IMPOSSIBLE");
	}
	return 0;
}

