#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <queue>

using namespace std;

struct point {
	int x, y;
};

FILE *fp_r, *fp_w;
int t, h, w;
int mp[100][100], nx[100][100], con[100][100][100][100];
int d[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
int visit[100][100];
point p;
queue<point> q;

int main() {
	fp_r = fopen("b.in", "r");
	fp_w = fopen("b.out", "w");

	fscanf(fp_r, "%d", &t);
	for(int i = 0; i < t; ++i) {
		fscanf(fp_r, "%d %d", &h, &w);

		for(int j = 0; j < h; ++j)
			for(int k = 0; k < w; ++k)
				fscanf(fp_r, "%d", &mp[j][k]);

		memset(con, 0, sizeof(con));
		for(int j = 0; j < h; ++j) {
			for(int k = 0; k < w; ++k) {
				int minv = mp[j][k];
				nx[j][k] = -1;
				for(int l = 0; l < 4; ++l) {
					int px = j + d[l][0];
					int py = k + d[l][1];
					if (px < 0 || px >= h || py < 0 || py >= w) continue;
					if (minv > mp[px][py]) {
						minv = mp[px][py];
						nx[j][k] = l;
					}
				}
				if (nx[j][k] != -1) {
					con[j][k][j+d[nx[j][k]][0]][k+d[nx[j][k]][1]] = 1;
					con[j+d[nx[j][k]][0]][k+d[nx[j][k]][1]][j][k] = 1;
				}
			}
		}

		int cnt = 0;
		memset(visit, 0, sizeof(visit));
		for(int j = 0; j < h; ++j) {
			for(int k = 0; k < w; ++k) {
				if (visit[j][k] > 0) continue;
				p.x = j;	p.y = k;
				q.push(p);
				visit[j][k] = ++cnt;
				while(1) {
					if (q.empty()) break;

					for(int l = 0; l < 4; ++l) {
						p.x = q.front().x + d[l][0];
						p.y = q.front().y + d[l][1];
						if (p.x < 0 || p.x >= h || p.y < 0 || p.y >= w) continue;
						if (con[q.front().x][q.front().y][p.x][p.y] == 0) continue;
						if (visit[p.x][p.y] != 0) continue;

						visit[p.x][p.y] = cnt;
						q.push(p);
					}

					q.pop();
				}
			}
		}
		
		fprintf(fp_w, "Case #%d:\n", i+1);
		for(int j = 0; j < h; ++j) {
			for(int k = 0; k < w; ++k) {
				if (k != 0) fprintf(fp_w, " ");
				fprintf(fp_w, "%c", visit[j][k]-1+'a');
			}
			fprintf(fp_w, "\n");
		}
	}	

	fclose(fp_r);
	fclose(fp_w);

	return 0;
}