#include <cstdio>
#include <cmath>
#include <cstring>
#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <algorithm>
#include <string>
using namespace std;
const int N = 110;
int a[2][N][N];
void print() {
	for (int i=1; i<=5; ++i) {
		for (int j=1; j<=5; ++j) printf("%d", a[0][i][j]);
		puts("");
	}
	puts("");
}
int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for (int cass=1; cass<=cas; ++cass) {
		int n;
		scanf("%d", &n);
		memset(a[0], 0,  sizeof(a[0]));
		for (int i=0; i<n; ++i) {
			int x1, y1, x2, y2;
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			for (int j=x1; j<=x2; ++j)
				for (int k=y1; k<=y2; ++k) a[0][j][k] = 1;
		}
		int pre=0, nxt=1;
		int res=0;
		while (1) {
//			print();
			++res;
			bool  flag = true;
			for (int i=1; i<=100; ++i) {
				for (int j=1; j<=100; ++j) {
					if (a[pre][i-1][j]==0 && a[pre][i][j-1]==0) {
						a[nxt][i][j] = 0;
						continue;
					}
					if (a[pre][i-1][j]==1 && a[pre][i][j-1]==1) {
						a[nxt][i][j] = 1;
						flag = false;
						continue;
					}
					a[nxt][i][j] = a[pre][i][j];
					if (a[pre][i][j]) flag = false;
				}
			}
			if (flag) {
				printf("Case #%d: %d\n", cass, res);
				break;
			}
			swap(pre, nxt);
		}
	}
	return 0;
}
