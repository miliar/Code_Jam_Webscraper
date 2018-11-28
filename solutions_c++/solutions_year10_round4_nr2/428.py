#include <algorithm>
#include <stdio.h>



const int BIG = 1000000000;
const int MAXN = 4096;
const int MAXR = 12;


int max_miss[MAXN];
int cost[MAXN];
int dp[2*MAXN][MAXR+1];


int main() {


  FILE* fin  = fopen("B.in",  "r");
  FILE* fout = fopen("B.out", "w");

  int tests;
  fscanf(fin, "%d", &tests);
  for(int casen = 1; casen <= tests; ++casen) {
    int rounds;
    fscanf(fin, "%d", &rounds);
    int n = 1 << rounds;

    for(int i = 0; i < n; ++i) {
      fscanf(fin, "%d", &max_miss[i]);
    }


    for(int i = 1; i <= rounds; ++i) {
      for(int j = 0; j < (1 << (rounds-i)); ++j) {
	fscanf(fin, "%d", &cost[(1<<(rounds-i))-1+j]);
      }
    }


//     printf("rounds = %d\n", rounds);
//     printf("n      = %d\n", n);
//     printf("max_miss =");
//     for(int i = 0; i < n; ++i) {
//       printf(" %d", max_miss[i]);
//     }
//     printf("\ncost =");
//     for(int i = 0; i < n-1; ++i) {
//       printf(" %d", cost[i]);
//     }
//     printf("\n\n");


    for(int i = 0; i < n; ++i) {
      for(int j = 0; j <= rounds; ++j) {
	if(j <= max_miss[i]) {
	  dp[n-1+i][j] = 0;
	} else {
	  dp[n-1+i][j] = BIG;
	}
      }
    }


    for(int i = n-2; i >= 0; --i) {
      int left  = 2*i+1;
      int right = 2*i+2;
      for(int j = 0; j <= rounds; ++j) {
	if(j == rounds) {
	  dp[i][j] = std::min(BIG, cost[i] + dp[left][j] + dp[right][j]);
	} else {
	  dp[i][j] =
	    std::min(cost[i] + dp[left][j] + dp[right][j],
		     std::min(BIG,
			      dp[left][j+1] + dp[right][j+1]));
	}
      }
    }

//     for(int i = 0; i < rounds; ++i) {
//       for(int j = 0; j < 2*n-1; ++j) {
// 	printf("%d ", dp[j][i]);
//       }
//       printf("\n");
//     }


    fprintf(fout, "Case #%d: %d\n", casen, dp[0][0]);

//     printf("\n\n");
//     printf("-------------------------------");
//     printf("\n\n");
  }

  fclose(fout);
  fclose(fin);


  return(0);
}
