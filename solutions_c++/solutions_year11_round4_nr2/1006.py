#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

FILE *fin = freopen("B-small-attempt5.in", "r", stdin);
FILE *fout = freopen("B.out", "w", stdout);
int main()
{
	int ncase;
	scanf("%d ", &ncase);

	for (int cases = 1; cases <= ncase; cases++) {
		int r, c, d;
		scanf("%d %d %d ", &r, &c, &d);
		vector<vector<int>> m(r, vector<int>(c, 0));
		for (int i = r - 1; i >= 0; i--) {
			char buf[255];
			scanf("%s ", &buf);
			for (int j = 0; j < c; j++) {
				m[i][j] = int(buf[j] - '0') + d;
			}
		}
		int res = 0;
		for (int k = 3; k <= min(r, c); k++) {
			for (int i = 0; i < r - k + 1; i++) {
				for (int j = 0; j < c - k + 1; j++) {
					double cy = 0.0, cx = 0.0;
					int tm = 0;
					for (int y = i; y < i + k; y++) {
						for (int x = j; x < j + k; x++) {
							if ((y == i && (x == j || x == j + k - 1)) || (y == i + k - 1 && (x == j || x == j + k - 1))) {
							}
							else {	
								tm += m[y][x];
								cy += double(m[y][x] * (y + 0.5)); cx += double(m[y][x] * (x + 0.5));
							}
						}
					}
					cy /= double(tm); cx /= double(tm);

					double vy = 0.0, vx = 0.0;
					int cnt = 0;
					for (int y = i; y < i + k; y++) {
						for (int x = j; x < j + k; x++) {
							if ((y == i && (x == j || x == j + k - 1)) || (y == i + k - 1 && (x == j || x == j + k - 1))) {
							}
							else {	
								cnt++;
								vy += y + 0.5;
								vx += x + 0.5;
							}
						}
					}

					vy /= double(cnt); vx /= double(cnt);
					
					if (fabs(vy - cy) < 1e-9 && fabs(vx - cx) < 1e-9) {
					//	cout << k << " " << endl;
						//cout << vy << " " << vx << endl;
						//cout << cy << " " << cx << endl;
						if (res < k) res = k;
					}
				}
			}
		}

		if (res < 3) printf("Case #%d: IMPOSSIBLE\n", cases);
		else printf("Case #%d: %d\n", cases, res);
	}
	return 0;
}
