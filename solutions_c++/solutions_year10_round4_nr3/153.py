#include<vector>
#include<string>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<set>
#include<map>
#include<sstream>
#include<queue>
#include<climits>
#include<cmath>
using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;

int N;

struct mat {
	int m[200][200];
} data, tmp;

void debug(mat* tmp) {
	for(int x = 0; x < 6; ++x) {
		for(int y = 0; y < 6; ++y) {
			cout << tmp->m[x][y];
		}
		cout << endl;
	}
	cout << endl;
}

inline int solve() {
	mat *curr = &data;
	mat *next = &tmp;
	int ret = 0;
	bool init = false;
	for(int x = 0; x < 200; ++x) {
		for(int y = 0; y < 200; ++y) {
			if(curr->m[x][y]) {
				init = true;
				break;
			}
		}
	}
	if(!init) return 0;
	while(1) {
		//debug(curr);
		bool has = false;
		for(int x = 0; x < 200; ++x) {
			for(int y = 0; y < 200; ++y) {
				const bool hasw = (x > 0 && curr->m[x-1][y]);
				const bool hasn = (y > 0 && curr->m[x][y-1]);
				if(curr->m[x][y]) {
					if(!hasw && !hasn) {
						next->m[x][y] = 0;
					} else {
						has = true;
						next->m[x][y] = 1;
					}
				} else {
					if(hasw && hasn) {
						next->m[x][y] = 1;
						has = true;
					} else {
						next->m[x][y] = 0;
					}
				}
			}
		}
		++ret;
		if(!has) break;
		swap(next, curr);
	}
	return ret;
}

int main() {
	int T; cin >> T;
	for(int tt = 1; tt <= T; ++tt) {
		for(int x = 0; x < 200; ++x)
			for(int y = 0; y < 200; ++y)
				data.m[x][y] = 0;
		cin >> N;
		for(int i = 0; i < N; ++i) {
			int x1, y1, x2, y2;
			cin >> x1 >> y1 >> x2 >> y2;
			--x1; --y1; --x2; --y2;
			for(int x = x1; x <= x2; ++x) {
				for(int y = y1; y <= y2; ++y) {
					data.m[x][y] = 1;
				}
			}
		}
		int ans = solve();
		cout << "Case #" << tt << ": " << ans << endl;
	}
	return 0;
}

