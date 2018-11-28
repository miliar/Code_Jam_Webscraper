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

const int MX = 7000;

namespace aaa {

bool hor_went[MX][MX];
bool ver_went[MX][MX];
bool up[MX][MX];
bool down[MX][MX];
bool left[MX][MX];
bool right[MX][MX];

bool pup[MX][MX];
bool pleft[MX][MX];

};

enum { NORTH, WEST, SOUTH, EAST };

int main()
{
	using namespace aaa;
	int T;
	scanf("%d", &T);
	for (int TT = 1; TT <= T; ++TT) {
		int R = MX/2, C = MX/2, D = 0;

		int L;
		scanf("%d", &L);
		memset(hor_went, 0, sizeof hor_went);
		memset(ver_went, 0, sizeof ver_went);
		while (L--) {
			char buf[64];
			int c;
			scanf("%s %d", buf, &c);
			while (c--) {
				for (int i = 0; buf[i] != 0; ++i) {
					int ch = buf[i];
					if (ch == 'R') {
						D = (D+3) % 4;
						continue;
					}
					if (ch == 'L') {
						D = (D+1) % 4;
						continue;
					}
					switch (D) {
					case NORTH:
						R -= 1;
						ver_went[R][C] = true;
						break;
					case SOUTH:
						ver_went[R][C] = true;
						R += 1;
						break;
					case WEST:
						C -= 1;
						hor_went[R][C] = true;
						break;
					case EAST:
						hor_went[R][C] = true;
						C += 1;
						break;
					}
				}
			}
		}
		memset(up, 0, sizeof up);
		memset(down, 0, sizeof down);
		memset(aaa::left, 0, sizeof aaa::left);
		memset(aaa::right, 0, sizeof aaa::right);
		memset(pup, 0, sizeof pup);
		memset(pleft, 0, sizeof pleft);

		for (int r = 1; r < MX; ++r)
			for (int c = 0; c < MX; ++c)
				up[r][c] |= (up[r-1][c] || hor_went[r][c]);
		for (int r = MX-2; r >= 0; --r)
			for (int c = 0; c < MX; ++c)
				down[r][c] |= (down[r+1][c] || hor_went[r][c]);
		for (int r = 0; r < MX; ++r)
			for (int c = 1; c < MX; ++c)
				aaa::left[r][c] |= (aaa::left[r][c-1] || ver_went[r][c]);
		for (int r = 0; r < MX; ++r)
			for (int c = MX-2; c >= 0; --c)
				aaa::right[r][c] |= (aaa::right[r][c+1] || ver_went[r][c]);

		for (int r = 1; r < MX; ++r)
			for (int c = 0; c < MX; ++c)
				pup[r][c] = pup[r-1][c] ^ hor_went[r][c];
		for (int r = 0; r < MX; ++r)
			for (int c = 1; c < MX; ++c)
				pleft[r][c] |= pleft[r][c-1] ^ ver_went[r][c];

		int A = 0;
		for (int r = 2; r < MX-2; ++r) {
			for (int c = 2; c < MX-2; ++c) {
				if (pup[r][c] != pleft[r][c]) {
					puts("BUG!");
					return -1;
				}
				bool inside = pup[r][c];
				if (inside) continue;
				if ((up[r][c] && down[r+1][c]) || (aaa::left[r][c] && aaa::right[r][c+1]))
					A += 1;
			}
		}
		printf("Case #%d: %d\n", TT, A);
		fflush(stdout);
	}

	return 0;
}
