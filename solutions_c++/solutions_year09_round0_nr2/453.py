#include <cstdio>
#include <vector>

using namespace std;

const int MAXN = 128;

int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};

int h, w;

bool isok(int x, int y)
{
	return x >= 0 && x < h && y >= 0 && y < w;
}

int ht[MAXN][MAXN];
char res[MAXN][MAXN];

void go(const vector<pair<int, int> > &vp, int c)
{
	for (int i = 0; i < vp.size(); ++i) {
		res[vp[i].first][vp[i].second] = char('a' + c);
	}
}

void run(int t)
{
	scanf("%d %d", &h, &w);
	for (int i = 0; i < h; ++i) {
		for (int j = 0; j < w; ++j) {
			scanf("%d", ht[i] + j);
			res[i][j] = -1;
		}
	}
	int now = 0;
	for (int i = 0; i < h; ++i) {
		for (int j = 0; j < w; ++j) {
			if (res[i][j] != -1) continue;
			int xx = i, yy = j;
			vector<pair<int, int> > vp;
			vp.push_back(make_pair(xx, yy));
			while (1) {
				int minh = ht[xx][yy], minx, miny;
				for (int k = 0; k < 4; ++k) {
					int nx = xx + dx[k], ny = yy + dy[k];
					if (!isok(nx, ny)) continue;
					if (ht[nx][ny] < minh) {
						minh = ht[nx][ny];
						minx = nx;
						miny = ny;
					}
				}
				if (minh == ht[xx][yy]) {
					go(vp, now);
					++now;
					break;
				}
				else if (res[minx][miny] != -1) {
					go(vp, res[minx][miny] - 'a');
					break;
				}
				else {
					vp.push_back(make_pair(minx, miny));
					xx = minx;
					yy = miny;
				}
			}
		}
	}
	printf("Case #%d:\n", t);
	for (int i = 0; i < h; ++i) {
		for (int j = 0; j < w; ++j) {
			printf("%c%c", res[i][j], j == w - 1 ? '\n' : ' ');
		}
	}
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; ++tt) {
		run(tt);
	}
	return 0;
}