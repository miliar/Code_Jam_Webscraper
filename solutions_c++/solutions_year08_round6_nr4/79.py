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
const char filename_r[] = "D-small-attempt0.in";
//const char filename_r[] = "D.txt";
const char filename_w[] = "D.out";
int a1[100], b1[100], a2[100], b2[100], a3[100], b3[100];
bool p;
VI v;
int cnt;

struct point {
	int x, y;

	bool operator < (const point &r) const {
		return (x != r.x ? x < r.x : y < r.y);
	}
	bool operator == (const point &r) const {
		return x == r.x && y == r.y;
	}
};

point pt;
vector<point> vp1, vp2;

int main() {
	fp_r = fopen(filename_r, "r");
	fp_w = fopen(filename_w, "w");

	fscanf(fp_r, "%d", &t);
	REP(i, t) {
		fscanf(fp_r, "%d", &n);
		REP(j, n - 1) {
			fscanf(fp_r, "%d %d", &a1[j], &b1[j]);
			a1[j]--;	b1[j]--;
		}

		vp1.clear();
		fscanf(fp_r, "%d", &m);
		REP(j, m - 1) {
			fscanf(fp_r, "%d %d", &a2[j], &b2[j]);
			a2[j]--;	b2[j]--;
			pt.x = min(a2[j], b2[j]);
			pt.y = max(a2[j], b2[j]);
			vp1.pb(pt);
		}
		sort(vp1.begin(), vp1.end());

		p = false;
		v.clear();
		REP(j, n)
			v.pb(j);

		while(1) {
	//		REP(j, n)
	//			printf("%d ", v[j]);
	//		printf("\n");

			cnt = 0;
			REP(j, n - 1) {
				a3[cnt] = v[a1[j]];
				b3[cnt] = v[b1[j]];
				if (a3[cnt] < m && b3[cnt] < m)
					cnt++;
			}

			if (m - 1 == cnt) {
				vp2.clear();
				REP(j, cnt) {
					pt.x = min(a3[j], b3[j]);
					pt.y = max(a3[j], b3[j]);
					vp2.pb(pt);
				}
				sort(vp2.begin(), vp2.end());

				p = true;
				REP(j, m - 1) {
					if (vp1[j] == vp2[j]) continue;
					p = false;
					break;
				}

				if (p) break;
			}

			if (!next_permutation(v.begin(), v.end())) break;
		}
		

		fprintf(fp_w, "Case #%d: %s\n", i+1, (p ? "YES" : "NO"));
	}

	fclose(fp_r);
	fclose(fp_w);
	
	return 0;
}