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
int t, n, m;
int i, j, k;
int x, y;

struct node {
	bool val;
	int type; // 0 : leaf , 1 : or , 2 : and
	int ch; // 0 : fixed , 2 : non-fixed
};

node tree[11000];
int dp[11000][2];

int main() {

	fp_r = fopen("A-large.in", "r");
	fp_w = fopen("A.out", "w");

	fscanf(fp_r, "%d", &t);
	for(i = 0; i < t; i++) {
		fscanf(fp_r, "%d %d", &n, &m);
		for(j = 0; j < (n-1)/2; j++) {
			fscanf(fp_r, "%d %d", &tree[j].type, &tree[j].ch);
			tree[j].type++;
			tree[j].val = true;
		}
		for(j = (n-1)/2; j < n; j++) {
			fscanf(fp_r, "%d", &tree[j].val);
			tree[j].type = 0;
			tree[j].ch = 0;
		}

		for(j = 0; j < n; j++)
			for(k = 0; k < 2; k++)
				dp[j][k] = -1;

		for(j = n-1; j >= 0; j--) {
			if (tree[j].type == 0) {
				dp[j][tree[j].val] = 0;
			}
			else {
				if (tree[j].ch == 0) {
					for(x = 0; x < 2; x++) {
						if (dp[j*2+1][x] == -1) continue;
						for(y = 0; y < 2; y++) {
							if (dp[j*2+2][y] == -1) continue;

							bool val;
							if (tree[j].type == 1) val = x || y;
							else if (tree[j].type == 2) val = x && y;
							if (dp[j][val] == -1)
								dp[j][val] = dp[j*2+1][x] + dp[j*2+2][y];
							else
								dp[j][val] = min(dp[j][val], dp[j*2+1][x] + dp[j*2+2][y]);
						}
					}					
				}
				else {
					for(x = 0; x < 2; x++) {
						if (dp[j*2+1][x] == -1) continue;
						for(y = 0; y < 2; y++) {
							if (dp[j*2+2][y] == -1) continue;

							bool val;
							if (tree[j].type == 1) val = x || y;
							else if (tree[j].type == 2) val = x && y;
							if (dp[j][val] == -1)
								dp[j][val] = dp[j*2+1][x] + dp[j*2+2][y];
							else
								dp[j][val] = min(dp[j][val], dp[j*2+1][x] + dp[j*2+2][y]);

							if (tree[j].type == 1) val = x && y;
							else if (tree[j].type == 2) val = x || y;
							if (dp[j][val] == -1)
								dp[j][val] = dp[j*2+1][x] + dp[j*2+2][y] + 1;
							else
								dp[j][val] = min(dp[j][val], dp[j*2+1][x] + dp[j*2+2][y] + 1);
						}
					}
				}
			}
		}

		fprintf(fp_w, "Case #%d: ", i+1);
		if (dp[0][m] == -1) fprintf(fp_w, "IMPOSSIBLE\n");
		else fprintf(fp_w, "%d\n", dp[0][m]);
	}

	fclose(fp_r);
	fclose(fp_w);

	return 0;
}