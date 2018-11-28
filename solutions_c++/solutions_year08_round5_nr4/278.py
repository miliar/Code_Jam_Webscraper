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
int t, n, m, c;
int i, j, k;
int rock[100][100];
long long way[100][100];
int x, y;

int main() {
	fp_r = fopen("D-small.txt", "r");
	fp_w = fopen("D.out", "w");

	fscanf(fp_r, "%d", &t);
	for(i = 0; i < t; i++) {
		fscanf(fp_r, "%d %d %d", &n, &m, &c);

		memset(way, 0, sizeof(way));
		memset(rock, 0, sizeof(rock));
		for(j = 0; j < c; j++) {
			fscanf(fp_r, "%d %d", &x, &y);
			x--;	y--;
			rock[x][y] = 1;
		}

		way[0][0] = 1;
		for(j = 0; j < n; j++) {
			for(k = 0; k < m; k++) {
				if (j - 1 >= 0 && k - 2 >= 0 && rock[j-1][k-2] == 0)
					way[j][k] += way[j-1][k-2];
				if (j - 2 >= 0 && k - 1 >= 0 && rock[j-2][k-1] == 0)
					way[j][k] += way[j-2][k-1];

				way[j][k] %= 10007;
			}
		}
		
		fprintf(fp_w, "Case #%d: %I64d\n", i+1, way[n-1][m-1]);
	}

	fclose(fp_r);
	fclose(fp_w);

	return 0;
}