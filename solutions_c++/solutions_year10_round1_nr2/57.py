#include <stdlib.h>
#include <stdio.h>

template<class T> inline T min(const T &a, const T &b) {
  if(a < b) {
    return(a);
  }
  return(b);
}


int delete_cost;
int insert_cost;
int max_diff;
int n;

//const int BIG = 1000000000;

const int MAXN = 1024;
int pixel[MAXN];
int dp[MAXN][256];


int main() {

  FILE* fin = fopen("B.in", "r");
  FILE* fout = fopen("B.out", "w");

  int tests;
  fscanf(fin, "%d", &tests);
  for(int t = 0; t < tests; ++t) {

    printf("TEST %d-------------------\n", 1+t);

    fscanf(fin, "%d %d %d %d", &delete_cost, &insert_cost, &max_diff, &n);
    printf("%d %d %d %d\n", delete_cost, insert_cost, max_diff, n);
    for(int i = 0; i < n; ++i) {
      fscanf(fin, "%d", &pixel[i]);
      printf("%d ", pixel[i]);
    }
    printf("\n");

    for(int j = 0; j < 256; ++j) {
      dp[0][j] = min(delete_cost, abs(j - pixel[0]));
    }

    for(int i = 1; i < n; ++i) {
      for(int j = 0; j < 256; ++j) {
	dp[i][j] = delete_cost + dp[i-1][j];
	if(max_diff == 0) {
	  dp[i][j] = min(dp[i][j], dp[i-1][j] + abs(j - pixel[i]));
	} else {
	  for(int v = 0; v < 256; ++v) {
	    int q = (v == j) ? 0 : ((abs(v - j) - 1) / max_diff);
	    dp[i][j] = min(dp[i][j], dp[i-1][v] + abs(j - pixel[i]) + q * insert_cost);
	  }
	}
	//printf("dp[%d][%d] = %d\n", i, j, dp[i][j]);
      }
    }

    int ans = dp[n-1][0];
    for(int j = 0; j < 256; ++j) {
      ans = min(ans, dp[n-1][j]);
    }

    printf("ans = %d\n", ans);

    fprintf(fout, "Case #%d: %d\n", 1+t, ans);
    

  }



  return(0);
}
