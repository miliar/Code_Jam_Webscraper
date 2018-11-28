#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>

using namespace std;

#define MAXN 101

int tab[MAXN][MAXN];
int res[MAXN][MAXN];
int h,w;
char c;

int dx[] = { 0, -1, 1, 0 };
int dy[] = { -1, 0, 0, 1 };

#define ok(y,x) (x >= 0 && x < w && y >= 0 && y < h)

int dfs(int i, int j) {
  if (res[i][j] != -1) return res[i][j];
  int mini = -1;
  int mina = tab[i][j];
  for (int k = 0; k < 4; k++) {
    int ii = i + dy[k];
    int jj = j + dx[k];
    if (!ok(ii,jj)) continue;
    if (tab[ii][jj] < mina) {
      mina = tab[ii][jj];
      mini = k;
    }
  }
  if (mini == -1) {
    c++;
    res[i][j] = c;
  }
  else {
    res[i][j] = dfs(i + dy[mini],j+dx[mini]);
  }
  return res[i][j];
}
  

int main() {
  int k;
  scanf("%d",&k);
  int test = 0;
  while (k--) {
    test++;
    printf("Case #%d:\n",test);
    scanf("%d %d",&h,&w);
    for (int i = 0; i < h; i++) {
      for (int j = 0; j < w; j++) {
	scanf("%d",&tab[i][j]);
      }
    }
    memset(res,-1,sizeof(res));
    c = 'a' -1;
    for (int i = 0; i < h; i++) {
      for (int j = 0; j < w; j++) {
	if (res[i][j] == -1) {
	  dfs(i,j);
	}
      }
    }
    for (int i = 0; i < h; i++) {
      for (int j = 0; j < w; j++) {
	if (j != 0) printf(" ");
	printf("%c",res[i][j]);
      }
      printf("\n");
    }
    
  }
  return 0;
}
