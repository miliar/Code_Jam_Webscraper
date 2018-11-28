#include<iostream>
#include<vector>
using namespace std;

int att[100][100];
char tag[100][100];
char mat[100][100];
int T, W, H;

int dir[][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};


int main() {
	freopen("d:/input.in", "r", stdin);
	freopen("d:/output.out", "w", stdout);
	scanf("%d", &T);
	for (int tid=1; tid<=T; ++tid) {
		scanf("%d %d", &H, &W);
		for (int i=0; i<H; ++i) {
			for (int j=0; j<W; ++j)
				scanf("%d", &att[i][j]);
		}
		memset(tag, 0, sizeof tag);
		for (int r=0; r<H; ++r)
			for (int c=0; c<W; ++c) {
				int choose = -1;
				int best = att[r][c];
				for (int d=0; d<4; ++d) {
					int nr = r + dir[d][0];
					int nc = c + dir[d][1];
					if (nr >=0 && nr <H && nc>=0 && nc < W) {
						if (att[nr][nc] < best) {
							choose = d;
							best = att[nr][nc];
						}
					}
				}
				tag[r][c] = choose;
			}


		char label = 'a';
		memset(mat, 0, sizeof mat);
		vector<pair<int, int> > trace;
		for (int r=0; r<H; ++r)
			for (int c=0; c<W; ++c) {
				int cur_r = r;
				int cur_c = c;
				trace.clear();
				while(true) {
					if (mat[cur_r][cur_c]) {
						for (int i=0,sz=trace.size(); i<sz; ++i) 
							mat[trace[i].first][trace[i].second] = mat[cur_r][cur_c];
						break;
					}
					trace.push_back(make_pair(cur_r, cur_c) );
					int d = tag[cur_r][cur_c];
					if (d == -1) {
						for (int i=0,sz=trace.size(); i<sz; ++i) 
							mat[trace[i].first][trace[i].second] = label;
						label++;
						break;
					}
					cur_r += dir[d][0];
					cur_c += dir[d][1];
			
				}
			}
			printf("Case #%d:\n", tid);
			for (int r=0; r<H; ++r) {
				for (int c=0; c<W; ++c) {
					printf("%c", mat[r][c]);
					if (c == W-1)
						printf("\n");
					else
						printf(" ");
				}
			}
	}
	return 0;
}