#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int INF = 0x7FFFFFFF;

int arr[256][256];

int n;

int getnum(int i)
{
	int m = i + 1;
	if (m > n) {
		m = n + n - m;
	}
	return m;
}

int getstt(int i)
{
	int stt = n - i;
	if (stt < 1) {
		stt = i - n + 2;
	}
	return stt;
}

bool isvalid(int row, int col)
{
	if (row < 0 || row >= n + n) return false;
	int m = getnum(row);
	int stt = getstt(row);
	int edd = stt + (m - 1) * 2;
	if (col < stt || col > edd) return false;
	return true;
}

void getsymver(int midc, int c, int &nc)
{
	nc = midc + midc - c;
}

void getsymhor(int midr, int r, int &nr)
{
	nr = midr + midr - r;
}

int temp[256][256];

int calcal(int sz)
{
	return (sz + 1) * (sz + 1);
}

int cal(int row, int col)
{
	memcpy(temp, arr, sizeof(arr));
	int ret = 0;
	for (int i = 0; i < n + n - 1; ++i) {
		int m = getnum(i);
		int stt = getstt(i);
		int edd = stt + (m - 1) * 2;
		for (int cur = stt; cur <= edd; ++cur) {
			if (i == row) {
				if (cur == col) {
					ret += temp[i][cur];
					continue;
				}
				else {
					ret += temp[i][cur] * 2;
					int nc = 0;
					getsymver(col, cur, nc);
					if (isvalid(i, nc)) {
						if (temp[i][nc] != temp[i][cur]) {
							return INF;
						}
						else {
							temp[i][nc] = 0;
						}
					}
					temp[i][cur] = 0;
				}
			}
			else {
				if (cur == col) {
					ret += temp[i][cur] * 2;
					int nr = 0;
					getsymhor(row, i, nr);
					if (isvalid(nr, cur)) {
						if (temp[nr][cur] != temp[i][cur]) {
							return INF;
						}
						else {
							temp[nr][cur] = 0;
						}
					}
					temp[i][cur] = 0;
				}
				else {
					int nr = 0, nc = 0;
					ret += temp[i][cur] * 4;
					getsymhor(row, i, nr);
					if (isvalid(nr, cur)) {
						if (temp[nr][cur] != temp[i][cur]) {
							return INF;
						}
						else {
							temp[nr][cur] = 0;
						}
					}

					getsymver(col, cur, nc);
					if (isvalid(i, nc)) {
						if (temp[i][nc] != temp[i][cur]) {
							return INF;
						}
						else {
							temp[i][nc] = 0;
						}
					}

					if (isvalid(nr, nc)) {
						if (temp[nr][nc] != temp[i][cur]) {
							return INF;
						}
						else {
							temp[nr][nc] = 0;
						}
					}
					temp[i][cur] = 0;
				}
			}
		}
	}
	int maxx = -1;
	for (int i = 0; i < n + n + 1; ++i) {
		int m = getnum(i);
		int stt = getstt(i);
		for (int j = 0, k = 0; j < m; ++j, k += 2) {
			maxx = max(maxx, abs(stt + k - col) + abs(i - row));
		}
	}
	return calcal(maxx);
}

int run()
{
	scanf("%d", &n);
	memset(arr, 0, sizeof(arr));
	int sm = 0;
	for (int i = 0; i < n + n - 1; ++i) {
		int m = getnum(i);
		int stt = getstt(i);
		for (int j = 0, k = 0; j < m; ++j, k += 2) {
			scanf("%d", &arr[i][stt + k]);
			++sm;
		}
	}
	int ret = INF;
	for (int hor = 0; hor < n + n - 1; ++hor) {
		int m = getnum(hor);
		int stt = getstt(hor);
		int edd = stt + (m - 1) * 2;
		for (int j = 0; j < n + n + 1; ++j) {
			ret = min(ret, cal(hor, j));
		}
	}
	return ret - sm;
}

int main()
{
	freopen("A2.in", "r", stdin);
	freopen("A2.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: %d\n", i, run());
	}
	return 0;
}