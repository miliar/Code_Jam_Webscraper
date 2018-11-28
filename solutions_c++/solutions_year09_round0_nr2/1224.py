#include <cstdio>
#include <queue>
#include <vector>

using namespace std;

inline int nextInt() 
{
	register int ans = 0, sgn = 1;
	register char ch;
	while ((ch = getchar()) < '0') if (ch == '-') sgn = -1;
	do {
		ans *= 10;
		ans += (ch - '0');
	} while ((ch = getchar()) >= '0');
	return sgn * ans;
}

#define pb push_back

const int MAXN = 110;

const int dx[] = {-1, 0, 0, 1};
const int dy[] = {0, 1, -1, 0};

const int M[] = {1, 3, 2, 4};

int h, w;

inline bool valid(int x, int y) {
	return x >= 0 && x < h && y >= 0 && y < w;
}

struct tok {
	int hi, smjer;

	tok(int _hi, int _smjer) { hi = _hi, smjer = _smjer; }

	friend inline bool operator < (const tok &A, const tok &B) {
		if (A.hi == B.hi) return M[A.smjer] < M[B.smjer];
		return A.hi < B.hi;
	}
};

int v[MAXN][MAXN];

inline int flow(int x, int y) {
	vector < tok > V;

	for (int i = 0; i < 4; ++i) {
		int nx = x + dx[i];
		int ny = y + dy[i];	
		if (valid(nx, ny) && v[nx][ny] < v[x][y]) V.pb(tok(v[nx][ny], i));
	}

	if (V.empty()) return -1;
	sort(V.begin(), V.end());
	return V[0].smjer;
}

struct state {
	int x, y, k;
	state(int _x, int _y, int _k) { x = _x, y = _y, k = _k; }
};

int comp[MAXN][MAXN], boja[MAXN], t, test;

void solve() 
{
	queue < state > Q;
	
	int compCnt = 0;
	for (int i = 0; i < h; ++i)
		for (int j = 0; j < w; ++j) if (flow(i, j) == -1) Q.push(state(i, j, compCnt++));

	while (!Q.empty()) 
	{
		state ovo = Q.front();
		Q.pop();
		comp[ovo.x][ovo.y] = ovo.k;
		for (int i = 0; i < 4; ++i) {
			int nx = ovo.x + dx[i];
			int ny = ovo.y + dy[i];
			if (valid(nx, ny) && flow(nx, ny) == 3 - i) Q.push(state(nx, ny, ovo.k));
		}
	}

	int col = 0;
	memset(boja, -1, sizeof boja);

	for (int i = 0; i < h; ++i)
		for (int j = 0; j < w; ++j) if (boja[comp[i][j]] == -1) boja[comp[i][j]] = col++;

	printf("Case #%d:\n", test);
	for (int i = 0; i < h; ++i)
		for (int j = 0; j < w; ++j) printf("%c%c", 'a' + boja[comp[i][j]], j == w - 1 ? '\n' : ' ');
}

int main(void) 
{
	t = nextInt();

	for (test = 1; test <= t; ++test)
	{
		h = nextInt();
		w = nextInt();
		for (int i = 0; i < h; ++i)
			for (int j = 0; j < w; ++j) v[i][j] = nextInt();
		solve();
	}

	return 0;
}
