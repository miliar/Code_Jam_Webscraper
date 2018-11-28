#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

const int N = 200;
int grid[N][N], grid2[N][N];
int n;
int main()
{
	freopen("data.in", "r", stdin);
	freopen("result.out", "w", stdout);
	int tn,curt;
	cin >> tn;
	for(curt = 1; curt <= tn; ++curt){
		cout << "Case #" << curt << ": ";

		int R;
		cin >> R;
		int i, j, k;
		while(R--) {
			int x1, x2, y1, y2;
			cin >> x1 >> y1 >> x2 >> y2;
			for(i = x1; i <= x2; ++i) {
				for(j  = y1; j <= y2; ++j) {
					grid[j][i] = 1;
				}
			}
		}
		//for(i = 1; i < N; ++i) {
		//		for(j = 1; j < N; ++j) {
		//			cout << grid[i][j];
		//		}
		//		cout << endl;
		//	}
		//cout << endl;
		int ans = 0;
		bool flag = true;
		while(flag) {
			flag = false;
			for(i = 1; i < N; ++i) {
				for(j = 1; j < N; ++j) {
					if(grid[i-1][j] == 1 && grid[i][j-1] == 1) {
						 grid2[i][j] = 1; flag = true; 
					} else if(grid[i-1][j] == 0 && grid[i][j-1] == 0) grid2[i][j] = 0;
					else {
						grid2[i][j] = grid[i][j];
						if(grid2[i][j] == 1) flag = true;
					}
				}
			}
			memcpy(grid, grid2, sizeof(grid2));
			ans++;

			//for(i = 1; i < N; ++i) {
			//	for(j = 1; j < N; ++j) {
			//		cout << grid[i][j];
			//	}
			//	cout << endl;
			//}
		}
		cout << ans << endl;
	}
	return 0;
}