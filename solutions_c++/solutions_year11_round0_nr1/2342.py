#include <cstdio>

using namespace std;

int d[1009], nextO[1009], nextB[1009], N; 
char R[1009];


void solve(int x, int y, int t, int i, int tc) {
  //printf("%d %d %d %d\n", x, y, t, i);
  if(i > N) {
    printf("Case #%d: %d\n", tc, t);
    return;
  }
  
  int dx, dy;
  if(nextO[i] > x) dx = 1;
  else if(nextO[i] == x) dx=0;
  else dx = -1;

  if(nextB[i] > y) dy = 1;
  else if(nextB[i] == y) dy = 0;
  else dy = -1;

  if(R[i]=='O' && x==d[i]) solve(x, y+dy, t+1, i+1, tc);
  else if(R[i]=='B' && y==d[i]) solve(x+dx, y, t+1, i+1, tc);
  else solve(x+dx, y+dy, t+1, i, tc);
}

int main() {
  int T; scanf("%d", &T);
  
  for(int tc=1; tc<=T; tc++) {
    scanf("%d", &N);
    for(int i=1; i<=N; i++) {
      do scanf("%c", &(R[i])); while(R[i]==' ' || R[i]=='\n');
      scanf("%d", &d[i]);
    }

    nextO[N+1] = nextB[N+1] = 100;
    for(int i=N; i>0; i--) {
      nextO[i] = nextO[i+1];
      nextB[i] = nextB[i+1];
      if(R[i]=='O') nextO[i] = d[i];
      if(R[i]=='B') nextB[i] = d[i];
    }
    solve(0,0,-1,1,tc);
  }
}
