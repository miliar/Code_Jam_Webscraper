//#pragma comment(linker, "/STACK:128000000")
//
//#include <iostream>
//#include <string>
//#include <algorithm>
//#include <vector>
//#include <set>
//#include <map>
//#include <cmath>
//
//using namespace std;
//
//int n;
//int s[1000];
//int sum;
//
//double Score(int id, double share) {
//	return 1. * s[id] + sum * share / 100.;
//}
//
//bool Eliminate(int id, double share) {
//	double score = Score(id, share);
//	share = 100. - share;
//	for (int i = 0; i < n; ++i) {
//		if (i == id) {
//			continue;
//		}
//
//		double x = (1. * score - s[i]) / sum * 100;
//		if (x < 0) {
//			x = 0;
//		}
//		share -= x;
//	}
//
//	return (share >= -1e-7);
//}
//
//void Out(int id) {
//	double L = 0, R = 100;
//	for (int step = 0; step < 100; ++step) {
//		double mid = (L + R) / 2.;
//		if (Eliminate(id, mid)) {
//			L = mid;
//		} else {
//			R = mid;
//		}
//	}
//	printf("%lf ", (L + R) / 2.);
//}
//
//void Solve() {
//	sum = 0;
//	cin >> n;
//	for (int i = 0; i < n; ++i) {
//		cin >> s[i];
//		sum += s[i];
//	}
//
//	for (int i = 0; i < n; ++i) {
//		Out(i);
//	}
//	printf("\n");
//}
//
//int main() {
//	freopen("in.txt", "r", stdin);
//	freopen("out.txt", "w", stdout);
//	int t;
//	cin >> t;
//	for (int i = 1; i <= t; ++i) {
//		printf("Case #%d: ", i);
//		Solve();
//	}
//	return 0;
//}

#pragma comment(linker, "/STACK:128000000")

#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>

using namespace std;

int h, n, m;
int c[100][100], f[100][100];
double d[100 * 100 * 7];
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};

int Hash(int x, int y) {
	return x * m + y;
}

pair<int, int> deHash(int val) {
	return pair<int, int>(val / m, val % m);
}

bool NoWay(int x, int y, int nx, int ny) {
	int f1 = f[x][y];
	int f2 = f[nx][ny];
	int c1 = c[x][y];
	int c2 = c[nx][ny];
	if (c2 - f2 < 50) {
		return true;
	}
	if (c1 - f2 < 50) {
		return true;
	}
	if (c2 - f1 < 50) {
		return true;
	}
	return false;
}

int Top(int x, int y, int nx, int ny) {
	int f1 = f[x][y];
	int f2 = f[nx][ny];
	int c1 = c[x][y];
	int c2 = c[nx][ny];
	return min(c1, c2) - 50;
}

void Solve() {
	cin >> h >> n >> m;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			cin >> c[i][j];
		}
	}

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			cin >> f[i][j];
		}
	}
	
	int FN = Hash(n - 1, m - 1);
	for (int i = 0; i <= FN; ++i) {
		d[i] = 1e10;
	}
	d[0] = 0;

	set<pair<double, int> > Q;
	Q.insert(make_pair(0, 0));
	while (!Q.empty()) {
		pair<double, int> tmpO = *Q.begin();
		Q.erase(Q.begin());
		double curDist = tmpO.first;
		int v = tmpO.second;
		pair<int, int> ppp = deHash(tmpO.second);
		int x = ppp.first, y = ppp.second;
		for (int i = 0; i < 4; ++i) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx < 0 || nx >= n) {
				continue;
			}
			if (ny < 0 || ny >= m) {
				continue;
			}

			if (NoWay(x, y, nx, ny)) {
				continue;
			}
			
			double curH = h;
			double top = Top(x, y, nx, ny);
			double add = 0;
			if (curH <= top) {
				/**/
			} else {
				continue;
			}
			if (curH - f[x][y] >= 20.) {
				add += 1;
			} else {
				add += 10;
			}

			int u = Hash(nx, ny);
			if (d[u] > d[v] + add) {
				Q.erase(make_pair(d[u], u));
				d[u] = d[v] + add;
				Q.insert(make_pair(d[u], u));
			}
		}
	}

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			int v = Hash(i, j);
			if (d[v] < 1e10) {
				d[v] = 0;
				Q.insert(make_pair(d[v], v));
			}
		}
	}

	while (!Q.empty()) {
		pair<double, int> tmpO = *Q.begin();
		Q.erase(Q.begin());
		double curDist = tmpO.first;
		int v = tmpO.second;
		pair<int, int> ppp = deHash(tmpO.second);
		int x = ppp.first, y = ppp.second;
		for (int i = 0; i < 4; ++i) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx < 0 || nx >= n) {
				continue;
			}
			if (ny < 0 || ny >= m) {
				continue;
			}

			if (NoWay(x, y, nx, ny)) {
				continue;
			}
			
			double curH = h - 10 * curDist;
			double newcurH = curH;
			double top = Top(x, y, nx, ny);
			double add = 0;
			if (curH <= top) {
				/**/
			} else {
				add += (curH - top) / 10.;
				newcurH = curH - (curH - top);
			}
			if (newcurH - f[x][y] >= 20.) {
				add += 1;
			} else {
				add += 10;
			}

			int u = Hash(nx, ny);
			if (d[u] > d[v] + add) {
				Q.erase(make_pair(d[u], u));
				d[u] = d[v] + add;
				Q.insert(make_pair(d[u], u));
			}
		}
	}

	printf("%lf\n", d[FN]);
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: ", i);
		Solve();
	}
	return 0;
}