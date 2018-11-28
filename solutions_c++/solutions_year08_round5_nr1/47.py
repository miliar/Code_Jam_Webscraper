#include<string.h>
#include<stdio.h>
#include<stdlib.h>

#define MAXN 6100
#define OFFSET 3050

int T;

int min(int a, int b){
  return a < b ? a : b;
}

int L;
int count[MAXN][MAXN][2];
int good[MAXN][MAXN];
int last[MAXN][2];
char strings[MAXN][50];
int rep[MAXN];

int dx[] = {1, 0,-1, 0};
int dy[] = {0,-1, 0, 1};
int c[] = {0, 1, 0, 1};

void runpath(){
  int x, y;
  x = y = OFFSET;
  int dir = 0;
  for(int i = 0; i < L; i++){
    for(int j = 0; j < rep[i]; j++){
      for(int k = 0; strings[i][k]; k++){
	switch(strings[i][k]){
	case 'L':
	  dir = (dir + 3)%4;
	  break;
	case 'R':
	  dir = (dir + 1)%4;
	  break;
	case 'F':
	  int nx = min(x, x+dx[dir]);
	  int ny = min(y, y+dy[dir]);
	  count[nx][ny][c[dir]]++;
	  x += dx[dir];
	  y += dy[dir];
	  break;
	}
      }
    }
  }
}

int main(){
  scanf("%d", &T);
  for(int nc = 0; nc < T; nc++){
    printf("Case #%d: ", nc+1);
    scanf("%d", &L);
    for(int i = 0; i < L; i++){
      scanf("%s %d", strings[i], &rep[i]);
    }
    memset(count, 0, sizeof(count));
    memset(good, 0, sizeof(good));
    runpath();
    int ans = 0;
    for(int i = 0; i < MAXN; i++){
      int numx = 0, numy = 0;
      for(int j = 0; j < MAXN; j++){
	numx += count[i][j][0];
	numy += count[j][i][1];
      }
      last[i][0] = numx;
      last[i][1] = numy;
    }
    for(int i = 0; i < MAXN; i++){
      int numx = 0, numy = 0;
      for(int j = 0; j < MAXN; j++){
	numx += count[i][j][0];
	numy += count[j][i][1];
	if (numx && numx != last[i][0] && !(numx%2)) {
	  good[i][j] = 1;
	}
	if (numy && numy != last[i][1] && !(numy%2)) {
	  good[j][i] = 1;
	}
      }
    }
    for(int i = 0; i < MAXN; i++){
      for(int j = 0; j < MAXN; j++){
	ans += good[i][j];
      }
    }
    printf("%d\n", ans);
    fflush(stdout);
  }
}
