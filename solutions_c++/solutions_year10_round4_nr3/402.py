#include <cstdio>
#include <cstring>

#define MAXN 200

char A[MAXN][MAXN];
char B[MAXN][MAXN];

int valid(int i, int j) { return i >= 0 && i < MAXN-2 && j >= 0 && j < MAXN-2; }

int step(char A[MAXN][MAXN], char B[MAXN][MAXN]) {

  for (int i = 0; i < MAXN; i++)
    for (int j = 0; j < MAXN; j++)
      if (A[i][j] == '1' && 
	  valid(i-1, j) &&
	  valid(i, j-1) &&
	  A[i-1][j] == '0' && A[i][j-1] == '0')
	B[i][j] = '0';
      else if (A[i][j] == '0' && 
	       valid(i-1, j) &&
	       valid(i, j-1) &&
	     A[i-1][j] == '1' && A[i][j-1] == '1')
	B[i][j] = '1';
      else 
	B[i][j] = A[i][j];

  int cnt = 0;
  for (int i = 0; i < MAXN; i++)
    for (int j = 0; j < MAXN; j++)
      if (B[i][j] == '1') cnt++;

  // for (int i = 0; i < MAXN; i++) {
  //   for (int j = 0; j < MAXN; j++)
  //     printf("%c", B[i][j]);
  //   printf("\n");
  // }

  // printf("\n");

  return cnt;
}

int main() {
  int C, R, cases = 1;

  scanf(" %d", &C);
  while (C--) {
    scanf(" %d", &R);
    
    memset(A, '0', sizeof(A));
    for (int k = 0; k < R; k++) {
      int x1, x2, y1, y2;
      scanf(" %d%d%d%d", &x1, &y1, &x2, &y2);
      for (int i = y1; i <= y2; i++)
	for (int j = x1; j <= x2; j++)
	  A[i][j] = '1';
    }

    // for (int i = 0; i < MAXN; i++) {
    //   for (int j = 0; j < MAXN; j++)
    // 	printf("%c", A[i][j]);
    //   printf("\n");
    // }

    // printf("\n");

    int res = 0;
    for (int i = 0; ; i++) {
      int ret = (i % 2 ? step(B, A) : step(A, B));
      res++;
      if (ret == 0)
	break;
    }      
    printf("Case #%d: %d\n", cases++, res);
  }

  return 0;
}
