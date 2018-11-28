#include <iostream>
#include <string.h>
using namespace std;

bool map[2][210][210];

bool test(int idx) {
	for(int i = 0; i < 210; i ++) {
		for(int j = 0; j < 210; j ++) {
			if(map[idx][i][j])	return false;
		}
	}
	return true;
}

void output(int idx) {
	for(int y = 0; y < 20; y ++) {
		for(int x = 0; x < 20; x ++) {
			cout << map[idx][y][x] << " ";
		}
		cout << endl;
	}
	cout << endl;
}

int main() {
	freopen("C-small.in", "r", stdin);
	freopen("c-small.out", "w", stdout);
	int t;
	cin >> t;
	for(int idx = 1; idx <= t; idx ++ ) {
		int k;
		cin >> k;
		int x1, y1, x2, y2;
		memset(map, 0, sizeof(map));
		for(int i = 0; i < k; i ++) {
			//cout << "k = " << k << endl;
			cin >> x1 >> y1 >> x2 >> y2;
			for(int y = y1; y <= y2; y ++) {
				for(int x = x1; x <= x2; x ++) {
					map[0][y][x] = true;
				//	cout << "..." << endl;
				}
			}
			//cout << "over" << endl;
		}
		//cout << "input over!" << endl;
		int now = 0;
		int ans = 0;
		for(; !test(now); ans ++) {
			int other = now ^ 1;
			for(int y = 0; y < 210; y ++) {
				for(int x = 0; x < 210; x ++) {
					map[other][y][x] = 0;
				}
			}
			
			for(int y = 1; y < 210; y ++) {
				for(int x = 1; x < 210; x ++) {
					if(map[now][y-1][x] && map[now][y][x-1]) {
						map[other][y][x] = true;
					}
				}
			}
			
			
			for(int y = 1; y < 210; y ++) {
				for(int x = 1; x < 210; x ++) {
					if(!map[now][y][x])	continue;
					if(map[now][y-1][x] || map[now][y][x-1])	map[other][y][x] = 1;
				}
			}
			now = other;
		}
		printf("Case #%d: %d\n", idx, ans);
		//cout << endl;
		//cout << "final !~!" << endl;
	}
	return 0;
}
