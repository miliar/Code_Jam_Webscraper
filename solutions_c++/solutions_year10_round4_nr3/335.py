#include <iostream>
#include <cmath>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <algorithm>
#include <numeric>
#include <functional>
#include <cstdlib>
#include <cassert>

using namespace std;

bool a[128][128];

int main() {
	freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	
	int tests;
	cin >> tests;
	for (int t = 1; t <= tests; ++t) {
		printf("Case #%d: ", t);
	
		for (int i = 0; i < 128; ++i) {
			for (int j = 0; j < 128; ++j) {
				a[i][j] = false;
			}
		}
		int r = 0;
		cin >> r;
		for (int i = 0; i < r; ++i) {
			int x1, y1, x2, y2;
			cin >> x1 >> y1 >> x2 >> y2;
			if (x1 > x2) { int t = x1; x1 = x2; x2 = t; } 
			if (y1 > y2) { int t = y1; y1 = y2; y2 = t; } 
			for (int x = x1; x <= x2; ++x) {
				for (int y = y1; y <= y2; ++y) {
					a[y][x] = true;
				}
			}
		}
		
		int cnt = 0;
		bool ok = true;
		while (ok) {
			
			/*cout << endl;
			for (int i = 0; i < 8; ++i) {
				for (int j = 0; j < 8; ++j) {
					cout << a[i][j];
				}
				cout << endl;
			}
			cout << endl;*/

			cnt++;
			ok = false;
			for (int x = 100; x >= 1; --x) {
				for (int y = 100; y >= 1; --y) {
					if (!a[x][y] && a[x-1][y] && a[x][y-1]) {
						a[x][y] = true;
					}
					else if (a[x][y] && !a[x-1][y] && !a[x][y-1]){
						a[x][y] = false;
					}
					if (a[x][y]) {
						ok = true;
					}					
				}
			} 
		}
		
		printf("%d\n", cnt);
	}
	return 0;
}
