#include <assert.h>
#include <stdio.h>

const int dy[4] = {-1, 0, 0,+1};
const int dx[4] = { 0,-1,+1, 0};
const int MAXN = 128;
int h,w;
int alt[MAXN][MAXN];
int sink[MAXN][MAXN];
char letter[MAXN][MAXN];


int find_sink(int r, int c) {
  if(sink[r][c] != -1) return(sink[r][c]);

  int rp=-1,cp=-1;
  for(int d = 0; d < 4; ++d) {
    int r2 = r+dy[d];
    int c2 = c+dx[d];
    if(!(0 <= r2 && r2 < h)) continue;
    if(!(0 <= c2 && c2 < w)) continue;
    if(alt[r2][c2] >= alt[r][c]) continue;
    if(rp == -1 || alt[rp][cp] > alt[r2][c2]) {
      rp = r2;
      cp = c2;
    }
  }

  if(rp == -1) {
    sink[r][c] = r*w+c;
    return(sink[r][c]);
  }

  sink[r][c] = find_sink(rp,cp);
  return(sink[r][c]);
}


int main() {

  int ncases;
  scanf("%d", &ncases);
  for(int caseNum = 0; caseNum < ncases; ++caseNum) {
    scanf("%d %d", &h, &w);
    for(int i = 0; i < h; ++i) {
      for(int j = 0; j < w; ++j) {
	scanf("%d", &alt[i][j]);
	sink[i][j] = -1;
	letter[i][j] = '?';
      }
    }

    for(int i = 0; i < h; ++i) {
      for(int j = 0; j < w; ++j) {
	int s = find_sink(i,j);
      }
    }

    char l = 'a';
    for(int i = 0; i < h; ++i) {
      for(int j = 0; j < w; ++j) {
	int s = sink[i][j];
	if(letter[s/w][s%w] == '?') {
	  assert(l <= 'z');
	  letter[s/w][s%w] = l;
	  ++l;
	}
	letter[i][j] = letter[s/w][s%w];
	assert('a' <= letter[i][j] && letter[i][j] <= 'z');
      }
    }

    printf("Case #%d:\n", caseNum+1);
    for(int i = 0; i < h; ++i) {
      for(int j = 0; j < w; ++j) {
	printf("%c%c", letter[i][j], (j==w-1) ? '\n' : ' ');
      }
    }
  }

  return(0);
}
