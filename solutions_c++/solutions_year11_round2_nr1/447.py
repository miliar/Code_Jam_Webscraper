#include <stdio.h>


const int MAXN = 256;

char grid[MAXN][MAXN];
int ops[MAXN];
int wins[MAXN];
double wp[MAXN];
double owp[MAXN];
double oowp[MAXN];
double score[MAXN];

int main() {

  int T;
  scanf("%d", &T);

  for(int i = 0; i < T; ++i) {
    int n;
    scanf("%d", &n);
    for(int j = 0; j < n; ++j) {
      scanf("%s", grid[j]);
    }
    for(int j = 0; j < n; ++j) {
      wins[j] = 0;
      ops[j] = 0;
      wp[j] = 0;
      owp[j] = 0;
      oowp[j] = 0;
    }
    for(int j = 0; j < n; ++j) {
      for(int k = 0; k < n; ++k) {
	if(grid[j][k] == '1') {
	  ++wins[j];
	}
	if(grid[j][k] != '.') {
	  ++ops[j];
	}
      }
    }
    for(int j = 0; j < n; ++j) {
      for(int k = 0; k < n; ++k) {
	if(grid[j][k] == '1') {
	  wp[j] += 1.0 / ops[j];
	}
      }
    }
    for(int j = 0; j < n; ++j) {
      for(int k = 0; k < n; ++k) {
	if(grid[j][k] == '.') continue;
	owp[j] += (wp[k] * ops[k] - (grid[k][j]=='1'?1:0)) / (double)(ops[j] * (grid[j][k]=='.'?ops[k]:(ops[k]-1)));
      }
    }
    for(int j = 0; j < n; ++j) {
      for(int k = 0; k < n; ++k) {
	if(grid[j][k] == '.') continue;
	oowp[j] += owp[k] / (double)ops[j];
      }
    }
    printf("Case #%d:\n", 1+i);
    for(int j = 0; j < n; ++j) {
      score[j] =
	0.25 * wp[j]
	+ 0.5 * owp[j]
	+ 0.25 * oowp[j];
      printf("%.12lf\n", score[j]);
    }
  }


  return(0);
}
