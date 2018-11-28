#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <memory.h>
#include <algorithm>

using namespace std;

#pragma comment(linker,"/STACK:16000000")

#define fi(a, b) for (i=a; i<=b; i++)
#define fj(a, b) for (j=a; j<=b; j++)
#define fo(a, b) for (o=a; o<=b; o++)
#define fdi(a, b) for (i=a; i>=b; i--)
#define fdj(a, b) for (j=a; j>=b; j--)
#define fdo(a, b) for (o=a; o>=b; o--)

#define ZERO(a) memset(a, 0, sizeof(a))

#define MAX 105

int t;
int n, m;
char ans[MAX][MAX];
int matr[MAX][MAX];
int ansq;

struct Rec {
	int x, y;
	int a;
	int d;
	bool operator <(const Rec &r) const {
		if (a != r.a) return a < r.a;
		return d < r.d;
	}
};

int X[4] = {0,-1,1,0};
int Y[4] = {-1,0,0,1};

bool Field(int x, int y) {
	if (x < 1 || x > n) return false;
	if (y < 1 || y > m) return false;
	return true;
}

char dfs(int x, int y) {
	if (ans[y][x]) return ans[y][x];
	int i;
	int q;
	int x2, y2;
	Rec rec[10];
	q = 0;
	fi(0, 4) {
		x2 = x + X[i];
		y2 = y + Y[i];
		if (!Field(x2, y2)) continue;
		if (matr[y2][x2] >= matr[y][x]) continue;
		q++;
		rec[q].a = matr[y2][x2];
		rec[q].d = i;
		rec[q].x = x2;
		rec[q].y = y2;
	}
	if (q == 0) {
		ans[y][x] = ansq + 'a';
		ansq++;
	} else {
		sort(rec + 1, rec + q + 1);
		ans[y][x] = dfs(rec[1].x, rec[1].y);
	}
	return ans[y][x];
}

void Solve() {
	int i, j;
	fj(1, m) {
		fi(1, n) {
			if (ans[j][i]) continue;
			dfs(i, j);
		}
	}
}

int main() {
	int i, j, o;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d", &t);
	fo(1, t) {
		scanf("%d %d", &m, &n);
		ZERO(matr);
		ZERO(ans);
		fj(1, m) {
			fi(1, n) {
				scanf("%d", &matr[j][i]);
			}
		}
		ansq = 0;
		Solve();
		printf("Case #%d:\n", o);
		fj(1, m) {
			fi(1, n) {
				printf("%c ", ans[j][i]);
			}
			printf("\n");
		}
	}
	return 0;
}