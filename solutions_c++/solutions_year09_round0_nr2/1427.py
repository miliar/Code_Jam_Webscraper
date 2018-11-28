#include <iostream>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

map <int, char> H;

vector <int> Q;

int h[101*101], p[101*101];

int a[101][101], b[101][101];

int getp(int v) {
	return v == p[v] ? v : (p[v] = getp(p[v]));
}

void Union(int v1, int v2) {
	v1 = getp(v1); v2 = getp(v2);
	if (h[v1] > h[v2])
		h[v1] += h[v2], p[v2] = v1;
	else
		h[v2] += h[v1], p[v1] = v2;
}

void solve(int n, int m) {
	int k = 0;
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j) {
			p[k + 1] = k + 1;
			b[i][j] = ++k;
		}

	memset(h, 0, sizeof(h));
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j) {
		     int v1 = 1e9, v2 = 1e9, v3 = 1e9, v4 = 1e9;
		     if (i - 1 >= 0) {
		     	v1 = a[i - 1][j];
		     }
		     if (j - 1 >= 0) {
		     	v2 = a[i][j - 1];
		     }
		     if (i + 1 < n) {
		     	v4 = a[i + 1][j];
		     }
		     if (j + 1 < m) {
		     	v3 = a[i][j + 1];
		     }
		     int Min = min(v1, min(v2, min(v3, v4)));
		     if (Min < a[i][j]) {
			     if (i - 1 >= 0 && Min == a[i - 1][j]) {
			     	Union(b[i - 1][j], b[i][j]);
//			     	cout << i << " " << j << "1\n";
			     } else
			     if (j - 1 >= 0 && Min == a[i][j - 1]) {
			     	Union(b[i][j - 1], b[i][j]);
//			     	cout << i << " " << j << "2\n";
			     } else
			     if (j + 1 < m && Min == a[i][j + 1]) {
			     	Union(b[i][j + 1], b[i][j]);
//			     	cout << i << " " << j << "3\n";
			     } else
			     if (i + 1 < n && Min == a[i + 1][j]) {
			     	Union(b[i + 1][j], b[i][j]);
//			     	cout << i << " " << j << "4\n";
			     }
		     }
		}

	Q.clear();
	H.clear();

	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
			Q.push_back(getp(b[i][j]));
	sort(Q.begin(), Q.end());
	Q.erase(unique(Q.begin(), Q.end()), Q.end());
	for (int i = 0; i < n; ++i) {
		int v;
		for (int j = 0; j < m; ++j) {
			v = getp(b[i][j]);
			b[i][j] = lower_bound(Q.begin(), Q.end(), v) - Q.begin();
		}
	}

	char ch = 'a';
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			if (H.find(b[i][j]) == H.end()) {
				printf("%c ",ch);
				H[b[i][j]] = ch++;
			} else
				printf("%c ",H[b[i][j]]);
		}
		printf("\n");
	}
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		int n, m;
		scanf("%d%d", &n, &m);
		for (int u = 0; u < n; ++u)
			for (int j = 0; j < m; ++j)
				scanf("%d", &a[u][j]);
		printf("Case #%d:\n",i);
		solve(n, m);
	}

	return 0;
}
