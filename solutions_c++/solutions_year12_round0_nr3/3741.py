#include<iostream>
#include<cmath>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<string>
#include<set>
using namespace std;

const int maxn = 1005;
int A, B;
int num[10];

struct node {
	int x, y;
	node() {}
	node (int _x, int _y) : x(_x), y(_y) {}
	bool operator < (const node &a) const {
		if (x == a.x) {
			return y < a.y;
		}
		return x < a.x;
	}
};

set<int> hash;

bool check(int n) {
	return A <= n && n <= B;
}

int split(int n) {
	int i = 0;
	while (n) {
		num[i++] = n % 10;
		n /= 10;
	}
	reverse(num, num + i);
	return i;
}

int cal(int n) {
	int len = split(n);
	int cnt = 0;
//	printf("len = %d\n", len);
	
//	for (int i = 0; i < len; i++) {
//		printf("%d", num[i]);
//	}
//	printf("\n");
	hash.clear();
	for (int i = 0; i < len; i++) {
		int m = num[i];
		for (int j = (i + 1) % len; j != i; j = (j + 1) % len) {
			m = m * 10 + num[j];
		}
//		printf("m = %d\n", m);
		if (n < m && check(m)) {
			if (hash.find(m) == hash.end()) {
				hash.insert(m);
				cnt ++;
			}
		}
	}
	return cnt;
}

int main( ) {
	freopen("C-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for (int t = 1; t <= cas; t++) {
		scanf("%d%d", &A, &B);
		int ans = 0;
		for (int i = A; i <= B; i++) {
			ans += cal(i);
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
