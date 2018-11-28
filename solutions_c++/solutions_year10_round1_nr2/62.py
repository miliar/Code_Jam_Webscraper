#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>
#include <set>
#include <map>

using namespace std;

const int MAXN = 105;

#define LEFT(a) (a << 1)
#define RIGHT(a) ((a << 1) | 1)

int T;
int D, A, M, N;
int mem[MAXN];

int dp[MAXN][256];

int tree[1024];
inline void maketree(int *x) {
	for(int i = 256 ; i < 512 ; i++) {
		tree[i] = x[i - 256];
	}
	for(int i = 255 ; i >= 1 ; i--) {
		tree[i] = min(tree[LEFT(i)], tree[RIGHT(i)]);
	}
}

inline int query(int x, int y, int ind = 1, int l = 0, int r = 255) {
	x = max(l, x);
	y = min(r, y);
	if (y < x) {return 55555;}
	if (x == l && y == r) {return tree[ind];}
	int mid = (l + r) >> 1;
	return min(query(x, y, LEFT(ind), l, mid), query(x, y, RIGHT(ind), mid + 1, r));
}

inline void checkmin(int &a, int b) {a = min(a, b);}

inline void checkabs(int *x) {
	int val = x[0];
	for(int i = 1 ; i < 256 ; i++) {
		val++;
		if (x[i] < val) {
			val = x[i];
		}	else {
			x[i] = val;
		}
	}
	val = x[255];
	for(int i = 254 ; i >= 0 ; i--) {
		val++;
		if (x[i] < val) {
			val = x[i];
		}	else {
			x[i] = val;
		}
	}
}

inline void checkadd(int *x) {
	for(int i = 1 ; i < 256 ; i++) {
		checkmin(x[i], query(max(0, i - M), i) + A);
	}
	for(int i = 254 ; i >= 0 ; i--) {
		checkmin(x[i], query(i, min(255, i + M)) + A);
	}
}

pair< int , int > q[256];
int front, back;

inline void check(int *x) {
	front = back = 0;
	q[back++] = make_pair(0, x[0]);
	for(int i = 1 ; i < 256 ; i++) {
		while(front < back && q[front].first + M < i) {front++;}
		checkmin(x[i], q[front].second + A);
		while (front < back && q[back - 1].second >= x[i]) {back--;}
		q[back++] = make_pair(i, x[i]);
	}
	front = back = 0;
	q[back++] = make_pair(255, x[255]);
	for(int i = 254 ; i >= 0 ; i--) {
		while(front < back && q[front].first - M > i) {front++;}
		checkmin(x[i], q[front].second + A);
		while (front < back && q[back - 1].second >= x[i]) {back--;}
		q[back++] = make_pair(i, x[i]);
	}
}

int calc[256];
inline void init() {
	calc[0] = 0;
	for(int i = 1 ; i < 256 ; i++) {
		calc[i] = 55555;
		for(int j = 1 ; j <= M ; j++) {
			if (i - j < 0) {break;}
			checkmin(calc[i], calc[i - j] + A);
		}
	}
}

inline int myabs(int a) {return (a < 0 ? -a : a);}

int main() {
	scanf("%d",&T);
	for(int t = 1 ; t <= T ; t++) {
		scanf("%d %d %d %d",&D,&A,&M,&N);
		for(int i = 1 ; i <= N ; i++) {
			scanf("%d",&mem[i]);
			for(int j = 0 ; j < 256 ; j++) {
				dp[i][j] = 55555;
			}
		}
		init();
		for(int j = 0 ; j < 256 ; j++) {dp[0][j] = 0;}
		int ans = N * D;

		for(int i = 1 ; i <= N ; i++) {
			maketree(dp[i - 1]);
			for(int j = 0 ; j < 256 ; j++) {
				checkmin(dp[i][j], myabs(j - mem[i]) + query(max(0, j - M), min(255, j + M)));
			}
			if (M > 0) {
				check(dp[i]);
			}
			for(int j = 0 ; j < 256 ; j++) {
				checkmin(dp[i][j], dp[i - 1][j] + D);
			}
		}
		for(int j = 0 ; j < 256 ; j++) {
			ans = min(ans, dp[N][j]);
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
