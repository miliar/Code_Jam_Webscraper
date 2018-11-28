// Adrian Kügel
#include <stdio.h>
#include <vector>
#include <set>
#include <queue>
#include <math.h>
#include <stdlib.h>
#include <map>
#include <assert.h>
#include <limits.h>
#include <complex>
#include <algorithm>
#include <ctype.h>
#include <string>
using namespace std;

typedef set<int> SI;
typedef vector<int> VI;
typedef vector<string> VS;
typedef complex<double> tComp;
typedef pair<short, int> PCI;

char grid[60][64];
char grid2[60][64];

char answer[4][20] = {"Neither", "Blue", "Red", "Both"};

int n, k;
int dirs[4][2] = {{0,1},{1,0},{1,1},{1,-1}};

int findK(char c) {
	for (int i=0; i<n; ++i) {
		for (int j=0; j<n; ++j) {
			for (int d=0; d<4; ++d) {
				int cnt = 0;
				int x = i;
				int y = j;
				for (int ii=0; ii<k; ++ii) {
					if (grid2[x][y] != c)
						break;
					++cnt;
					x += dirs[d][0];
					y += dirs[d][1];
					if (x < 0 || x >= n || y < 0 || y >= n)
						break;
				}
				if (cnt == k)
					return 1;
			}
		}
	}
	return 0;
}

int main() {
	int tc;
	scanf("%d", &tc);
	for (int scen=1; scen<=tc; ++scen) {
		printf("Case #%d: ", scen);
		scanf("%d %d", &n, &k);
		for (int i=0; i<n; ++i)
			scanf("%s", grid[i]);
		for (int i=0; i<n; ++i)
			for (int j=0; j<n; ++j)
				grid2[i][j] = grid[j][n-i-1];
		for (int j=0; j<n; ++j) {
			int p = 0;
			for (int i=0; i<n; ++i)
				if (grid2[i][j] != '.')
					grid2[p++][j] = grid2[i][j];
			while(p < n)
				grid2[p++][j] = '.';
		}
		int which = findK('R') * 2 + findK('B');
		printf("%s\n", answer[which]);
	}
	return 0;
}
