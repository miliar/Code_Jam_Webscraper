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

int X[101000];
int Y[101000];

LL one_cnt[101000][9];
LL two_cnt[101000][9];
LL three_cnt[101000][9];

int main()
{
	int T;
	LL n, A, B, C, D, x0, y0, M;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; ++tt) {
		scanf("%lld %lld %lld %lld %lld %lld %lld %lld", &n, &A, &B, &C, &D, &x0, &y0, &M);

		int nn = 0;
		X[nn] = x0 % 3;
		Y[nn] = y0 % 3;
		nn += 1;

		for (; nn < n; ++nn) {
			x0 = (A*x0 + B) % M;
			y0 = (C*y0 + D) % M;
			X[nn] = x0 % 3;
			Y[nn] = y0 % 3;
		}

		memset(one_cnt, 0, sizeof one_cnt);
		memset(two_cnt, 0, sizeof one_cnt);
		memset(three_cnt, 0, sizeof one_cnt);

		for (int i = n-1; i >= 0; --i) {
			for (int j = 0; j < 9; ++j) {
				int x = j / 3;
				int y = j % 3;

				one_cnt[i][j] = one_cnt[i+1][j];
				if (x == X[i] && y == Y[i])
					one_cnt[i][j] += 1;
			}
		}

		for (int i = n-1; i >= 0; --i) {
			for (int j = 0; j < 9; ++j) {
				int x = j / 3;
				int y = j % 3;

				two_cnt[i][j] = two_cnt[i+1][j] + one_cnt[i+1][(x-X[i]+6)%3*3 + (y-Y[i]+6)%3];
			}
		}

		for (int i = n-1; i >= 0; --i) {
			for (int j = 0; j < 9; ++j) {
				int x = j / 3;
				int y = j % 3;

				three_cnt[i][j] = three_cnt[i+1][j] + two_cnt[i+1][(x-X[i]+6)%3*3 + (y-Y[i]+6)%3];
			}
		}

		printf("Case #%d: %lld\n", tt, three_cnt[0][0]);
	}

	return 0;
}
