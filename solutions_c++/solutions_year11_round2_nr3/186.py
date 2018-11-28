#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

const int MAXN = 2010;

map<int, int> mm;
vector< vector<int> > circle;
int cas, n, m, c[MAXN], u[MAXN], v[MAXN];

inline void cut(int ui, int vi) {
	int ci = 0;
	for (int i = 0; i < circle.size(); ++i) {
		const vector<int>& cir = circle[i];
		bool f1 = false, f2 = false;
		for (int j = 0; j < cir.size(); ++j) {
			if (cir[j] == ui)
				f1 = true;
			else if (cir[j] == vi)
				f2 = true;
		}
		if (f1 && f2) {
			ci = i;
			break;
		}
	}
	//int ci = mm[ui];
	vector<int> cir = circle[ci];
	circle.erase(circle.begin() + ci);
	vector<int> left, right;
	int si = 0;
	for (int i = 0; i < cir.size(); ++i) {
		if (cir[i] == ui) {
			si = i;
			break;
		}
	}
	int n = cir.size(), si2 = 0;
	for (int i = si; ; i = (i + 1)%n) {
		left.push_back(cir[i]);
		if (cir[i] == vi) {
			si2 = i;
			break;
		}
	}
	for (int i = si2; ; i = (i + 1) % n) {
		right.push_back(cir[i]);
		if (cir[i] == ui) {
			break;
		}
	}
	for (int i = 0; i < left.size(); ++i)
		mm[ left[i] ] = circle.size();
	circle.push_back(left);
	for (int i = 0; i < right.size(); ++i)
		mm[ right[i] ] = circle.size();
	circle.push_back(right);
}

inline void show() {
	for (int i = 0; i < circle.size(); ++i) {
		const vector<int>& cir = circle[i];
		for (int j = 0; j < cir.size(); ++j)
			printf("%d ", cir[j]);
		puts("");
	}
}

int mmo;
int color[MAXN], ans[MAXN], vv[MAXN];

inline bool ok() {
	for (int i = 0; i < circle.size(); ++i) {
		const vector<int>& cir = circle[i];
		memset(vv, 0, sizeof(int) * mmo);
		for (int j = 0; j < cir.size(); ++j) {
			vv[ color[cir[j]] ] = true;
		}
		for (int j = 0; j < mmo; ++j) {
			if (! vv[j])
				return false;
		}
	}
	return true;
}

bool dfs(int i) {
	if (i == n + 1) {
		if (ok()) {
			memcpy(ans, color, sizeof(int) * (n + 10));
			//printf("ok : ");
			//for (int jj = 1; jj < i; ++jj)
			//	printf("%d ", color[jj]);
			//puts("");
			return true;
		} else {
			return false;
		}
	}
	for (int j = 0; j < mmo; ++j) {
		color[i] = j;
		if (dfs(i + 1))
			return true;
	}
	return false;
}

int main() {
	//freopen("B-large.in", "r", stdin);
	//freopen("B-large.out", "w", stdout);
	freopen("C-small-attempt2.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	//freopen("in.txt", "r", stdin);
	scanf("%d", &cas);
	for (int c = 1; c <= cas; ++c) {
		scanf("%d%d", &n, &m);
		vector<int> cir;
		for (int i = 1; i <= n; ++i)
			cir.push_back(i);
		mm.clear();
		circle.clear();
		circle.push_back(cir);
		for (int i = 1; i <= n; ++i)
			mm[i] = 0;
		for (int i = 0; i < m; ++i) {
			scanf("%d", &u[i]);
		}
		for (int i = 0; i < m; ++i) {
			scanf("%d", &v[i]);
		}
		//printf("n = %d, m = %d\n", n, m);
		for (int i = 0; i < m; ++i) {
			//printf("\t%d %d\n", u[i], v[i]);
			//printf("n = %d, %d/%d : %d %d\n", n, i, m, u[i], v[i]);
			cut(u[i], v[i]);
		}

		//puts("");
		//show();

		int most = 0;
		for (int i = 0; i < circle.size(); ++i)
			most = max(most, (int)circle[i].size());
		for (mmo = most; mmo >= 1; --mmo) {
			if (dfs(1))
				break;
		}
		printf("Case #%d: %d\n", c, mmo);
		for (int i = 1; i <= n; ++i) {
			if (i > 1) putchar(' ');
			printf("%d", ans[i] + 1);
		}
		puts("");
	}
	return 0;
}