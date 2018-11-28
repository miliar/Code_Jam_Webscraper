#include<stdio.h>
#include<stdlib.h>

#define MAXN 10000
#define AND 1
#define OR 0

int min(int a, int b){
  return a < b ? a : b;
}

int NOT(int x){
  if (x)
    return 0;
  return 1;
}

int T;
int gates[MAXN], change[MAXN];
int mins[MAXN][2];
int n, g;

int main(){
  int i, x;
  scanf("%d", &T);
  for(int nc = 0; nc < T; nc++){
    printf("Case #%d: ", nc+1);
    scanf("%d %d", &n, &g);
    for(i = 0; i < (n - 1) / 2; i++){
      scanf("%d", &gates[i]);
      scanf("%d", &change[i]);
    }
    for(; i < n; i++){
      scanf("%d", &x);
      mins[i][x] = 0;
      mins[i][NOT(x)] = MAXN+12;
    }
    for(i = (n-1)/2 - 1; i >= 0; i--){
      for(int j = 0; j < 2; j++){
	if (gates[i] ^ j) {
	  mins[i][j] = min(mins[2*i+1][NOT(gates[i])],
			   mins[2*i+2][NOT(gates[i])]);
	  if (change[i])
	    mins[i][j] = min(mins[i][j],
			     mins[2*i+1][NOT(gates[i])] +
			     mins[2*i+2][NOT(gates[i])] + 1);
	} else {
	  mins[i][j] = mins[2*i+1][gates[i]] + mins[2*i+2][gates[i]];
	  if (change[i])
	    mins[i][j] = min(mins[i][j],
			     min(mins[2*i+1][gates[i]],
				 mins[2*i+2][gates[i]]) + 1);
	}
      }
    }
    if (mins[0][g] > MAXN) {
      printf("IMPOSSIBLE\n");
    } else {
      printf("%d\n", mins[0][g]);
    }
  }
}
