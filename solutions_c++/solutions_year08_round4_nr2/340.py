#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <functional>
#include <algorithm>

#define sqr(a) ((a) * (a))
#define eps 1.0e-12
#define pi (2.0 * acos(0.0))
#define sz(a) ((int)a.size())
#define clr(a, b) (memset(a, b, sizeof(a)))
#define pb push_back
#define FORS(i, a, b, s) for(int i = (a); i < (b); i+=(s))
#define FOR(i, a, b) FORS(i, a, b, 1)
#define REP(i, a) FOR(i, 0, a)
#define FORI(i, a, b) for(i = (a); i != (b); ++i)

using namespace std;

typedef long long ll;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef set<int> SI;

FILE *fp_r, *fp_w;
int t, n, m, a;
int i, j, k, x, y;
bool b;
int area;

int main() {

	fp_r = fopen("B-small.txt", "r");
	fp_w = fopen("B.out", "w");

	fscanf(fp_r, "%d", &t);
	for(i = 0; i < t; i++) {
		fscanf(fp_r, "%d %d %d", &n, &m, &a);

		fprintf(fp_w, "Case #%d:", i+1);
		b = false;
		for(j = 1; j <= n; j++) {
			for(k = 1; k <= m; k++) {
				if (j * k * 2 < a) continue;
				for(x = 0; x < k; x++) {
					for(y = j; y > 0; y--) {
						area = j * k * 2 - j * x - k * y - (j - y) * (k - x);
						if (area == a) {
							fprintf(fp_w, " 0 0 %d %d %d %d\n", j, x, y, k);
							b = true;
							break;
						}
					}
					if (b) break;
				}
				if (b) break;
			}
			if (b) break;
		}

		if (!b) fprintf(fp_w, " IMPOSSIBLE\n");
	}

	fclose(fp_r);
	fclose(fp_w);

	return 0;
}