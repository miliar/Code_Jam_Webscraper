#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int R, C;
char m[501][501];
int Rsum[501][501];
int Csum[501][501];

bool isOK(int r, int c, int k) {
  int delta;
  int rr = 0;
  int cc = 0;
  //printf("preverjam: r=%d c=%d k=%d\n", r, c, k);
  for (int i=r; i<r+k; i++) {
    delta = 0;
    if (i == r || i == r+k-1) delta = 1;
    if (k%2 == 1) {
      rr += (Csum[i][c+k-1-delta] - Csum[i][c-1+delta]) * (i - r - k/2);
    } else {
      if (i - r >= k/2) rr += (Csum[i][c+k-1-delta] - Csum[i][c-1+delta]) * (2*(i - r - k/2 + 1)-1); else rr += (Csum[i][c+k-1-delta] - Csum[i][c-1+delta]) * (2*(i - r - k/2)+1);
    }
  }
  for (int j=c; j<c+k; j++) {
    delta = 0;
    if (j == c || j == c+k-1) delta = 1;
    if (k%2 == 1) {
      cc += (Rsum[r+k-1-delta][j] - Rsum[r-1+delta][j]) * (j - c - k/2);
    } else {
      if (j - c >= k/2) cc += (Rsum[r+k-1-delta][j] - Rsum[r-1+delta][j]) * (2*(j - c - k/2 + 1)-1); else cc += (Rsum[r+k-1-delta][j] - Rsum[r-1+delta][j]) * (2*(j - c - k/2)+1);
    }
  }
  //printf("rr = %d, cc = %d\n", rr, cc);
  return (rr == 0) && (cc == 0);
}

int bruteForce() {
  int bestK = 0;
  for (int i=1; i<=R-2; i++) {
    for (int j=1; j<=C-2; j++) {
      for (int k=3; i+k-1<=R && j+k-1<=C; k++) {
        if (isOK(i, j, k)) {
          bestK = max(bestK, k);
        }
      }
    }
  }
  return bestK;
}

int main() {
  int T;
  char line[1000];
  
  scanf("%d\n", &T);
  for (int caseNum=1; caseNum<=T; caseNum++) {
    int D;
    for (int i=0; i<=500; i++) Rsum[0][i] = Csum[0][i] = Rsum[i][0] = Csum[i][0] = 0;
    scanf("%d %d %d\n", &R, &C, &D);
    for (int i=0; i<R; i++) {
      fgets(line, 1000, stdin);
      for (int j=0; j<C; j++) { m[i+1][j+1] = line[j] - '0';
      Rsum[i+1][j+1] = m[i+1][j+1];
      Rsum[i+1][j+1] += Rsum[i][j+1];
      Csum[i+1][j+1] = m[i+1][j+1];
      Csum[i+1][j+1] += Csum[i+1][j];}
    }
    
    /*for (int i=1; i<=R; i++) {
      for (int j=1; j<=C; j++) printf("%3d ", Rsum[i][j]);
      printf("\n");
    }*/
    
    int k = bruteForce();
    if (k == 0) printf("Case #%d: IMPOSSIBLE\n", caseNum); else printf("Case #%d: %d\n", caseNum, k);
    
  }
  return 0; 
}
