#include <cstdio>
#include <algorithm>
using namespace std;

#define FOR(i, a, b) for(__typeof(a) i = (a); i < (b); i++)
#define CLEAR(a, b) memset((a), (b), sizeof(a))

const int N = 128;
const int MOD = 10007;

void add(int& a, int b) { a += b%MOD; a %= MOD; }

int main()
{
	bool stone[N][N];
	int way[N][N];
	int T;
	scanf("%d", &T);
	FOR(t, 0, T) {
		int n, m, r; scanf("%d %d %d", &n, &m, &r);
		CLEAR(stone, false);
		CLEAR(way, 0);
		FOR(i, 0, r) {
			int x, y; scanf("%d %d", &x, &y);
			stone[x-1][y-1] = true;
		}
		way[0][0] = 1;
		FOR(i, 0, n) FOR(j, 0, m) if(!stone[i][j]) {
			add(way[i+2][j+1], way[i][j]);
			add(way[i+1][j+2], way[i][j]);
		}
		printf("Case #%d: %d\n", t+1, way[n-1][m-1]);
	}
	return 0;
}

