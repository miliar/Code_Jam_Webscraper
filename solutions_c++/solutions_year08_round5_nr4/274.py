#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <utility>
#include <queue>
#include <map>
using namespace std;

typedef long long LL;
typedef unsigned int UINT32;

const int M = 10007;


LL H, W, R;

int cache[110][110];

int calc(int r, int c)
{
	if (cache[r][c] != -1) return cache[r][c];

	int & ans = cache[r][c];
	ans = 0;
	int dr[] = {2,1};
	int dc[] = {1,2};
	for (int i=0; i<2; ++i) {
		int nr = r+dr[i];
		int nc = c+dc[i];
		if (nr<=0 || nr>H || nc<=0 || nc>W) continue;
		if (cache[nr][nc] == -2) continue;

		ans += calc(nr, nc);
		ans %= M;
	}

	ans %= M;
	return ans;
}

int main(void)
{
	int N;
	cin >> N;
	for (int i=1; i<=N; ++i) {
		cin >> H >> W >> R;

		memset(cache, -1, sizeof(cache));
		for (int j=0; j<R; ++j) {
			int r, c;
			cin >> r >> c;
			cache[r][c] = -2;
		}

		cache[H][W] = 1;
		cout << "Case #" << i << ": " << calc(1, 1) << endl;
	}

	return 0;
}
