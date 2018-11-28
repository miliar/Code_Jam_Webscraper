#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <queue>
using namespace std;

#define FOR(i,n) for (int i = 0; i < n; i++)
#define abs(x) ((x)<0?(-(x)):(x))
#define REP(i,v) for (unsigned i = 0; i < v.size(); i++)
#define RL(i,v) for (unsigned i = 0; i < v.length(); i++)
typedef long long ll;


struct vec2 {
	ll x, y;
	vec2() {}
	vec2(ll x, ll y): x(x), y(y) {}
};

int a[512][512];
vec2 b[512][512];
vec2 S[512][512];
ll   F[512][512];
int R, C;


inline vec2 operator + (const vec2& a, const vec2& b)
{
	return vec2(a.x + b.x, a.y + b.y);
}

inline vec2 operator - (const vec2& a, const vec2& b)
{
	return vec2(a.x - b.x, a.y - b.y);
}

inline vec2 operator * (const vec2& a, ll m)
{
	return vec2(a.x * m, a.y * m);
}

inline bool operator == (const vec2& a, const vec2& b)
{
	return (a.x == b.x) && (a.y == b.y);
}

inline vec2 query(int x0, int y0, int sx, int sy)
{
	return S[y0 + sy - 1][x0 + sx - 1] - S[y0 - 1][x0 + sx - 1] - S[y0 + sy - 1][x0 - 1] + S[y0 - 1][x0 - 1];
}

inline ll queryA(int x0, int y0, int sx, int sy)
{
	return F[y0 + sy - 1][x0 + sx - 1] - F[y0 - 1][x0 + sx - 1] - F[y0 + sy - 1][x0 - 1] + F[y0 - 1][x0 - 1];
}

bool good(int SZ)
{
// 	int offs = (SZ + 1) / 2;
	ll num = SZ * SZ - 4;
	for (int y = 1; y <= 1 + R - SZ; y++) {
		for (int x = 1; x <= 1 + C - SZ; x++) {
			
			vec2 expected;
			if (SZ % 2 == 0) {
				expected.x = ((SZ - 1) + 2*x);
				expected.y = ((SZ - 1) + 2*y);
			} else {
				expected.x = (x + SZ/2) * 2;
				expected.y = (y + SZ/2) * 2;
			}
			int x1 = x + SZ - 1;
			int y1 = y + SZ - 1;
			vec2 t = query(x, y, SZ, SZ) - b[y][x] - b[y][x1] - b[y1][x] - b[y1][x1];
			vec2 Z = t*2;
			ll oo[5] = {queryA(x, y, SZ, SZ), (ll) a[y][x], (ll) a[y][x1], (ll) a[y1][x], (ll) a[y1][x1]};
			ll o = oo[0] - oo[1] - oo[2] - oo[3] - oo[4];
			vec2 Y = expected * o;
			if (Y == Z) return true;
			
/*			if (
			// vertical 
				query(x, y, SZ, SZ/2) - a[y][x] - a[y][x1] == query(x, y + offs, SZ, SZ/2) - a[y1][x] - a[y1][x1] &&
			// horizontal
				query(x, y, SZ/2, SZ) - a[y][x] - a[y1][x] == query(x + offs, y, SZ/2, SZ) - a[y][x1] - a[y1][x1])
				return true;*/
		}
	}
	return false;
}

void solve(void)
{
	int DDD;
	scanf("%d%d%d", &R, &C, &DDD);
	char t[1000];
	FOR(i, R) {
		scanf("%s", t);
		FOR(j, C)
			a[i+1][j+1] = ((int) (t[j] - '0')) + DDD;
	}
	memset(S, 0, sizeof(S));
	memset(F, 0, sizeof(F));
	for (int i = 1; i <= R; i++) for (int j = 1; j <= C; j++) {
		b[i][j] = vec2(j, i) * a[i][j];
		S[i][j] = S[i - 1][j] + S[i][j - 1] - S[i - 1][j - 1] + b[i][j];
		F[i][j] = F[i - 1][j] + F[i][j - 1] - F[i - 1][j - 1] + (ll) a[i][j];
	}
	cout << S[R][C].x << " " << S[R][C].y << " " << F[R][C] << endl;
	int maxx = 0;
	for (int SZ = 3; SZ <= min(R, C); SZ++) {
		if (good(SZ)) maxx = SZ;
	}
	if (maxx) printf("%d\n", maxx);
	else printf("IMPOSSIBLE\n");
}


int main(void)
{
// 	freopen("/home/vesko/gcj/b.in", "rt", stdin);
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		printf("Case #%d: ", tc);
		solve();
	}
	return 0;
}
