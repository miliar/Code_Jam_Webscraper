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
#include <valarray>
#include <vector> 
using namespace std; 

#define ALL(x) (x).begin(), (x).end()
#define MP make_pair
#define SZ(x) ((int) (x).size())
#define max2(x,y) ((x) = max((x),(y)))
#define min2(x,y) ((x) = min((x),(y)))
typedef long long LL;

int R, C;
int BASINS;
int alt[128][128];
int basin[128][128];

int get_alt(int r, int c)
{
	if (r < 0 || r >= R || c < 0 || c >= C)
		return 12345;
	return alt[r][c];
}

int get_basin(int r, int c)
{
	if (basin[r][c] != 0)
		return basin[r][c];

	int a = get_alt(r, c);
	int north, west, east, south;
	north = get_alt(r-1, c  );
	west  = get_alt(r  , c-1);
	east  = get_alt(r  , c+1 );
	south = get_alt(r+1, c  );
	if (north >= a && west >= a && east >= a && south >= a) {
		basin[r][c] = ++BASINS;
		return BASINS;
	}

	if (north <= west && north <= east && north <= south) {
		basin[r][c] = get_basin(r-1, c  );
	} else if (west <= east && west <= south) {
		basin[r][c] = get_basin(r  , c-1);
	} else if (east <= south) {
		basin[r][c] = get_basin(r  , c+1);
	} else {
		basin[r][c] = get_basin(r+1, c  );
	}

	return basin[r][c];
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int TC = 1; TC <= T; ++TC) {
		scanf("%d %d", &R, &C);
		for (int r = 0; r < R; ++r) {
			for (int c = 0; c < C; ++c) {
				scanf("%d", &alt[r][c]);
			}
		}
		BASINS = 0;
		memset(basin, 0, sizeof basin);
		for (int r = 0; r < R; ++r) {
			for (int c = 0; c < C; ++c) {
				get_basin(r, c);
			}
		}

		map<int, char> m;
		int cur_char = 'a';
		printf("Case #%d:\n", TC);
		for (int r = 0; r < R; ++r) {
			for (int c = 0; c < C; ++c) {
				if (m[basin[r][c]] == 0) {
					m[basin[r][c]] = cur_char;
					cur_char += 1;
				}

				printf("%c ", m[basin[r][c]]);
			}
			printf("\n");
		}
	}
	return 0;
}
