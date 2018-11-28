#include <cstdio>
#include <algorithm>
using namespace std;

typedef long long ll;

ll W, H, D;
ll A[600][600];
ll X[600][600];
ll Y[600][600];
ll AP[600][600];
ll XP[600][600];
ll YP[600][600];

bool possible(ll size) {
  for(ll x = 0; x+size <= W; x++) for(ll y = 0; y+size <= H; y++) {
    ll cx = 2*x+size, cy = 2*y+size;
    ll asum = AP[y+size][x+size] - AP[y][x+size] - AP[y+size][x] + AP[y][x]; 
    ll xsum = XP[y+size][x+size] - XP[y][x+size] - XP[y+size][x] + XP[y][x];
    ll ysum = YP[y+size][x+size] - YP[y][x+size] - YP[y+size][x] + YP[y][x];
    asum -= A[y][x] + A[y][x+size-1] + A[y+size-1][x] + A[y+size-1][x+size-1];
    xsum -= X[y][x] + X[y][x+size-1] + X[y+size-1][x] + X[y+size-1][x+size-1];
    ysum -= Y[y][x] + Y[y][x+size-1] + Y[y+size-1][x] + Y[y+size-1][x+size-1];
//    fprintf(stderr, "x%lld,y%lld,size%lld: asum%lld xsum%lld ysum%lld\n", x, y, size, asum, xsum, ysum);
    if(xsum == cx*asum && ysum == cy*asum) return true;
  }
  return false;
}

int main() {
  ll T;
  scanf("%lld", &T);
  for(ll tid = 1; tid <= T; tid++) {
    scanf("%lld%lld%lld ", &H, &W, &D);
    for(ll y = 0; y < H; y++) {
      for(ll x = 0; x < W; x++) {
        A[y][x] = D + getchar()-'0';
        X[y][x] = A[y][x] * (2*x+1);
        Y[y][x] = A[y][x] * (2*y+1);
      }
      getchar();
    }
    for(ll y = 0; y < 550; y++) AP[0][y] = AP[y][0] = XP[0][y] = XP[y][0] = YP[0][y] = YP[y][0] = 0;
    for(ll y = 0; y < H; y++) for(ll x = 0; x < W; x++) {
      AP[y+1][x+1] = A[y][x] + AP[y][x+1] + AP[y+1][x] - AP[y][x];
      XP[y+1][x+1] = X[y][x] + XP[y][x+1] + XP[y+1][x] - XP[y][x];
      YP[y+1][x+1] = Y[y][x] + YP[y][x+1] + YP[y+1][x] - YP[y][x];
    }
    ll size;
    for(size = min(W, H); size >= 3; size--) {
      if(possible(size)) break;
    }
    if(size < 3) printf("Case #%lld: IMPOSSIBLE\n", tid);
    else printf("Case #%lld: %lld\n", tid, size);
  }
  return 0;
}

