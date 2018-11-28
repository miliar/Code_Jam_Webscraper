#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <queue>
#include <list>
#include <stack>
#include <string>
#include <fstream>
#include <math.h>
#include <limits>
#include <set>
#include <map>
#include <sstream>
#include <stdio.h>
#include <time.h>
#include <memory.h>
using namespace std;

#define ALL(ar)       (ar).begin(),(ar).end()
#define SZ(a)         int((a).size())
#define MP(a,b)       make_pair(a,b)
#define INF           0x7f7f7f7f
typedef long long     LL;
typedef vector<int>   VI;
typedef pair<int,int> II;

/* @date    03.09.2009
 * @idea    Find connected components
 */

const int dh[] = {-1, 0, 0, 1};
const int dw[] = {0, -1, 1, 0};

int all = 0;
int T;
int H, W;
int alt[100][100];
int bas[100][100];
int lb[26]; // letter of basin

// return the drainage basin id
int go (int _i, int _j) {
	if (bas[_i][_j] == INF) // unused
	{
		int dd = -1, mini = alt[_i][_j];
		for (int k = 0; k < 4; k++) {
			int h = _i + dh[k], w = _j + dw[k];
			if (h >= 0 && h < H && w >= 0 && w < W && alt[h][w] < mini)
				mini = alt[h][w], dd = k;
		}
		bas[_i][_j] = dd == -1 ? all++ : go (_i + dh[dd], _j + dw[dd]);
	}
	return bas[_i][_j];
}

int main()
{
	freopen("in.in", "rt", stdin);
	freopen("out.out", "wt+", stdout);

	scanf ("%d", &T);
	for (int tc = 0; tc < T; tc++)
	{
		// Input
		scanf ("%d %d", &H, &W);
		for (int i = 0; i < H; i++)
			for (int j = 0; j < W; j++)
				scanf ("%d", alt[i]+j);
	
		// DFS solution
		all = 0;
		memset (bas, 0x7f7f7f7f, sizeof (bas));
		for (int i = 0; i < H; i++)
			for (int j = 0; j < W; j++)
				bas[i][j] = go (i, j);

		// Mark and output
		printf ("Case #%d:\n", tc+1);
		all = 0;
		memset (lb, -1, sizeof (lb));
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W; j++) {
				if (lb[bas[i][j]] == -1)
					lb[bas[i][j]] = all++;
				putchar ('a' + lb[bas[i][j]]);
				putchar (' ');
			}
			putchar ('\n');
		}
	}

	return 0;
}