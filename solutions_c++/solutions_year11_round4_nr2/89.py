#include <string.h>
#include <stdlib.h>
#include <stdio.h>


template <class T> inline T min(const T &a, const T &b) {
  return (a <= b) ? a : b;
}


const int MAXN = 1024;

long long grid[MAXN][MAXN];
long long sums_1[MAXN][MAXN];
long long sums_y[MAXN][MAXN];
long long sums_x[MAXN][MAXN];

int r,c;


int main() {


  int Tcases;
  scanf("%d", &Tcases);

  memset(sums_1, 0, MAXN*MAXN*sizeof(long long));
  memset(sums_x, 0, MAXN*MAXN*sizeof(long long));
  memset(sums_y, 0, MAXN*MAXN*sizeof(long long));

  for(int casen = 0; casen < Tcases; ++casen) {
    int d;
    scanf("%d %d %d", &r, &c, &d);

    char buffer[MAXN+1];
    for(int i = 0; i < r; ++i) {
      scanf("%s", buffer);
      for(int j = 0; j < c; ++j) {
	grid[i][j] = buffer[j] - '0';
      }
    }

    // for(int i = 0; i < r; ++i) {
    //   for(int j = 0; j < c; ++j) {
    // 	printf("%lld", grid[i][j]);
    //   }
    //   printf("\n");
    // }


    for(int i = 0; i < r; ++i) {
      for(int j = 0; j < c; ++j) {
	sums_1[i+1][j+1] = grid[i][j] + sums_1[i+1][j] + sums_1[i][j+1] - sums_1[i][j];
	sums_y[i+1][j+1] = i*(long long)grid[i][j] + sums_y[i+1][j] + sums_y[i][j+1] - sums_y[i][j];
	sums_x[i+1][j+1] = j*(long long)grid[i][j] + sums_x[i+1][j] + sums_x[i][j+1] - sums_x[i][j];
	//printf("%lld\t", sums_1[i+1][j+1]);
      }
      //printf("\n");
    }


    int best = 0;
    //printf("i\tj\tk\tm\tym\txm\n");
    for(int i = 0; i < r; ++i) {
      for(int j = 0; j < c; ++j) {
	int maxK = min(r-i, c-j);
	for(int k = 3; k <= maxK; ++k) {
	  if(k <= best) continue;
	  long long m = sums_1[i+k][j+k] - sums_1[i][j+k] - sums_1[i+k][j] + sums_1[i][j]
	    - grid[i][j] - grid[i+k-1][j] - grid[i][j+k-1] - grid[i+k-1][j+k-1];
	  long long ym = sums_y[i+k][j+k] - sums_y[i][j+k] - sums_y[i+k][j] + sums_y[i][j]
	    - i*grid[i][j] - i*grid[i][j+k-1] - (i+k-1)*grid[i+k-1][j] - (i+k-1)*grid[i+k-1][j+k-1];
	  long long xm = sums_x[i+k][j+k] - sums_x[i][j+k] - sums_x[i+k][j] + sums_x[i][j]
	    - j*grid[i][j] - j*grid[i+k-1][j] - (j+k-1)*grid[i][j+k-1] - (j+k-1)*grid[i+k-1][j+k-1];
	  //printf("%d\t%d\t%d\t%lld\t%lld\t%lld\n", i, j, k, m, ym, xm);
	  if(2*ym == m*(2*i+k-1) &&
	     2*xm == m*(2*j+k-1)) {
	    best = k;
	  }
	}
      }
    }

    if(best > 0) {
      printf("Case #%d: %d\n", 1+casen, best);
    } else {
      printf("Case #%d: IMPOSSIBLE\n", 1+casen);
    }
  }


  return(0);
}
