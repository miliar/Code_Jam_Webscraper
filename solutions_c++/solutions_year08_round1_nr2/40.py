#include<stdio.h>
#include<stdlib.h>

#define MAXN 2100



int T;

int n;
int m;
int numunmalted[MAXN];
int unmalted[MAXN][MAXN];
int malted[MAXN];
int dead[MAXN];
int count;
int state[MAXN];
int done;

int main(){
  int x, y, z;
  int i;
  scanf("%d", &T);
  for(int nc = 0; nc < T; nc++){
    printf("Case #%d:", nc+1);


    scanf("%d", &n);
    for(i = 0; i < n; i++)
      state[i] = 0;
    scanf("%d", &m);
    for(i = 0; i < m; i++) {
      scanf("%d", &x);
      numunmalted[i] = 0;
      malted[i] = -1;
      dead[i] = 0;
      for(int j = 0; j < x; j++){
	scanf("%d %d", &y, &z);
	y--;
	if (z) {
	  malted[i] = y;
	} else {
	  unmalted[i][numunmalted[i]++] = y;
	}
      }
    }
    count = 0;
    while(true) {
      done = true;
      for (i = 0; i < m; i++){
	if (!dead[i] && !numunmalted[i]) {
	  done = false;
	  break;
	}
      }
      if (done)
	break;
      if (malted[i] == -1)
	break;
      int v = malted[i];
      state[v] = 1;
      for(i = 0; i < m; i++) {
	if (malted[i] == v)
	  dead[i] = 1;
	bool found = false;
	for(int j = 0; j < numunmalted[i]; j++) {
	  if (unmalted[i][j] == v) {
	    found = true;
	  }
	  if (found)
	    unmalted[i][j] = unmalted[i][j+1];
	}
	if (found)
	  numunmalted[i]--;
      }
    }
    if (done) {
      for(i = 0; i < n; i++){
	printf(" %d", state[i]);
      }
      printf("\n");
    } else {
      printf(" IMPOSSIBLE\n");
    }
  }
}
