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
int t, n;
int i, j, k, l;
char s[20];
int c, len;

int d[4][2] = {{-1,0}, {0,1}, {1,0}, {0,-1}};
int px, py, dir;
int bd[500][500];

struct point {
	int x, y;
};
queue<point> q;
point p;
int cnt;
int x, y;
bool a1, a2;

int main() {
	fp_r = fopen("A-small.txt", "r");
	fp_w = fopen("A.out", "w");

	fscanf(fp_r, "%d", &t);
	for(i = 0; i < t; i++) {
		fscanf(fp_r, "%d", &n);

		dir = 0;
		px = 250;	py = 250;
		memset(bd, 0, sizeof(bd));
		bd[px][py] = 1;
		for(j = 0; j < n; j++) {
			fscanf(fp_r, "%s %d", s, &c);
			
			len = strlen(s);
			for(k = 0; k < c; k++) {
				for(l = 0; l < len; l++) {
					if (s[l] == 'F') {
						px += d[dir][0];
						py += d[dir][1];
						bd[px][py] = 1;
						px += d[dir][0];
						py += d[dir][1];
						bd[px][py] = 1;
					}
					else {
						if (s[l] == 'L') dir = (dir + 3) % 4;
						if (s[l] == 'R') dir = (dir + 1) % 4;
					}
				}
			}
		}

		p.x = 0; p.y = 0;
		bd[p.x][p.y] = -1;
		q.push(p);
		while(1) {
			if (q.empty()) break;

			p = q.front();			
			for(k = 0; k < 4; k++) {
				p = q.front();
				p.x += d[k][0];
				p.y += d[k][1];
				if (p.x < 0 || p.x >= 500 || p.y < 0 || p.y >= 500) continue;
				if (bd[p.x][p.y] != 0) continue;
				bd[p.x][p.y] = -1;
				q.push(p);
			}

			q.pop();
		}

        cnt = 0;
		for(j = 0; j < 500; j++) {
			for(k = 0; k < 500; k++) {
				if (bd[j][k] != -1) continue;

				a1 = false;
				x = j-1;
				while(x >= 0) {
					if (bd[x][k] != -1) {
						a1 = true;
						break;
					}
					x--;
				}

				a2 = false;
				x = j+1;
				while(x < 500) {
					if (bd[x][k] != -1) {
						a2 = true;
						break;
					}
					x++;
				}

				if (a1 && a2) {
					bd[j][k] = 7;
					if (j % 2 != 0 && k % 2 != 0)
						cnt++;
					continue;
				}

				a1 = false;
				y = k-1;
				while(y >= 0) {
					if (bd[j][y] != -1) {
						a1 = true;
						break;
					}
					y--;
				}

				a2 = false;
				y = k+1;
				while(y < 500) {
					if (bd[j][y] != -1) {
						a2 = true;
						break;
					}
					y++;
				}

				if (a1 && a2) {
					bd[j][k] = 7;
					if (j % 2 != 0 && k % 2 != 0)
						cnt++;
					continue;
				}
			}
		}

		fprintf(fp_w, "Case #%d: %d\n", i+1, cnt);		
	}

	fclose(fp_r);
	fclose(fp_w);

	return 0;
}