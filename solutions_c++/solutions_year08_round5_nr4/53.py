#include<stdio.h>
#include<stdlib.h>

int T;

#define MAXR 10
#define P 10007

int inv[P];
int exps[P];

void computeinv(){
  int G = 5;
  exps[0] = 1;
  for(int i = 1; i < P; i++){
    exps[i] = (exps[i-1]*G)%P;
  }
  for(int i = 0; i < P; i++){
    inv[exps[i]] = exps[P-i-1];
  }
}

int choose(int a, int b){
  int ans = 1;
  int nump = 0;
  for(int i = 1; i <= b; i++){
    int mul = a - (i - 1);
    int div = i;
    while(mul % P == 0) {
      mul = mul / P;
      nump++;
    }
    while(div % P == 0) {
      div /= P;
      nump--;
    }
    ans = (ans * (mul%P)) % P;
    ans = (ans * inv[div%P]) % P;
  }
  if (nump)
    return 0;
  return ans;
}

int numways(int dx, int dy){
  if ((dx+dy)%3)
    return 0;
  int m = (dx + dy)/3;
  if (dx < m || dy < m)
    return 0;
  return choose(m, dx-m);
}

int H, W;
int R;
int rocks[MAXR][2];

int rs[MAXR][2];

int compare(const void *a, const void *b){
  return ((int *)a)[0] - ((int *)b)[0];
}

int getnum(int set){
  int nr = 0;
  rs[0][0] = 1;
  rs[0][1] = 1;
  nr++;
  rs[1][0] = H;
  rs[1][1] = W;
  nr++;
  for(int i = 0; i < R; i++){
    if (set & (1<<i)){
      rs[nr][0] = rocks[i][0];
      rs[nr][1] = rocks[i][1];
      nr++;
    }
  }
  int bit = (nr%2) ? -1 : 1;
  qsort(rs, nr, sizeof(rs[0]), compare);
  int ans = 1;
  for(int i = 1; i < nr; i++){
    if (rs[i-1][1] > rs[i][1])
      return 0;
    ans = (ans * numways(rs[i][0] - rs[i-1][0],
			 rs[i][1] - rs[i-1][1]))%P;
  }
  return bit*ans;
}


int main(){
  int i;
  computeinv();
  scanf("%d", &T);
  for(int nc = 0; nc < T; nc++){
    printf("Case #%d: ", nc+1);
    scanf("%d %d %d", &H, &W, &R);
    for(i = 0; i < R; i++)
      scanf("%d %d", &rocks[i][0], &rocks[i][1]);
    int ans = 0;
    for(i = 0; i < 1<<R; i++){
      ans = (ans + getnum(i))%P;
    }
    printf("%d\n", (ans+P)%P);
  }
}
