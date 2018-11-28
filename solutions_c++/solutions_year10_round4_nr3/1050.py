/*
 * C.cpp
 *
 *  Created on: Jun 5, 2010
 *      Author: Administrator
 */

/*
 ID: Manal Sadek
 LANG: C++
 TASK:
 */

#include <map>
#include <set>
#include <math.h>
#include <deque>
#include <stack>
#include <queue>
#include <vector>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <memory.h>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,s,m) for(int i=s;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define PI = (2.0 * acos(0.0));
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define OO ((int)1e9)

int n = 105;
int grid[105][105];
int newG[105][105];

int main() {
	freopen("C.in", "rt", stdin);
	freopen("C.out", "wt", stdout);
	int t = 0, T, x1, x2, y1, y2;
	cin >> T;
	while (t++ < T) {
		int  cnt = 0;
		int r;
		memset(grid, 0, sizeof(grid));
		memset(newG, 0, sizeof(newG));
		cin >> r;
		for (int i = 0; i < r; i++) {
			cin >> y1 >> x1 >> y2 >> x2;
			x1++, x2++, y1++, y2++;
			if (x1 == x2)
				for (int j = y1; j <= y2; j++)
					newG[x1][j] = grid[x1][j] = 1;
			else if (y1 == y2)
				for (int j = x1; j <= x2; j++)
					newG[j][y1] = grid[j][y1] = 1;
			else {
				for (int j = x1; j <= x2; j++)
					for (int k = y1; k <= y2; k++)
						newG[j][k] = grid[j][k] = 1;
			}
		}
		bool flag = false;
		while (!flag) {

			flag = true;
			for (int i = 1; i < n; i++)
				for (int j = 1; j < n; j++) {
					if (newG[i][j])
						flag = false;
					grid[i][j] = newG[i][j];
				}
			if (!flag) {
				for (int i = 1; i < n; i++)
					for (int j = 1; j < n; j++) {
						if (grid[i][j] && !grid[i - 1][j] && !grid[i][j - 1])
							newG[i][j] = 0;
						else if (!grid[i][j] && grid[i - 1][j]
								&& grid[i][j - 1])
							newG[i][j] = 1;
						else
							newG[i][j] = grid[i][j];
					}
					cnt++;
			}
		}
		printf("Case #%d: %d\n", t, cnt);
	}

	//  system("pause");
	return 0;
}
