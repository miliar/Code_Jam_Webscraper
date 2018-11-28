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
char bd[100][110];
vector< VI > v;
int chk[100][100];
int cnt, max_cnt;
int dp[10][1024];

void find(int x, int y) {
	int p, q, r;

	if (x == n)
		return ;

	if (x > 0 && y == -1) {
		r = 0;
		for(p = 0; p < m; p++)
			r = r * 2 + chk[x-1][p];

		if (cnt < dp[x][r])
			return ;
		dp[x][r] = cnt;
	}

	for(p = y+1; p < m; p++) {
		if (x != 0) {
			if (p != 0 && chk[x-1][p-1] == 1) continue;
			if (p < m && chk[x-1][p+1] == 1) continue;
		}
		if (p != 0 && chk[x][p-1] == 1) continue;
		if (p < m && chk[x][p+1] == 1) continue;
		if (bd[x][p] == 'x') continue;

        chk[x][p] = 1;
		cnt++;
		max_cnt = max(max_cnt, cnt);
		if (p == m-1) find(x+1, -1);
		else find(x, p);
		chk[x][p] = 0;
		cnt--;
	}

	if (x == n-1)
		return ;

	r = 0;
	for(p = 0; p < m; p++)
		r = r * 2 + chk[x][p];

	if (cnt < dp[x+1][r])
		return ;
	dp[x+1][r] = cnt;

	for(p = x+1; p < n; p++) {
		for(q = 0; q < m; q++) {
			if (q != 0 && chk[p-1][q-1] == 1) continue;
			if (q < m && chk[p-1][q+1] == 1) continue;
			if (q != 0 && chk[p][q-1] == 1) continue;
			if (q < m && chk[p][q+1] == 1) continue;
			if (bd[p][q] == 'x') continue;

			chk[p][q] = 1;
			cnt++;
			max_cnt = max(max_cnt, cnt);
			if (q == m-1) find(p+1, -1);
			else find(p, q);
			chk[p][q] = 0;
			cnt--;
		}
	}
}

int main() {
	fp_r = fopen("C-small.txt", "r");
	fp_w = fopen("C.out", "w");

	fscanf(fp_r, "%d", &t);
	for(i = 0; i < t; i++) {
		fscanf(fp_r, "%d %d", &n, &m);
		for(j = 0; j < n; j++)
			fscanf(fp_r, "%s", bd[j]);

		memset(chk, 0, sizeof(chk));
		memset(dp, 0, sizeof(dp));
		max_cnt = 0;
		cnt = 0;
		find(0, -1);

		fprintf(fp_w, "Case #%d: %d\n", i+1, max_cnt);
	}

	fclose(fp_r);
	fclose(fp_w);

	return 0;
}