#include <cstdio>
#include <cstdlib>
#include <vector>
using namespace std;

int N, H, W, R;
vector<vector<bool> > avail;
vector<vector<int> > nways;

void inc(int r, int c, int amt) {
  if (r < H && c < W && avail[r][c]) {
    nways[r][c] = (nways[r][c]+amt) % 10007;
  }
}

int main() {
  scanf("%d", &N);
  for (int cnum = 1; cnum <= N; cnum++) {
    scanf("%d%d%d", &H, &W, &R);
    avail = vector<vector<bool> >(H, vector<bool>(W, true));
    nways = vector<vector<int> >(H, vector<int>(W, 0));
    for (int i = 0; i < R; i++) {
      int r, c;
      scanf("%d%d", &r, &c);
      avail[r-1][c-1] = false;
    }
    nways[0][0] = 1;
    for (int i = 0; i < H; i++) {
      for (int j = 0; j < W; j++) {
	if (nways[i][j] > 0) {
	  inc(i+2, j+1, nways[i][j]);
	  inc(i+1, j+2, nways[i][j]);
	}
      }
    }
    printf("Case #%d: %d\n", cnum, nways[H-1][W-1]);
  }
  return 0;
}
