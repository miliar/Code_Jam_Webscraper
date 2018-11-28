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

int t, n, m;
FILE *fp_r, *fp_w;
const char filename_r[] = "A-small-attempt1.in";
//const char filename_r[] = "A.txt";
const char filename_w[] = "A.out";
char bird[100];
VI v1, v2;
int x[1000], y[1000], type[1000];
int lx, ly, rx, ry;
int px, py;

int main() {
	fp_r = fopen(filename_r, "r");
	fp_w = fopen(filename_w, "w");

	fscanf(fp_r, "%d", &t);
	REP(i, t) {
		fscanf(fp_r, "%d", &n);
		v1.clear();
		v2.clear();
		REP(j, n) {
			fscanf(fp_r, "%d %d ", &x[j], &y[j]);
			fgets(bird, 100, fp_r);

			if (strncmp(bird, "BIRD", 4) == 0) {
				v1.pb(x[j]);
				v2.pb(y[j]);
				type[j] = 0;
			}
			else 
				type[j] = 1;
		}

		sort(v1.begin(), v1.end());
		sort(v2.begin(), v2.end());

		lx = ly = -999999999;
		rx = ry = 999999999;

		REP(j, n) {
			if (sz(v1) == 0) break;
			if (type[j] == 0) continue;

			if (x[j] >= v1[0] && x[j] <= v1[sz(v1)-1]) {
				// handle y
				if (y[j] < v2[0]) ly = max(ly, y[j]);
				if (y[j] > v2[sz(v2)-1]) ry = min(ry, y[j]);
			}
			else {
				// handle x
				if (x[j] < v1[0]) lx = max(lx, x[j]);
				if (x[j] > v1[sz(v1)-1]) rx = min(rx, x[j]);
			}
		}

		fprintf(fp_w, "Case #%d:\n", i+1);
		fscanf(fp_r, "%d", &m);
		REP(j, m) {
			fscanf(fp_r, "%d %d", &px, &py);

			if (sz(v1) == 0) {
				bool b = false;
				REP(k, n) {
					if (px == x[k] && py == y[k]) {
						fprintf(fp_w, "NOT BIRD\n");
						b = true;
						break;
					}
				}
				if (!b) fprintf(fp_w, "UNKNOWN\n");
				continue;
			}

			if (px >= v1[0] && px <= v1[sz(v1)-1] && py >= v2[0] && py <= v2[sz(v2)-1])
				fprintf(fp_w, "BIRD\n");
			else if (px <= lx || px >= rx || py <= ly || py >= ry)
				fprintf(fp_w, "NOT BIRD\n");
			else
				fprintf(fp_w, "UNKNOWN\n");
		}
	}

	fclose(fp_r);
	fclose(fp_w);
	
	return 0;
}