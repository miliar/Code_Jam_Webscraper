#include <cstdio>

int T;
int k;
int A[51][51];

bool isok(int s, int ox, int oy) {
  int x, y;
  for(x = 0; x < k; x++) for(y = 0; y < k; y++) {
    int px = x+ox, py = y+oy;
    int hx = py, hy = px;
    int vx = s-1-py, vy = s-1-px;
    hx -= ox; hy -= oy;
    vx -= ox; vy -= oy;
    if(hx >= 0 && hx < k && hy >= 0 && hy < k && A[hx][hy] != A[x][y]) return 0;
    if(vx >= 0 && vx < k && vy >= 0 && vy < k && A[vx][vy] != A[x][y]) return 0;
  }
  return 1;
}

int main() {
  scanf("%d", &T);
  for(int tc=1;tc<=T;tc++) {
    scanf("%d", &k);
    int s,x,y,i;
    //input it
    for(i = 0; i < k+k+1; i++) {
      if(i < k) x = 0, y = i;
      else x = i-k+1, y = k-1;
      for(; x < k && y >= 0; x++, y--)
        scanf("%d", &A[x][y]);
    }
    //compute
    int ok = 0;
    for(s = k; s <= 3*k && !ok; s++) {
      for(x = 0; x+k <= s && !ok; x++) for(y = 0; y+k <= s && !ok; y++)
        if(/*x<=y && x+y<=s-1 &&*/ isok(s, x, y))
          ok = s;
    }
    printf("Case #%d: %d\n", tc, ok*ok-k*k);
  }
}

