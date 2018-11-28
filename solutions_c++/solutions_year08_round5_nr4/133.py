#include <algorithm> 
#include <bitset> 
#include <cassert>
#include <cmath> 
#include <complex>
#include <cstdio> 
#include <cstdlib> 
#include <cstring>
#include <ctime> 
#include <deque> 
#include <functional> 
#include <iomanip> 
#include <iostream> 
#include <list> 
#include <map> 
#include <numeric> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <stack> 
#include <utility> 
#include <vector> 
using namespace std; 

#define ALL(x) (x).begin(), (x).end()
#define MP make_pair
#define SZ(x) ((int) (x).size())
#define max2(x,y) ((x) = max((x),(y)))
#define min2(x,y) ((x) = min((x),(y)))
typedef long long LL;

bool rock[128][128];
int w[128][128];

int main()
{
	int T;
	scanf("%d", &T);
	for (int TT = 1; TT <= T; ++TT) {
		memset(rock, 0, sizeof rock);
		int H, W, R;
		scanf("%d %d %d", &H, &W, &R);
		while (R--) {
			int r, c;
			scanf("%d %d", &r, &c);
			rock[r][c] = true;
		}

		w[1][1] = 1;
		for (int r = 2; r <= H; ++r) {
			for (int c = 1; c <= W; ++c) {
				w[r][c] = 0;
				if (rock[r][c])
					continue;
				int nr, nc;
				nr = r-2;
				nc = c-1;
				if (nr >= 1 && nc >= 1)
					w[r][c] += w[nr][nc];
				nr = r-1;
				nc = c-2;
				if (nr >= 1 && nc >= 1)
					w[r][c] += w[nr][nc];
				w[r][c] %= 10007;
			}
		}
		printf("Case #%d: %d\n", TT, w[H][W]);
	}

	return 0;
}
