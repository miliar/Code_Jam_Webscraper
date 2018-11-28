#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <queue>

using namespace std;

int N;
int step[100][2];
int dis[100][100][101];
int mk[100][100][101];

int mymin(int a, int b) {
	if ( a == -1 ) return b;
	return a < b ? a : b;
}

struct node {
	int b, o, s, d;
	bool operator < (const node &t) const {
		return d > t.d;
	}
	node (int a, int e, int c, int f):b(a), o(e), s(c), d(f) {};
	node(){};
};

int solve() {
	int ans = 0;
	int sb = 1, so = 1;
	int saveb = 0, saveo = 0;
	for (int i = 0; i < N; ++i) {
		if ( step[i][0] == 0 ) {
			int go = sb - step[i][1];
			if (go < 0 )go = -go;
			ans += 1;
			saveo += 1;
			if ( saveb < go ) {
				ans += go - saveb;
				saveo += go - saveb;
			}
			saveb = 0;
			sb = step[i][1];	
		}
		else if ( step[i][0] == 1 ) {
			int go = so - step[i][1];
			if ( go < 0 )go = -go;
			ans += 1;
			saveb += 1;
			if ( saveo < go ) {
				ans += go - saveo;
				saveb += go - saveo;
			}
			saveo = 0;
			so = step[i][1];
		}
	}
	return ans;
}
	

int main() {
	int T;
	cin >> T;
	int cas = 1;
	while (T--) {
		scanf("%d", &N); 
		for (int i = 0; i < N; ++i) {
			char str[10];
			int k;
			cin >> str >> k;
			if ( str[0] == 'B' ) {
				step[i][0] = 0;
			} else {
				step[i][0] = 1;
			}
			step[i][1] = k;
		}
		printf("Case #%d: %d\n", cas++, solve());
	}
	return 0;
}
