#include <iostream>
#include <string.h>
using namespace std;
int T,H,W,m[100][100],l[100][100],k;
void solve(int N, int M);
int main() {
  int i,j,tests=0;
  scanf("%d",&T);
  while (T--) {
    scanf("%d %d",&H,&W);
    memset(l,-1,sizeof(l));
    for (i = 0 ; i < H ; i++) {
      for (j = 0 ; j < W ; j++) {
	scanf("%d",&m[i][j]);
      }
    }
    k = -1;
    for (i = 0 ; i < H ; i++) 
      for (j = 0 ; j < W ; j++)
	solve(i,j);
    printf("Case #%d:\n",++tests);
    for (i = 0 ; i < H ; i++) {
      for (j = 0 ; j < W ; j++) {
	if (j == W-1)
	  printf("%c\n",l[i][j]+'a');
	else printf("%c ",l[i][j]+'a');
      }
    }
  }
  return 0;
}
void solve(int N, int M) {
  int max = 1000;
  if (l[N][M] != -1) return;
  int i=N,j=M;
  if (N != 0) {
      if (m[N-1][M] < m[i][j]) {
	i = N-1;
	j = M;
      }
  }
  if (M != 0) {
    if (m[N][M-1] < m[i][j]) {
      i = N;
      j = M-1;
    }
  }
  if (M != W-1) {
    if (m[N][M+1] < m[i][j]) {
      i = N;
      j = M+1;
    }
  }
  if (N != H-1) {
    if (m[N+1][M] < m[i][j]) {
      i = N+1;
      j = M;
    }
  }
  if (i == N && j == M) {
    k++;
    l[i][j] = k;
    return;
  }
  else {
    solve(i,j);
    l[N][M] = l[i][j];
  }
}
